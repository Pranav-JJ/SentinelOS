import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import subprocess
import webbrowser
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./yellow.json")

icon_image = ctk.CTkImage(
    light_image=Image.open("./sentinelOS1.png"),
    dark_image=Image.open("./sentinelOS1.png"),
    size=(250, 50)
)

class App(ctk.CTk):
    def open_documentation_link(self):
        webbrowser.open("https://customtkinter.tomschimansky.com/documentation/")

    def open_github_repo_link(self):
        webbrowser.open("https://github.com/Pranav-JJ/SentinelOS")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def create_home_screen(self):
        # Clear the existing widgets in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        menu_options = ["System Updates", "Secure Boot Settings", "Network Configuration", "Firewall Configuration", "File System Configuration"]

        for i, option in enumerate(menu_options):
            button = ctk.CTkButton(self.sidebar_frame, text=option, command=lambda opt=option: self.create_config_page(opt))
            button.grid(row=i + 1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event
        )
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

    def back_to_home_screen(self):
        # Create the home screen when the image is clicked
        self.create_home_screen()

        # Clear the widgets in the main frame (right side)
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Optionally, you can re-add any widgets that should be present on the home screen
    
    def sidebar_button_event(self, button_text):
        if button_text == "Documentation":
            self.open_documentation_link()
        elif button_text == "Github Repo":
            self.open_github_repo_link()
        else:
            print(f"Selected: {button_text}")

    def create_config_page(self, config_name):
        # Clear the existing widgets in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a new frame for the selected configuration
        config_frame = ctk.CTkFrame(self.main_frame)
        config_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Create switches and input/output areas based on the selected configuration
        if config_name == "System Updates":
            self.create_system_update_config(config_frame)
        elif config_name == "Secure Boot Settings":
            self.create_secure_boot_config(config_frame)
        elif config_name == "Network Configuration":
            self.create_network_config(config_frame)
        elif config_name == "Firewall Configuration":
            self.create_firewall_config(config_frame)
        elif config_name == "File System Configuration":
            self.create_file_system_config(config_frame)

    def create_system_update_config(self, config_frame):
        system_update_switch = ctk.CTkSwitch(config_frame, text="Auto System Updates On")
        system_update_switch.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add other UI elements for system updates configuration here
        update_button = ctk.CTkButton(config_frame, text="Check for Updates", command=self.check_for_updates)
        update_button.grid(row=1, column=0, padx=20, pady=10)

        update_status_label = ctk.CTkLabel(config_frame, text="Update Status:")
        update_status_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.update_status_textbox = ctk.CTkTextbox(config_frame, width=40, height=10, state="disabled")
        self.update_status_textbox.grid(row=3, column=0, padx=20, pady=10)

        refresh_button = ctk.CTkButton(config_frame, text="Refresh Status", command=self.refresh_update_status)
        refresh_button.grid(row=4, column=0, padx=20, pady=10)

        custom_command_label = ctk.CTkLabel(config_frame, text="Enter Custom Command:")
        custom_command_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        self.custom_command_entry = ctk.CTkEntry(config_frame, width=30)
        self.custom_command_entry.grid(row=6, column=0, padx=20, pady=10)

        execute_command_button = ctk.CTkButton(config_frame, text="Execute Command", command=self.execute_custom_command)
        execute_command_button.grid(row=7, column=0, padx=20, pady=10)

        output_label = ctk.CTkLabel(config_frame, text="Command Output:")
        output_label.grid(row=8, column=0, padx=20, pady=10, sticky="w")

        self.command_output_textbox = ctk.CTkTextbox(config_frame, width=40, height=10, state="disabled")
        self.command_output_textbox.grid(row=9, column=0, padx=20, pady=10)

    def execute_custom_command(self):
        # Simulate executing a custom command and displaying the output
        command = self.custom_command_entry.get()
        # You can replace this with actual command execution logic
        command_output = f"Command executed: {command}\nCommand output goes here."
        # Update the command output textbox
        self.command_output_textbox.config(state="normal")
        self.command_output_textbox.delete("1.0", "end")
        self.command_output_textbox.insert("1.0", command_output)
        self.command_output_textbox.config(state="disabled")

    def refresh_update_status(self):
        # Simulate checking for system updates and update status
        update_status = "No updates available."
        # Update the update status textbox
        self.update_status_textbox.config(state="normal")
        self.update_status_textbox.delete("1.0", "end")
        self.update_status_textbox.insert("1.0", update_status)
        self.update_status_textbox.config(state="disabled")

    def check_for_updates(self):
        # Simulate checking for system updates
        update_status = "No updates available."
        # Update the update status textbox
        self.update_status_textbox.config(state="normal")
        self.update_status_textbox.delete("1.0", "end")
        self.update_status_textbox.insert("1.0", update_status)
        self.update_status_textbox.config(state="disabled")


        # Add other UI elements for system updates configuration here

    def create_secure_boot_config(self, config_frame):
        secure_boot_switch = ctk.CTkSwitch(config_frame, text="Secure Boot Settings")
        secure_boot_switch.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add other UI elements for secure boot configuration here

    def create_network_config(self, config_frame):
        network_switch = ctk.CTkSwitch(config_frame, text="Network Configuration")
        network_switch.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add other UI elements for network configuration here

    def create_firewall_config(self, config_frame):
        firewall_switch = ctk.CTkSwitch(config_frame, text="Firewall Configuration")
        firewall_switch.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add other UI elements for firewall configuration here

    def create_file_system_config(self, config_frame):
        file_system_switch = ctk.CTkSwitch(config_frame, text="File System Configuration")
        file_system_switch.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add other UI elements for file system configuration here

    def __init__(self):
        super().__init__()

        self.title("SentinelOS Security Configuration")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="", image=icon_image)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Inside the __init__ method, set up the image click event
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="", image=icon_image)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label.bind("<Button-1>", lambda event: self.back_to_home_screen())

        menu_options = ["System Updates", "Secure Boot Settings", "Network Configuration", "Firewall Configuration", "File System Configuration"]

        for i, option in enumerate(menu_options):
            button = ctk.CTkButton(self.sidebar_frame, text=option, command=lambda opt=option: self.create_config_page(opt))
            button.grid(row=i + 1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event
        )
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

def open_upper_gui():
    app = App()
    app.wm_iconbitmap("sentinelIcon.ico")
    app.mainloop()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./yellow.json")

def login():
    username = "admin"
    password = "admin"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
        root.destroy() 
        open_upper_gui()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")

root = ctk.CTk()
root.wm_iconbitmap("sentinelIcon.ico")
root.geometry("400x400")
root.title("Trial Admin Login GUI")

label = ctk.CTkLabel(root, text="Login UI Page")
label.pack(pady=20)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Ubuntu Security Login UI')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

root.mainloop()

