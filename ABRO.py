import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QListWidget, QPushButton, QFileDialog

class DirectoryExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Layout
        layout = QVBoxLayout()
        
        # Dropdown for directories
        self.dirLabel = QLabel('Select Directory:')
        layout.addWidget(self.dirLabel)
        
        self.dirComboBox = QComboBox()
        self.dirComboBox.addItem("Select a directory...")
        layout.addWidget(self.dirComboBox)
        
        # Button to open directory dialog
        self.dirButton = QPushButton('Browse...')
        self.dirButton.clicked.connect(self.browse_directory)
        layout.addWidget(self.dirButton)
        
        # Sidebar list of subdirectories
        self.subdirList = QListWidget()
        layout.addWidget(self.subdirList)
        
        # Set layout
        self.setLayout(layout)
        self.setWindowTitle('Directory Explorer')
        
    def browse_directory(self):
        # Open directory selection dialog
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        if directory:
            self.dirComboBox.addItem(directory)
            self.dirComboBox.setCurrentText(directory)
            self.list_subdirectories(directory)
    
    def list_subdirectories(self, directory):
        # Clear existing list
        self.subdirList.clear()
        
        # List all subdirectories in the selected directory
        subdirs = []
        for root, dirs, _ in os.walk(directory):
            for dir in dirs:
                subdirs.append(os.path.join(root, dir))
        
        # Populate the subdirectory list in the sidebar
        for subdir in subdirs:
            self.subdirList.addItem(subdir)


# Main function to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    explorer = DirectoryExplorer()
    explorer.show()
    sys.exit(app.exec_())
