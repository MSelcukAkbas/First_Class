# Geliştirici: M. Selcuk akbas
# Tarih: 24-28... Kasım 2023
# Açıklama:Bu kodu bilgisayarda yapılabilecek küçük optimizasyonları otamatik yapması için geliştirdim
import tkinter as tk
from tkinter import messagebox , ttk
import subprocess
import threading
#alttaki fonksiyon geri bildirim vermeden önce bekleme sağlıyor 
def bekle(milisaniye, fonksiyon, *args, **kwargs):
    pencere.after(milisaniye, lambda: fonksiyon(*args, **kwargs))
    #alttaki fonksiyon bir dizi ipconfig komutu ile ağ ayarlarını optimize ediyor
def internet_ayarı():
    goster_progress_bar()  # Progress bar'ı göster
    commands = [
        ['cmd', '/c', 'ipconfig', '/flushdns'],
        ['cmd', '/c', 'ipconfig', '/release'],
        ['cmd', '/c', 'ipconfig', '/renew']
    ]

    success_message = "İşlem başarıyla tamamlandı."

    progress_bar['maximum'] = len(commands)

    for idx, command in enumerate(commands, start=1):
        result = subprocess.run(command, capture_output=True)
        progress_bar['value'] = idx
        pencere.update_idletasks()

        if result.returncode != 0:
            messagebox.showerror("Hata", f"{command} çalıştırılırken bir hata oluştu.")
            gizle_progress_bar()  # Progress bar'ı gizle
            return

    bekle(700, messagebox.showinfo, "Başarı", success_message)
    gizle_progress_bar()  # Progress bar'ı gizle
#alttaki fonksiyon winget komutu ile güncellemeri kontrol edip yüklüyor
def guncelleme_yukle():
    goster_progress_bar()  # Progress bar'ı göster
    result = subprocess.run(['winget', 'upgrade', '--all'], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()
    updated_packages = [line for line in output_lines if line.startswith("Updated ")]
    num_updated_packages = len(updated_packages)
    
    bekle(700, messagebox.showinfo, "Bilgi", f"{num_updated_packages} paket güncellendi.")
    gizle_progress_bar()  # Progress bar'ı gizle
#alttaki fonksiyon powercfg komutu ile güç planı değiştiriyor
def guc_planı(plan_ayarları):
    command = f'powercfg -setactive {plan_ayarları}'
    try:
        subprocess.run(command, shell=True, check=True)
        bekle(700, messagebox.showinfo, "Bilgi", f"Güç planı değiştirildi: {plan_ayarları}")
    except subprocess.CalledProcessError as e:
        print(f'Hata oluştu: {e}')
        bekle(700, messagebox.showerror, "Hata", "Güç planı değiştirilirken bir hata oluştu.")
#alttaki fonksiyon güç ayarları tuşunu gizliyor
def guc_ayarlarını_goster():
    guc_ayar_cercevesi.grid_forget()
    guc_ayar_cercevesi.grid(row=5, column=0, columnspan=2, pady=(0, 20))
#alttaki fonksiyon uzun süren ayarları(güncelleme ve internet gibi) arka planda yapya yarayan basit bir ayar sağlıyo
def arkaplanda_calistir(fonksiyon, *args):
    threading.Thread(target=fonksiyon, args=args).start()
#alttaki fonksiyon  Progress barı kullanılmadığı zaman gizliyor    
def gizle_progress_bar():
    progress_bar.grid_forget()
#alttaki fonksiyon  Progress barı kullanıldığında gösteriyor
def goster_progress_bar():
    progress_bar.grid(row=3, column=0, columnspan=2, pady=(0, 20))
############################# PENCERE ,  BUTON , VE YERLEŞİM ŞEKLİ  ###########################################
pencere = tk.Tk()
pencere.title("Sorun Çözücü")
pencere.geometry("400x390")
pencere.resizable(False, False)
pencere.configure(bg='#E6E6E6')  
#####################################################################
baslik_etiket = tk.Label(pencere, text="Sorun Çözücü Araçlar", font=("Arial", 18), bg='#E6E6E6')  
baslik_etiket.grid(row=0, column=0, columnspan=2, pady=(10, 20))
#####################################################################
guncelleme_btn = tk.Button(pencere, text="Güncelleme Denetleme", command=lambda: arkaplanda_calistir(guncelleme_yukle), padx=100, pady=5, font=("Arial", 14), bg='#d63604', fg='white')  
guncelleme_btn.grid(row=1, column=0, columnspan=2, pady=(0, 20))
#################################
internet_ayarı_btn = tk.Button(pencere, text="Ping Sorununu Çözme", command=lambda: arkaplanda_calistir(internet_ayarı), padx=106, pady=5, font=("Arial", 14), bg='#d63604', fg='white')  
internet_ayarı_btn.grid(row=2, column=0, columnspan=2, pady=(0, 20))
#####################################################################
guc_ayar_cercevesi = tk.Frame(pencere)
#################################
guc_ayar_dugmesi = tk.Button(pencere, text="Güç Ayarları", command=guc_ayarlarını_goster, padx=100, pady=5, font=("Arial", 14), bg='#d63604', fg='white')
guc_ayar_dugmesi.grid(row=4, column=0, columnspan=2, pady=(0, 20))
#################################
yuksek_guc_tuşu = tk.Button(guc_ayar_cercevesi, text="Yüksek Güç Modunu Aç", command=lambda: guc_planı ("8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"))
yuksek_guc_tuşu.pack(pady=5)
#################################
normal_guc_tuşu = tk.Button(guc_ayar_cercevesi, text="Normal Güç Modunu Aç", command=lambda: guc_planı("381b4222-f694-41f0-9685-ff5bb260df2e"))
normal_guc_tuşu.pack(pady=5)
#################################
guc_ayar_cercevesi.pack_forget()
#####################################################################
progress_bar = ttk.Progressbar(pencere, orient="horizontal", length=200, mode="determinate")
gizle_progress_bar()
#####################################################################
pencere.mainloop()
#########################################################################################################
