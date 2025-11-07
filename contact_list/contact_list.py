"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QLabel,
    QVBoxLayout,
    QWidget,
    QTableWidgetItem,
)


class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.__initialize_widgets()
        self.__wire_events()  # connect buttons to our methods

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.

        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)

        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def __wire_events(self):
        """Connect button clicks to their handlers."""
        self.add_button.clicked.connect(self.add_contact)
        self.remove_button.clicked.connect(self.remove_contact)

    def add_contact(self):
        """Add a contact to the table if both fields are filled."""
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not phone:
            self.status_label.setText("Please enter both name and phone.")
            return

        # Add a new row
        row = self.contact_table.rowCount()
        self.contact_table.insertRow(row)
        self.contact_table.setItem(row, 0, QTableWidgetItem(name))
        self.contact_table.setItem(row, 1, QTableWidgetItem(phone))

        # Clear inputs and update status
        self.contact_name_input.clear()
        self.phone_input.clear()
        self.status_label.setText(f"Added: {name}")

    def remove_contact(self):
        """Remove the selected contact from the table after confirmation."""
        row = self.contact_table.currentRow()

        if row == -1:
            self.status_label.setText("Select a contact row to remove.")
            return

        name_item = self.contact_table.item(row, 0)
        name = name_item.text() if name_item else "Contact"

        # Ask for confirmation using QMessageBox
        reply = QMessageBox.question(
            self,
            "Remove Contact",
            f"Are you sure you want to remove {name}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.contact_table.removeRow(row)
            self.status_label.setText(f"Removed: {name}")
        else:
            self.status_label.setText("Removal canceled.")
