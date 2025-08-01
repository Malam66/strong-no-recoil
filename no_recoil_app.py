import tkinter as tk
from tkinter import ttk, messagebox
import json
import threading
import time
from pynput import mouse, keyboard
import keyboard as kb
import mouse as ms

class NoRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Strong No Recoil")
        self.root.geometry("500x600")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(False, False)
        
        # Variables
        self.recoil_enabled = tk.BooleanVar(value=False)
        self.rapid_fire_enabled = tk.BooleanVar(value=False)
        self.require_ads = tk.BooleanVar(value=True)
        self.caps_lock_toggle = tk.BooleanVar(value=False)
        
        self.vertical_strength = tk.IntVar(value=8)
        self.horizontal_strength = tk.IntVar(value=2)
        self.recoil_delay = tk.DoubleVar(value=0.01)
        self.rapid_fire_speed = tk.IntVar(value=50)
        
        self.current_mode = tk.StringVar(value="HEAVY")
        self.config_slot = tk.IntVar(value=1)
        
        # Threading
        self.recoil_thread = None
        self.rapid_fire_thread = None
        self.running = False
        
        # Mode presets
        self.modes = {
            "LIGHT": {"vertical": 3, "horizontal": 1, "delay": 0.02},
            "MEDIUM": {"vertical": 6, "horizontal": 2, "delay": 0.015},
            "HEAVY": {"vertical": 8, "horizontal": 2, "delay": 0.01}
        }
        
        self.setup_ui()
        self.load_config()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="STRONG NO RECOIL", 
                             font=('Arial', 16, 'bold'), 
                             fg='#ffffff', bg='#1a1a1a')
        title_label.pack(pady=(0, 20))
        
        # Configuration Section
        config_frame = self.create_section(main_frame, "CONFIGURATION")
        
        config_buttons_frame = tk.Frame(config_frame, bg='#2a2a2a')
        config_buttons_frame.pack(fill='x', pady=5)
        
        tk.Button(config_buttons_frame, text="LOAD CONFIG", 
                 command=self.load_config, bg='#404040', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left', padx=(0, 10))
        
        tk.Button(config_buttons_frame, text="SAVE CONFIG", 
                 command=self.save_config, bg='#404040', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left')
        
        # Config slot selector
        slot_frame = tk.Frame(config_frame, bg='#2a2a2a')
        slot_frame.pack(fill='x', pady=5)
        
        tk.Label(slot_frame, text="Slot:", bg='#2a2a2a', fg='#ffffff').pack(side='left')
        slot_spinbox = tk.Spinbox(slot_frame, from_=1, to=10, width=5,
                                 textvariable=self.config_slot, bg='#404040', fg='#ffffff')
        slot_spinbox.pack(side='left', padx=(5, 0))
        
        # Anti-Recoil Section
        recoil_frame = self.create_section(main_frame, "ANTI-RECOIL")
        
        # Toggle controls
        tk.Checkbutton(recoil_frame, text="TOGGLE RECOIL SCRIPT", 
                      variable=self.recoil_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#2a2a2a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(recoil_frame, text="REQUIRE ADS (Aim Down Sight)", 
                      variable=self.require_ads, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#2a2a2a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # Strength controls
        strength_frame = tk.Frame(recoil_frame, bg='#2a2a2a')
        strength_frame.pack(fill='x', pady=10)
        
        tk.Label(strength_frame, text="VERTICAL STRENGTH:", bg='#2a2a2a', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.vertical_strength, 0, 15)
        
        tk.Label(strength_frame, text="HORIZONTAL STRENGTH:", bg='#2a2a2a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(strength_frame, self.horizontal_strength, 0, 10)
        
        tk.Label(strength_frame, text="DELAY (seconds):", bg='#2a2a2a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(strength_frame, self.recoil_delay, 0.001, 0.1, is_float=True)
        
        # Rapid Fire Section
        rapid_frame = self.create_section(main_frame, "RAPID FIRE")
        
        tk.Checkbutton(rapid_frame, text="TOGGLE RAPID FIRE SCRIPT", 
                      variable=self.rapid_fire_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#2a2a2a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(rapid_frame, text="REQUIRE ADS (Aim Down Sight)", 
                      variable=self.require_ads, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#2a2a2a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Label(rapid_frame, text="SPEED (ms):", bg='#2a2a2a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(rapid_frame, self.rapid_fire_speed, 10, 200)
        
        # Mode Selection
        mode_frame = self.create_section(main_frame, "MODE SELECTION")
        
        mode_buttons_frame = tk.Frame(mode_frame, bg='#2a2a2a')
        mode_buttons_frame.pack(fill='x', pady=5)
        
        for mode in ["LIGHT", "MEDIUM", "HEAVY"]:
            tk.Button(mode_buttons_frame, text=mode, 
                     command=lambda m=mode: self.set_mode(m),
                     bg='#404040' if mode == "HEAVY" else '#2a2a2a', 
                     fg='#ffffff', relief='flat', padx=10, pady=5).pack(side='left', padx=(0, 5))
        
        # Status Section
        status_frame = self.create_section(main_frame, "STATUS")
        
        self.status_label = tk.Label(status_frame, text="Status: DISABLED", 
                                   bg='#2a2a2a', fg='#ff4444', font=('Arial', 10, 'bold'))
        self.status_label.pack(anchor='w')
        
        self.mode_label = tk.Label(status_frame, text="Mode: HEAVY", 
                                 bg='#2a2a2a', fg='#ffffff')
        self.mode_label.pack(anchor='w', pady=(5, 0))
        
        # Control Buttons
        buttons_frame = tk.Frame(main_frame, bg='#1a1a1a')
        buttons_frame.pack(fill='x', pady=(20, 0))
        
        tk.Button(buttons_frame, text="START/STOP", 
                 command=self.toggle_recoil, bg='#ff4444', fg='#ffffff',
                 relief='flat', padx=20, pady=10, font=('Arial', 12, 'bold')).pack(side='left', padx=(0, 10))
        
        tk.Button(buttons_frame, text="EXIT", 
                 command=self.root.quit, bg='#404040', fg='#ffffff',
                 relief='flat', padx=20, pady=10).pack(side='right')
        
        # Bind events
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_section(self, parent, title):
        frame = tk.Frame(parent, bg='#2a2a2a', relief='flat', bd=1)
        frame.pack(fill='x', pady=(10, 0))
        
        tk.Label(frame, text=title, bg='#2a2a2a', fg='#ffffff', 
                font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=5)
        
        content_frame = tk.Frame(frame, bg='#2a2a2a')
        content_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        return content_frame
    
    def create_slider_with_entry(self, parent, variable, min_val, max_val, is_float=False):
        frame = tk.Frame(parent, bg='#2a2a2a')
        frame.pack(fill='x', pady=2)
        
        slider = tk.Scale(frame, from_=min_val, to=max_val, variable=variable,
                         orient='horizontal', bg='#2a2a2a', fg='#ffffff',
                         highlightbackground='#2a2a2a', troughcolor='#404040')
        slider.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        if is_float:
            entry = tk.Entry(frame, textvariable=variable, width=8, bg='#404040', fg='#ffffff')
        else:
            entry = tk.Entry(frame, textvariable=variable, width=8, bg='#404040', fg='#ffffff')
        entry.pack(side='right')
        
        return slider, entry
    
    def set_mode(self, mode):
        self.current_mode.set(mode)
        preset = self.modes[mode]
        self.vertical_strength.set(preset["vertical"])
        self.horizontal_strength.set(preset["horizontal"])
        self.recoil_delay.set(preset["delay"])
        self.mode_label.config(text=f"Mode: {mode}")
    
    def toggle_recoil(self):
        if not self.running:
            self.start_recoil()
        else:
            self.stop_recoil()
    
    def start_recoil(self):
        if not self.recoil_enabled.get() and not self.rapid_fire_enabled.get():
            messagebox.showwarning("Warning", "Please enable at least one feature!")
            return
        
        self.running = True
        self.status_label.config(text="Status: ENABLED", fg='#44ff44')
        
        if self.recoil_enabled.get():
            self.recoil_thread = threading.Thread(target=self.recoil_loop, daemon=True)
            self.recoil_thread.start()
        
        if self.rapid_fire_enabled.get():
            self.rapid_fire_thread = threading.Thread(target=self.rapid_fire_loop, daemon=True)
            self.rapid_fire_thread.start()
    
    def stop_recoil(self):
        self.running = False
        self.status_label.config(text="Status: DISABLED", fg='#ff4444')
    
    def recoil_loop(self):
        while self.running:
            try:
                if kb.is_pressed('mouse1'):  # Left mouse button
                    if not self.require_ads.get() or kb.is_pressed('mouse2'):  # Right mouse for ADS
                        # Apply recoil compensation
                        vertical = self.vertical_strength.get()
                        horizontal = self.horizontal_strength.get()
                        
                        if vertical > 0:
                            ms.move(0, vertical, absolute=False)
                        if horizontal > 0:
                            ms.move(horizontal, 0, absolute=False)
                        
                        time.sleep(self.recoil_delay.get())
                
                time.sleep(0.001)  # Small delay to prevent high CPU usage
            except Exception as e:
                print(f"Recoil error: {e}")
                break
    
    def rapid_fire_loop(self):
        while self.running:
            try:
                if kb.is_pressed('mouse1'):
                    if not self.require_ads.get() or kb.is_pressed('mouse2'):
                        # Rapid fire logic
                        speed = self.rapid_fire_speed.get() / 1000.0
                        time.sleep(speed)
                        # Simulate rapid clicking
                        ms.click()
                
                time.sleep(0.001)
            except Exception as e:
                print(f"Rapid fire error: {e}")
                break
    
    def save_config(self):
        config = {
            "recoil_enabled": self.recoil_enabled.get(),
            "rapid_fire_enabled": self.rapid_fire_enabled.get(),
            "require_ads": self.require_ads.get(),
            "vertical_strength": self.vertical_strength.get(),
            "horizontal_strength": self.horizontal_strength.get(),
            "recoil_delay": self.recoil_delay.get(),
            "rapid_fire_speed": self.rapid_fire_speed.get(),
            "current_mode": self.current_mode.get()
        }
        
        try:
            with open(f"config_{self.config_slot.get()}.json", "w") as f:
                json.dump(config, f)
            messagebox.showinfo("Success", f"Configuration saved to slot {self.config_slot.get()}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save config: {e}")
    
    def load_config(self):
        try:
            with open(f"config_{self.config_slot.get()}.json", "r") as f:
                config = json.load(f)
            
            self.recoil_enabled.set(config.get("recoil_enabled", False))
            self.rapid_fire_enabled.set(config.get("rapid_fire_enabled", False))
            self.require_ads.set(config.get("require_ads", True))
            self.vertical_strength.set(config.get("vertical_strength", 8))
            self.horizontal_strength.set(config.get("horizontal_strength", 2))
            self.recoil_delay.set(config.get("recoil_delay", 0.01))
            self.rapid_fire_speed.set(config.get("rapid_fire_speed", 50))
            self.current_mode.set(config.get("current_mode", "HEAVY"))
            
            self.mode_label.config(text=f"Mode: {self.current_mode.get()}")
            messagebox.showinfo("Success", f"Configuration loaded from slot {self.config_slot.get()}")
        except FileNotFoundError:
            messagebox.showwarning("Warning", f"No configuration found in slot {self.config_slot.get()}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load config: {e}")
    
    def on_closing(self):
        self.stop_recoil()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoRecoilApp(root)
    root.mainloop() 