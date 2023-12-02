import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
import keyboard
import pyautogui

class MacroThread(QThread):
    tamamlandi = pyqtSignal()

    def run(self):
        while not keyboard.is_pressed('alt') and not keyboard.is_pressed('left'):
            self.aksiyonu_gercekle()
        self.tamamlandi.emit()

    def aksiyonu_gercekle(self):
        keyboard.press_and_release('2')
        self.msleep(300)
        pyautogui.click(button='left')
        self.msleep(300)
        keyboard.press_and_release('1')
        self.msleep(300)

class MacroUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        self.setGeometry(300, 300, 400, 220)
        self.setWindowTitle('Macro Uygulaması')
        self.setStyleSheet('background-color: lightgray;')

        self.etiket = QLabel("Sol Alt Tuşuna Basılı Tutun", self)
        font = QFont("Arial", 12)
        self.etiket.setFont(font)

        self.baslat_butonu = QPushButton("Başlat", self)
        self.baslat_butonu.clicked.connect(self.macro_baslat)
        self.baslat_butonu.setStyleSheet('background-color: green; color: white; font-size: 25px; font-weight: bold;')

        self.durdur_butonu = QPushButton("Durdur", self)
        self.durdur_butonu.clicked.connect(self.macro_durdur)
        self.durdur_butonu.setStyleSheet('background-color: red; color: white; font-size: 30px; font-weight: bold;')
        self.durdur_butonu.setEnabled(False)

        dikey_kutu = QVBoxLayout()
        dikey_kutu.addWidget(self.etiket)
        dikey_kutu.addWidget(self.baslat_butonu)
        dikey_kutu.addWidget(self.durdur_butonu)

        self.setLayout(dikey_kutu)

        self.calisiyor = False
        self.macro_thread = MacroThread()
        self.macro_thread.tamamlandi.connect(self.macro_durdur)

    def macro_baslat(self):
        self.calisiyor = True
        self.baslat_butonu.setEnabled(False)
        self.durdur_butonu.setEnabled(True)

        self.macro_thread.start()

    def macro_durdur(self):
        self.calisiyor = False
        self.baslat_butonu.setEnabled(True)
        self.durdur_butonu.setEnabled(False)
        self.macro_thread.quit()
        self.macro_thread.wait()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacroUygulamasi()
    ex.show()
    sys.exit(app.exec_())
