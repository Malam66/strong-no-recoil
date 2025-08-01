import tkinter as tk
from tkinter import ttk, messagebox
import json
import threading
import time
import math
from pynput import mouse, keyboard
import keyboard as kb
import mouse as ms

class AdvancedNoRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Strong No Recoil")
        self.root.geometry("600x700")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        # Enhanced Variables
        self.recoil_enabled = tk.BooleanVar(value=False)
        self.rapid_fire_enabled = tk.BooleanVar(value=False)
        self.require_ads = tk.BooleanVar(value=True)
        self.auto_trigger = tk.BooleanVar(value=False)
        self.smart_recoil = tk.BooleanVar(value=True)
        
        # Advanced recoil settings
        self.vertical_strength = tk.IntVar(value=12)
        self.horizontal_strength = tk.IntVar(value=3)
        self.recoil_delay = tk.DoubleVar(value=0.008)
        self.recoil_pattern = tk.StringVar(value="LINEAR")
        self.recoil_curve = tk.DoubleVar(value=1.5)
        
        # Rapid fire settings
        self.rapid_fire_speed = tk.IntVar(value=30)
        self.burst_mode = tk.BooleanVar(value=False)
        self.burst_count = tk.IntVar(value=3)
        
        # Advanced settings
        self.current_mode = tk.StringVar(value="EXTREME")
        self.config_slot = tk.IntVar(value=1)
        self.sensitivity_multiplier = tk.DoubleVar(value=1.0)
        
        # Threading
        self.recoil_thread = None
        self.rapid_fire_thread = None
        self.running = False
        self.shot_count = 0
        
        # Enhanced mode presets
        self.modes = {
            "LIGHT": {"vertical": 4, "horizontal": 1, "delay": 0.015, "curve": 1.0},
            "MEDIUM": {"vertical": 8, "horizontal": 2, "delay": 0.012, "curve": 1.2},
            "HEAVY": {"vertical": 12, "horizontal": 3, "delay": 0.008, "curve": 1.5},
            "EXTREME": {"vertical": 15, "horizontal": 4, "delay": 0.005, "curve": 2.0}
        }
        
        self.setup_ui()
        self.load_config()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#0a0a0a', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="ADVANCED STRONG NO RECOIL", 
                             font=('Arial', 18, 'bold'), 
                             fg='#ff4444', bg='#0a0a0a')
        title_label.pack(pady=(0, 20))
        
        # Configuration Section
        config_frame = self.create_section(main_frame, "CONFIGURATION")
        
        config_buttons_frame = tk.Frame(config_frame, bg='#1a1a1a')
        config_buttons_frame.pack(fill='x', pady=5)
        
        tk.Button(config_buttons_frame, text="LOAD CONFIG", 
                 command=self.load_config, bg='#404040', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left', padx=(0, 10))
        
        tk.Button(config_buttons_frame, text="SAVE CONFIG", 
                 command=self.save_config, bg='#404040', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left')
        
        # Config slot selector
        slot_frame = tk.Frame(config_frame, bg='#1a1a1a')
        slot_frame.pack(fill='x', pady=5)
        
        tk.Label(slot_frame, text="Slot:", bg='#1a1a1a', fg='#ffffff').pack(side='left')
        slot_spinbox = tk.Spinbox(slot_frame, from_=1, to=20, width=5,
                                 textvariable=self.config_slot, bg='#404040', fg='#ffffff')
        slot_spinbox.pack(side='left', padx=(5, 0))
        
        # Anti-Recoil Section
        recoil_frame = self.create_section(main_frame, "ADVANCED ANTI-RECOIL")
        
        # Toggle controls
        tk.Checkbutton(recoil_frame, text="TOGGLE RECOIL SCRIPT", 
                      variable=self.recoil_enabled, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#1a1a1a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(recoil_frame, text="REQUIRE ADS (Aim Down Sight)", 
                      variable=self.require_ads, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#1a1a1a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(recoil_frame, text="SMART RECOIL PATTERN", 
                      variable=self.smart_recoil, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#1a1a1a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # Advanced strength controls
        strength_frame = tk.Frame(recoil_frame, bg='#1a1a1a')
        strength_frame.pack(fill='x', pady=10)
        
        tk.Label(strength_frame, text="VERTICAL STRENGTH:", bg='#1a1a1a', fg='#ff4444').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.vertical_strength, 0, 20)
        
        tk.Label(strength_frame, text="HORIZONTAL STRENGTH:", bg='#1a1a1a', fg='#ff4444').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(strength_frame, self.horizontal_strength, 0, 15)
        
        tk.Label(strength_frame, text="DELAY (seconds):", bg='#1a1a1a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(strength_frame, self.recoil_delay, 0.001, 0.05, is_float=True)
        
        # Recoil pattern selection
        pattern_frame = tk.Frame(recoil_frame, bg='#1a1a1a')
        pattern_frame.pack(fill='x', pady=10)
        
        tk.Label(pattern_frame, text="RECOIL PATTERN:", bg='#1a1a1a', fg='#ffffff').pack(anchor='w')
        pattern_combo = ttk.Combobox(pattern_frame, textvariable=self.recoil_pattern,
                                    values=["LINEAR", "EXPONENTIAL", "LOGARITHMIC", "CUSTOM"],
                                    state="readonly", width=15)
        pattern_combo.pack(anchor='w', pady=2)
        
        tk.Label(pattern_frame, text="CURVE INTENSITY:", bg='#1a1a1a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(pattern_frame, self.recoil_curve, 0.5, 3.0, is_float=True)
        
        # Rapid Fire Section
        rapid_frame = self.create_section(main_frame, "ADVANCED RAPID FIRE")
        
        tk.Checkbutton(rapid_frame, text="TOGGLE RAPID FIRE SCRIPT", 
                      variable=self.rapid_fire_enabled, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#1a1a1a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(rapid_frame, text="BURST MODE", 
                      variable=self.burst_mode, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#404040', activebackground='#1a1a1a',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Label(rapid_frame, text="SPEED (ms):", bg='#1a1a1a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(rapid_frame, self.rapid_fire_speed, 5, 100)
        
        tk.Label(rapid_frame, text="BURST COUNT:", bg='#1a1a1a', fg='#ffffff').pack(anchor='w', pady=(10, 0))
        self.create_slider_with_entry(rapid_frame, self.burst_count, 2, 10)
        
        # Mode Selection
        mode_frame = self.create_section(main_frame, "MODE SELECTION")
        
        mode_buttons_frame = tk.Frame(mode_frame, bg='#1a1a1a')
        mode_buttons_frame.pack(fill='x', pady=5)
        
        for mode in ["LIGHT", "MEDIUM", "HEAVY", "EXTREME"]:
            bg_color = '#ff4444' if mode == "EXTREME" else '#404040' if mode == "HEAVY" else '#2a2a2a'
            tk.Button(mode_buttons_frame, text=mode, 
                     command=lambda m=mode: self.set_mode(m),
                     bg=bg_color, fg='#ffffff', relief='flat', padx=8, pady=5).pack(side='left', padx=(0, 5))
        
        # Status Section
        status_frame = self.create_section(main_frame, "STATUS & MONITORING")
        
        self.status_label = tk.Label(status_frame, text="Status: DISABLED", 
                                   bg='#1a1a1a', fg='#ff4444', font=('Arial', 10, 'bold'))
        self.status_label.pack(anchor='w')
        
        self.mode_label = tk.Label(status_frame, text="Mode: EXTREME", 
                                 bg='#1a1a1a', fg='#ffffff')
        self.mode_label.pack(anchor='w', pady=(5, 0))
        
        self.shots_label = tk.Label(status_frame, text="Shots Fired: 0", 
                                  bg='#1a1a1a', fg='#44ff44')
        self.shots_label.pack(anchor='w', pady=(5, 0))
        
        # Control Buttons
        buttons_frame = tk.Frame(main_frame, bg='#0a0a0a')
        buttons_frame.pack(fill='x', pady=(20, 0))
        
        tk.Button(buttons_frame, text="START/STOP", 
                 command=self.toggle_recoil, bg='#ff4444', fg='#ffffff',
                 relief='flat', padx=20, pady=10, font=('Arial', 12, 'bold')).pack(side='left', padx=(0, 10))
        
        tk.Button(buttons_frame, text="RESET COUNTER", 
                 command=self.reset_counter, bg='#404040', fg='#ffffff',
                 relief='flat', padx=15, pady=10).pack(side='left', padx=(0, 10))
        
        tk.Button(buttons_frame, text="EXIT", 
                 command=self.root.quit, bg='#404040', fg='#ffffff',
                 relief='flat', padx=20, pady=10).pack(side='right')
        
        # Bind events
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_section(self, parent, title):
        frame = tk.Frame(parent, bg='#1a1a1a', relief='flat', bd=1)
        frame.pack(fill='x', pady=(10, 0))
        
        tk.Label(frame, text=title, bg='#1a1a1a', fg='#ffffff', 
                font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=5)
        
        content_frame = tk.Frame(frame, bg='#1a1a1a')
        content_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        return content_frame
    
    def create_slider_with_entry(self, parent, variable, min_val, max_val, is_float=False):
        frame = tk.Frame(parent, bg='#1a1a1a')
        frame.pack(fill='x', pady=2)
        
        slider = tk.Scale(frame, from_=min_val, to=max_val, variable=variable,
                         orient='horizontal', bg='#1a1a1a', fg='#ffffff',
                         highlightbackground='#1a1a1a', troughcolor='#404040')
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
        self.recoil_curve.set(preset["curve"])
        self.mode_label.config(text=f"Mode: {mode}")
    
    def toggle_recoil(self):
        if not self.running:
            self.start_recoil()
        else:
            self.stop_recoil()
    
    def reset_counter(self):
        self.shot_count = 0
        self.shots_label.config(text="Shots Fired: 0")
    
    def start_recoil(self):
        if not self.recoil_enabled.get() and not self.rapid_fire_enabled.get():
            messagebox.showwarning("Warning", "Please enable at least one feature!")
            return
        
        self.running = True
        self.status_label.config(text="Status: ENABLED", fg='#44ff44')
        
        if self.recoil_enabled.get():
            self.recoil_thread = threading.Thread(target=self.advanced_recoil_loop, daemon=True)
            self.recoil_thread.start()
        
        if self.rapid_fire_enabled.get():
            self.rapid_fire_thread = threading.Thread(target=self.advanced_rapid_fire_loop, daemon=True)
            self.rapid_fire_thread.start()
    
    def stop_recoil(self):
        self.running = False
        self.status_label.config(text="Status: DISABLED", fg='#ff4444')
    
    def calculate_recoil_pattern(self, shot_number):
        """Calculate recoil compensation based on pattern and shot number"""
        pattern = self.recoil_pattern.get()
        curve = self.recoil_curve.get()
        
        if pattern == "LINEAR":
            return shot_number
        elif pattern == "EXPONENTIAL":
            return math.pow(shot_number, curve)
        elif pattern == "LOGARITHMIC":
            return math.log(shot_number + 1) * curve
        else:  # CUSTOM
            return shot_number * curve
    
    def advanced_recoil_loop(self):
        while self.running:
            try:
                if kb.is_pressed('mouse1'):  # Left mouse button
                    if not self.require_ads.get() or kb.is_pressed('mouse2'):  # Right mouse for ADS
                        # Enhanced recoil compensation
                        vertical = self.vertical_strength.get()
                        horizontal = self.horizontal_strength.get()
                        
                        if self.smart_recoil.get():
                            # Apply pattern-based compensation
                            pattern_multiplier = self.calculate_recoil_pattern(self.shot_count + 1)
                            vertical_comp = int(vertical * pattern_multiplier / 10)
                            horizontal_comp = int(horizontal * pattern_multiplier / 10)
                        else:
                            vertical_comp = vertical
                            horizontal_comp = horizontal
                        
                        if vertical_comp > 0:
                            ms.move(0, vertical_comp, absolute=False)
                        if horizontal_comp > 0:
                            ms.move(horizontal_comp, 0, absolute=False)
                        
                        self.shot_count += 1
                        self.shots_label.config(text=f"Shots Fired: {self.shot_count}")
                        
                        time.sleep(self.recoil_delay.get())
                    else:
                        # Reset shot count when not firing
                        self.shot_count = 0
                else:
                    # Reset shot count when not firing
                    self.shot_count = 0
                
                time.sleep(0.001)  # Small delay to prevent high CPU usage
            except Exception as e:
                print(f"Advanced recoil error: {e}")
                break
    
    def advanced_rapid_fire_loop(self):
        while self.running:
            try:
                if kb.is_pressed('mouse1'):
                    if not self.require_ads.get() or kb.is_pressed('mouse2'):
                        if self.burst_mode.get():
                            # Burst fire mode
                            burst_count = self.burst_count.get()
                            for _ in range(burst_count):
                                if not self.running:
                                    break
                                ms.click()
                                time.sleep(self.rapid_fire_speed.get() / 1000.0)
                        else:
                            # Continuous rapid fire
                            speed = self.rapid_fire_speed.get() / 1000.0
                            time.sleep(speed)
                            ms.click()
                
                time.sleep(0.001)
            except Exception as e:
                print(f"Advanced rapid fire error: {e}")
                break
    
    def save_config(self):
        config = {
            "recoil_enabled": self.recoil_enabled.get(),
            "rapid_fire_enabled": self.rapid_fire_enabled.get(),
            "require_ads": self.require_ads.get(),
            "smart_recoil": self.smart_recoil.get(),
            "burst_mode": self.burst_mode.get(),
            "vertical_strength": self.vertical_strength.get(),
            "horizontal_strength": self.horizontal_strength.get(),
            "recoil_delay": self.recoil_delay.get(),
            "recoil_pattern": self.recoil_pattern.get(),
            "recoil_curve": self.recoil_curve.get(),
            "rapid_fire_speed": self.rapid_fire_speed.get(),
            "burst_count": self.burst_count.get(),
            "current_mode": self.current_mode.get()
        }
        
        try:
            with open(f"advanced_config_{self.config_slot.get()}.json", "w") as f:
                json.dump(config, f)
            messagebox.showinfo("Success", f"Advanced configuration saved to slot {self.config_slot.get()}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save config: {e}")
    
    def load_config(self):
        try:
            with open(f"advanced_config_{self.config_slot.get()}.json", "r") as f:
                config = json.load(f)
            
            self.recoil_enabled.set(config.get("recoil_enabled", False))
            self.rapid_fire_enabled.set(config.get("rapid_fire_enabled", False))
            self.require_ads.set(config.get("require_ads", True))
            self.smart_recoil.set(config.get("smart_recoil", True))
            self.burst_mode.set(config.get("burst_mode", False))
            self.vertical_strength.set(config.get("vertical_strength", 12))
            self.horizontal_strength.set(config.get("horizontal_strength", 3))
            self.recoil_delay.set(config.get("recoil_delay", 0.008))
            self.recoil_pattern.set(config.get("recoil_pattern", "LINEAR"))
            self.recoil_curve.set(config.get("recoil_curve", 1.5))
            self.rapid_fire_speed.set(config.get("rapid_fire_speed", 30))
            self.burst_count.set(config.get("burst_count", 3))
            self.current_mode.set(config.get("current_mode", "EXTREME"))
            
            self.mode_label.config(text=f"Mode: {self.current_mode.get()}")
            messagebox.showinfo("Success", f"Advanced configuration loaded from slot {self.config_slot.get()}")
        except FileNotFoundError:
            messagebox.showwarning("Warning", f"No advanced configuration found in slot {self.config_slot.get()}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load config: {e}")
    
    def on_closing(self):
        self.stop_recoil()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedNoRecoilApp(root)
    root.mainloop() 