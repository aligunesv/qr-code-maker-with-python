import sys
import qrcode
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog


class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.url_label = QLabel("URL:")
        self.url_edit = QLineEdit()
        self.generate_button = QPushButton("Generate QR Code")
        self.qr_code_label = QLabel()

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_edit)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.qr_code_label)
        self.setLayout(layout)

        # Connect signals and slots
        self.generate_button.clicked.connect(self.generate_qr_code)

    def generate_qr_code(self):
        # Get URL from text edit
        url = self.url_edit.text()

        # Generate QR code image
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Open file dialog to select save location and file name
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save QR Code Image", "", "PNG Files (*.png)", options=options)
        if file_name:
            # Save QR code image to file
            img.save(file_name)

            # Convert QR code image to QPixmap and set to label
            qr_code_pixmap = QPixmap(file_name)
            self.qr_code_label.setPixmap(qr_code_pixmap)


if __name__ == "__main__":
    # Create application and widget
    app = QApplication(sys.argv)
    widget = QRCodeGenerator()
    widget.show()

    # Run event loop
    sys.exit(app.exec_())


#Hope you like it! You can use it fully free!
#https://github.com/aligunesv
