import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QSpinBox,
    QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt5.QtCore import Qt

class POSApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS App - Avryan Adjie Pratama - F1D021099")
        self.resize(500, 400)

        self.products = {
            "Pensil": 2000,
            "Buku": 5000,
            "Penghapus": 1500,
            "Pulpen": 3000
        }

        self.init_ui()
        self.cart = []
        self.total_price = 0

    def init_ui(self):
        # Label Nama dan NIM
        self.name_label = QLabel("Nama: Avryan Adjie Pratama | NIM: F1D021099")
        self.name_label.setAlignment(Qt.AlignCenter)

        # Produk
        self.product_label = QLabel("Pilih Produk:")
        self.product_combo = QComboBox()
        self.product_combo.addItems(self.products.keys())

        # Jumlah
        self.qty_label = QLabel("Jumlah:")
        self.qty_spin = QSpinBox()
        self.qty_spin.setRange(1, 100)

        # Diskon
        self.discount_label = QLabel("Diskon:")
        self.discount_combo = QComboBox()
        self.discount_combo.addItems(["0%", "10%", "20%", "30%"])

        # Tombol
        self.add_button = QPushButton("Add to Cart")
        self.clear_button = QPushButton("Clear")

        self.add_button.clicked.connect(self.add_to_cart)
        self.clear_button.clicked.connect(self.clear_form)

        # Cart
        self.cart_display = QTextEdit()
        self.cart_display.setReadOnly(True)

        # Total
        self.total_label = QLabel("Total: Rp 0")

        # Layout
        form_layout = QGridLayout()
        form_layout.addWidget(self.product_label, 0, 0)
        form_layout.addWidget(self.product_combo, 0, 1)
        form_layout.addWidget(self.qty_label, 1, 0)
        form_layout.addWidget(self.qty_spin, 1, 1)
        form_layout.addWidget(self.discount_label, 2, 0)
        form_layout.addWidget(self.discount_combo, 2, 1)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.name_label)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.cart_display)
        main_layout.addWidget(self.total_label)

        self.setLayout(main_layout)

    def add_to_cart(self):
        product = self.product_combo.currentText()
        price = self.products[product]
        qty = self.qty_spin.value()
        discount_text = self.discount_combo.currentText()
        discount_percent = int(discount_text.replace("%", ""))

        subtotal = price * qty
        discount_amount = subtotal * discount_percent / 100
        total = subtotal - discount_amount

        self.total_price += total
        cart_line = f"{product} x{qty} - Diskon {discount_percent}% = Rp {int(total)}"
        self.cart.append(cart_line)

        self.cart_display.setText("\n".join(self.cart))
        self.total_label.setText(f"Total: Rp {int(self.total_price)}")

    def clear_form(self):
        self.product_combo.setCurrentIndex(0)
        self.qty_spin.setValue(1)
        self.discount_combo.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())
