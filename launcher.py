import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class NoRecoilLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Strong No Recoil Launcher")
        self.root.geometry("400x300")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a', padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="STRONG NO RECOIL LAUNCHER", 
                             font=('Arial', 16, 'bold'), 
                             fg='#ff4444', bg='#1a1a1a')
        title_label.pack(pady=(0, 30))
        
        # Description
        desc_label = tk.Label(main_frame, text="Choose your no-recoil application:", 
                            font=('Arial', 10), fg='#ffffff', bg='#1a1a1a')
        desc_label.pack(pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#1a1a1a')
        buttons_frame.pack(fill='x', pady=20)
        
        # Basic version button
        basic_btn = tk.Button(buttons_frame, text="BASIC VERSION", 
                            command=self.launch_basic, bg='#404040', fg='#ffffff',
                            relief='flat', padx=30, pady=15, font=('Arial', 12, 'bold'))
        basic_btn.pack(fill='x', pady=(0, 15))
        
        # Advanced version button
        advanced_btn = tk.Button(buttons_frame, text="ADVANCED VERSION", 
                               command=self.launch_advanced, bg='#ff4444', fg='#ffffff',
                               relief='flat', padx=30, pady=15, font=('Arial', 12, 'bold'))
        advanced_btn.pack(fill='x', pady=(0, 15))
        
        # Install dependencies button
        install_btn = tk.Button(buttons_frame, text="INSTALL DEPENDENCIES", 
                              command=self.install_dependencies, bg='#2a2a2a', fg='#ffffff',
                              relief='flat', padx=20, pady=10, font=('Arial', 10))
        install_btn.pack(fill='x', pady=(0, 15))
        
        # Exit button
        exit_btn = tk.Button(buttons_frame, text="EXIT", 
                           command=self.root.quit, bg='#2a2a2a', fg='#ffffff',
                           relief='flat', padx=20, pady=10, font=('Arial', 10))
        exit_btn.pack(fill='x')
        
        # Info text
        info_text = """
BASIC VERSION:
• Simple recoil control
• Basic rapid fire
• Easy to use interface

ADVANCED VERSION:
• Smart recoil patterns
• Burst fire mode
• Shot counter
• Advanced customization
        """
        
        info_label = tk.Label(main_frame, text=info_text, 
                            font=('Arial', 8), fg='#cccccc', bg='#1a1a1a',
                            justify='left')
        info_label.pack(pady=(20, 0))
        
    def launch_basic(self):
        try:
            if not os.path.exists('no_recoil_app.py'):
                messagebox.showerror("Error", "Basic version not found!")
                return
            
            subprocess.Popen([sys.executable, 'no_recoil_app.py'])
            self.root.withdraw()  # Hide launcher window
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch basic version: {e}")
    
    def launch_advanced(self):
        try:
            if not os.path.exists('advanced_no_recoil.py'):
                messagebox.showerror("Error", "Advanced version not found!")
                return
            
            subprocess.Popen([sys.executable, 'advanced_no_recoil.py'])
            self.root.withdraw()  # Hide launcher window
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch advanced version: {e}")
    
    def install_dependencies(self):
        try:
            result = messagebox.askyesno("Install Dependencies", 
                                       "This will install required Python packages.\n\n"
                                       "Do you want to continue?")
            if result:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
                messagebox.showinfo("Success", "Dependencies installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install dependencies: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoRecoilLauncher(root)
    root.mainloop() 