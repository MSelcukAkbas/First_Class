import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
import psutil
import GPUtil
import platform

class UpdateThread(QThread):
    updated = pyqtSignal(dict)

    def run(self):
        while True:
            ram_info = psutil.virtual_memory()
            cpu_info = {
                "processor_name": platform.processor(),
                "cores": psutil.cpu_count(logical=False),
                "total_cores": psutil.cpu_count(logical=True),
                "cpu_freq": psutil.cpu_freq().current,
                "cpu_percent": psutil.cpu_percent(),
            }
            try:
                gpus = GPUtil.getGPUs()
                gpu_info = {
                    "gpu_name": gpus[0].name,
                    "memory_total": gpus[0].memoryTotal,
                    "memory_free": gpus[0].memoryFree,
                    "memory_used": gpus[0].memoryUsed,
                    "temperature": gpus[0].temperature,
                }
            except Exception as e:
                gpu_info = {"error": f"Ekran kartı bilgisi alınamadı: {str(e)}"}

            data = {"ram_info": ram_info, "cpu_info": cpu_info, "gpu_info": gpu_info}
            self.updated.emit(data)
            self.msleep(1000)  # Her 1000 milisaniyede (1 saniye) bir güncelleme yap

class SystemInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistem Bilgisi")
        self.setGeometry(100, 100, 600, 400)

        # Başlık çubuğu fontu ve renk ayarları
        title_font = QFont("Arial", 20, QFont.Bold)
        title_label = QLabel("Sistem Bilgisi")
        title_label.setFont(title_font)

        layout = QVBoxLayout(self)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)  # Başlık çubuğunu merkeze al

        # RAM Bilgisi
        self.ram_label = QLabel()
        self.ram_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.ram_label)

        # CPU Bilgisi
        self.cpu_label = QLabel()
        self.cpu_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.cpu_label)

        # Ekran Kartı Bilgisi
        self.gpu_label = QLabel()
        self.gpu_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.gpu_label)

        # Pencereyi daha güzel göstermek için arka plan rengi ve padding
        self.setStyleSheet("background-color: #abcabc; padding: 13px;")

        self.setLayout(layout)

        # UpdateThread'i başlat
        self.update_thread = UpdateThread()
        self.update_thread.updated.connect(self.update_ui)
        self.update_thread.start()

    def update_ui(self, data):
        ram_text = f"<b>Toplam RAM:</b> {round(data['ram_info'].total / (1024 ** 3), 2)} GB<br>" \
                   f"<b>Kullanılan RAM:</b> {round(data['ram_info'].used / (1024 ** 3), 2)} GB<br>" \
                   f"<b>Boş RAM:</b> {round(data['ram_info'].available / (1024 ** 3), 2)} GB"
        self.ram_label.setText(ram_text)

        cpu_info = f"<b>İşlemci Adı:</b> {data['cpu_info']['processor_name']}<br>" \
                   f"<b>Çekirdek Sayısı:</b> {data['cpu_info']['cores']}<br>" \
                   f"<b>Toplam Çekirdek Sayısı:</b> {data['cpu_info']['total_cores']}<br>" \
                   f"<b>CPU Frekansı:</b> {data['cpu_info']['cpu_freq']} MHz<br>" \
                   f"<b>CPU Kullanımı:</b> {data['cpu_info']['cpu_percent']}%"
        self.cpu_label.setText(cpu_info)

        try:
            gpu_text = f"<b>Ekran Kartı:</b> {data['gpu_info']['gpu_name']}<br>" \
                        f"<b>Bellek Toplam:</b> {data['gpu_info']['memory_total']} MB<br>" \
                        f"<b>Bellek Boş:</b> {data['gpu_info']['memory_free']} MB<br>" \
                        f"<b>Bellek Kullanılan:</b> {data['gpu_info']['memory_used']} MB<br>" \
                        f"<b>Sıcaklık:</b> {data['gpu_info']['temperature']} °C"
        except Exception as e:
            gpu_text = f"<b>Hata:</b> {str(e)}"
        self.gpu_label.setText(gpu_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemInfoApp()
    window.show()
    sys.exit(app.exec_())
