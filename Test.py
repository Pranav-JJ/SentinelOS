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

    def open_presentation_link(self):
        webbrowser.open("https://www.canva.com/design/DAFuQi7Jy-M/ocMNFOlBoO7o0HNuEa2FnA/edit")

    def open_github_repo_link(self):
        webbrowser.open("https://github.com/Pranav-JJ/SentinelOS")

    def sidebar_button_event(self, button_text):
        if button_text == "Documentation":
            self.open_documentation_link()
        elif button_text == "Presentation":
            self.open_presentation_link()
        elif button_text == "Github Repo":
            self.open_github_repo_link()
        else:
            print("")

    def __init__(self):
        super().__init__()

        self.title("SentinelOS Security Configuration")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="SentinelOS", font=ctk.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="", image=icon_image)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text = "Documentation", command=self.open_documentation_link)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text = "Github Repo", command=self.open_github_repo_link)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text = "Presentation", command=self.open_presentation_link)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # ctk.deactivate_automatic_dpi_awareness()
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter Custom Command")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, text = "Enter", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("File System Configuration")
        self.tabview.add("Secure Boot Settings")
        self.tabview.add("System Updates")
        self.tabview.add("Network Security/Firewall Config")
        self.tabview.tab("File System Configuration").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Secure Boot Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("System Updates").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Network Security/Firewall Config").grid_columnconfigure(0, weight=1)

        self.file_system_switch = ctk.CTkSwitch(self.tabview.tab("File System Configuration"))
        self.file_system_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.file_system_action_label = ctk.CTkLabel(self.tabview.tab("File System Configuration"), text="File System Action:", anchor="w")
        self.file_system_action_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.file_system_action_var = ctk.StringVar(value="Add Files to Database")
        self.file_system_action_optionmenu = ctk.CTkOptionMenu(self.tabview.tab("File System Configuration"), values=["Add Files to Database", "Run File Integrity", "Run Directory Integrity"],
                                                                         command=self.update_file_system_action,
                                                                         variable=self.file_system_action_var)
        self.file_system_action_optionmenu.grid(row=3, column=0, padx=20, pady=(0, 20))
        self.file_system_button = ctk.CTkButton(self.tabview.tab("File System Configuration"), text="Configure File System", command=self.configure_file_system)
        self.file_system_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.secure_boot_switch = ctk.CTkSwitch(self.tabview.tab("Secure Boot Settings"))
        self.secure_boot_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.secure_boot_button = ctk.CTkButton(self.tabview.tab("Secure Boot Settings"), text="Apply Secure Boot Settings", command=self.apply_secure_boot)
        self.secure_boot_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.system_updates_switch = ctk.CTkSwitch(self.tabview.tab("System Updates"))
        self.system_updates_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.system_updates_button = ctk.CTkButton(self.tabview.tab("System Updates"), text="Run System Updates", command=self.run_system_update)
        self.system_updates_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.network_security_switch = ctk.CTkSwitch(self.tabview.tab("Network Security/Firewall Config"))
        self.network_security_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.network_security_button = ctk.CTkButton(self.tabview.tab("Network Security/Firewall Config"), text="Configure Network Security/Firewall", command=self.configure_network_security)
        self.network_security_button.grid(row=1, column=0, padx=20, pady=(10, 20))

    def configure_file_system(self):
        selected_action = self.file_system_action_var.get()
        if self.file_system_switch.get() == "on":
            if selected_action == "Add Files to Database":
                # subprocess.run(["./add_files_to_database.sh"])
                subprocess.run(["Code/pythonintrotut.py"])
            elif selected_action == "Run File Integrity":
                subprocess.run(["./run_file_integrity.sh"])
            elif selected_action == "Run Directory Integrity":
                subprocess.run(["./run_directory_integrity.sh"])

    def apply_secure_boot(self):
        if self.secure_boot_switch.get() == "on":
            subprocess.run(["./apply_secure_boot.sh"])

    def run_system_update(self):
        if self.system_updates_switch.get() == "on":
            subprocess.run(["./run_system_update.sh"])

    def configure_network_security(self):
        if self.network_security_switch.get() == "on":
            subprocess.run(["./configure_network_security.sh"])

    def update_file_system_action(self, selected_action):
        # yet to add certain other actions here (need to try diff options available for integrity checks)
        pass

    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

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
