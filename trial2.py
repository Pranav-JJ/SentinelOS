import tkinter
import customtkinter
import subprocess

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

       # configured window
        self.title("CustomTkinter Security Configuration")
        self.geometry(f"{1100}x{580}")

        # configured grid layout (a 4x4 layout)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # created sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # created main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # created textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # created tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("File System Configuration")
        self.tabview.add("Secure Boot Settings")
        self.tabview.add("System Updates")
        self.tabview.add("Network Security/Firewall Config")
        self.tabview.tab("File System Configuration").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Secure Boot Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("System Updates").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Network Security/Firewall Config").grid_columnconfigure(0, weight=1)

        self.file_system_switch = customtkinter.CTkSwitch(self.tabview.tab("File System Configuration"))
        self.file_system_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.file_system_button = customtkinter.CTkButton(self.tabview.tab("File System Configuration"), text="Configure File System", command=self.configure_file_system)
        self.file_system_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.secure_boot_switch = customtkinter.CTkSwitch(self.tabview.tab("Secure Boot Settings"))
        self.secure_boot_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.secure_boot_button = customtkinter.CTkButton(self.tabview.tab("Secure Boot Settings"), text="Apply Secure Boot Settings", command=self.apply_secure_boot)
        self.secure_boot_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.system_updates_switch = customtkinter.CTkSwitch(self.tabview.tab("System Updates"))
        self.system_updates_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.system_updates_button = customtkinter.CTkButton(self.tabview.tab("System Updates"), text="Run System Updates", command=self.run_system_update)
        self.system_updates_button.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.network_security_switch = customtkinter.CTkSwitch(self.tabview.tab("Network Security/Firewall Config"))
        self.network_security_switch.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.network_security_button = customtkinter.CTkButton(self.tabview.tab("Network Security/Firewall Config"), text="Configure Network Security/Firewall", command=self.configure_network_security)
        self.network_security_button.grid(row=1, column=0, padx=20, pady=(10, 20))


    # Defined functions to execute shell scripts when switches are toggled
    def configure_file_system(self):
        if self.file_system_switch.get() == "on":
            # subprocess.run(["./configure_file_system.sh"])
            subprocess.run(["./pythonintrotut.py"])

    def apply_secure_boot(self):
        if self.secure_boot_switch.get() == "on":
            # subprocess.run(["./apply_secure_boot.sh"])
            subprocess.run(["./pythonintrotut.py"])

    def run_system_update(self):
        if self.system_updates_switch.get() == "on":
            # subprocess.run(["./run_system_update.sh"])
            subprocess.run(["./pythonintrotut.py"])

    def configure_network_security(self):
        if self.network_security_switch.get() == "on":
            # subprocess.run(["./configure_network_security.sh"])
            subprocess.run(["./pythonintrotut.py"])

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()
