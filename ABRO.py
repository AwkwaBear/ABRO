import os
import customtkinter as ctk
from tkinter import filedialog

class DirectoryExplorer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.title("Directory Explorer")
        self.geometry("400x300")
        
        # Dropdown for directories (Label and OptionMenu)
        self.dirLabel = ctk.CTkLabel(self, text='Select Directory:')
        self.dirLabel.pack(pady=10)
        
        self.selected_directory = ctk.StringVar(value="Select a directory...")
        self.dirComboBox = ctk.CTkOptionMenu(self, variable=self.selected_directory, values=["Select a directory..."])
        self.dirComboBox.pack(pady=10)
        
        # Button to open directory dialog
        self.dirButton = ctk.CTkButton(self, text='Browse...', command=self.browse_directory)
        self.dirButton.pack(pady=10)
        
        # Sidebar list of subdirectories (CTkListbox does not exist, so using CTkTextbox for displaying subdirectories)
        self.subdirList = ctk.CTkTextbox(self, height=150)
        self.subdirList.pack(pady=10, padx=10, fill='both', expand=True)
    
    def browse_directory(self):
        # Open directory selection dialog
        directory = filedialog.askdirectory(title="Select Directory")
        
        if directory:
            # Add the directory to the OptionMenu and select it
            self.dirComboBox.configure(values=[directory])
            self.selected_directory.set(directory)
            self.list_subdirectories(directory)
    
    def list_subdirectories(self, directory):
        # Clear existing list in the Textbox
        self.subdirList.delete("1.0", "end")
        
        # List all subdirectories in the selected directory
        subdirs = []
        for root, dirs, _ in os.walk(directory):
            for dir in dirs:
                subdirs.append(os.path.join(root, dir))
        
        # Populate the subdirectory list in the Textbox
        for subdir in subdirs:
            self.subdirList.insert("end", subdir + "\n")


# Main function to run the application
if __name__ == '__main__':
    # Set dark mode appearance globally
    ctk.set_appearance_mode("dark")  # Options: "light", "dark", or "system"
    
    # Set default color theme
    ctk.set_default_color_theme("dark-blue")  # Built-in themes: "blue", "green", or "dark-blue"

    
    # Create and run the application
    app = DirectoryExplorer()
    app.mainloop()
