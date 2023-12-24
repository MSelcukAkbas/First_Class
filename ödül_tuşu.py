import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

pencere = tk.Tk() # burda pencere açıyoruz

def fotoğrafkazıma():
    url = "https://i.pinimg.com/originals/e5/27/2c/e5272c6d803c00e3f97db3c5988bc857.jpg" 
    cevap = requests.get(url)
    img = Image.open(BytesIO(cevap.content))  #burası zordu ; fotoğrafı internettten alıp pencere içine yerleştiriyor
    tk_img = ImageTk.PhotoImage(img)

    image_label = tk.Label(pencere, image=tk_img)
    image_label.photo = tk_img
    image_label.pack()


def oneLar():
    tuş1 = tk.Button(pencere, text="tuş1", command=lambda: [tuş1.place_forget(), sevenLer()])
    tuş1.pack()                                 # ana tuş bu
    tuş1.place(x=140, y=140) # place yerleşim yerini temsil eder

    def kötübildiri():
        mesaj = [                                      
            ("NOP!!!!", "BU DEĞİL"),
            ("NOP!!!!", "BURASI DEĞİL"),
            ("NOP!!!!", "SEN BİRAZ ŞANSSIZSIN!!"),
            ("NOP!!!!", "TEKRAR DENE"), ]
        mesajlarr = random.choice(mesaj) # random bir şekilde mesaj veriyoruz. ilk başta farklı fonksiyonlar şeklinde yaptım sonra güncelledim
        messagebox.showinfo(mesajlarr[0], mesajlarr[1])

    def iyibildiri():
        messagebox.showinfo("WOW!!!!", "AFFERİM!!!!")

    def sevenLer():
        tuş2 = tk.Button(pencere, text="tuş2", command=lambda: tuş2.place_forget())
        tuş3 = tk.Button(pencere, text="tuş3", command=lambda: [tuş3.place_forget(), fotoğrafkazıma() ,iyibildiri() ])
        # köşeli parantez ile listeleyerek fonksiyon çağırıyor
        tuş4 = tk.Button(pencere, text="tuş4", command=lambda: tuş4.place_forget())
        tuş5 = tk.Button(pencere, text="tuş5", command=lambda: tuş5.place_forget())
        tuş6 = tk.Button(pencere, text="tuş6", command=lambda: [tuş6.place_forget(), kötübildiri()])
        tuş7 = tk.Button(pencere, text="tuş7", command=lambda: [tuş7.place_forget(), kötübildiri()])
        tuş8 = tk.Button(pencere, text="tuş8", command=lambda: [tuş8.place_forget(), kötübildiri()])
        tuş9 = tk.Button(pencere, text="tuş9", command=lambda: [tuş9.place_forget(), kötübildiri()])
        tuş10 = tk.Button(pencere, text="tuş10", command=lambda: tuş10.place_forget())

        tuş2.pack()
        tuş2.place(x=30, y=30)
        tuş3.pack()
        tuş3.place(x=240, y=30)
        tuş4.pack()
        tuş4.place(x=240, y=240)
        tuş5.pack()
        tuş5.place(x=30, y=240)
        tuş6.pack()                    #bu kısıma bi 15 dk uğtaştım kare olsun diye
        tuş6.place(x=30, y=135)
        tuş7.pack()
        tuş7.place(x=135, y=30)
        tuş8.pack()
        tuş8.place(x=240, y=135)
        tuş9.pack()
        tuş9.place(x=135, y=240)
        tuş10.pack()
        tuş10.place(x=135, y=135)


oneLar() # ana program burda başlıyor
pencere.title("pencere")
pencere.geometry("300x300")
pencere.config(bg="gray")     # burası renk için , geometry zaten geometri , mainloop pencereyi kapatana kadar döngüye sokar
pencere.mainloop()
