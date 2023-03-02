

import tkinter as tk
from tkinter import ttk

from login_db import  *

class app(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x400")
        self.title("USER LOGİN")

        self.etiket1 = tk.Label(text="user name: \t",bg="grey")
        self.etiket1.grid(row=2,column=2)

        self.username = tk.Entry()
        self.username.grid(row=2,column=3)

        self.etiket2 = tk.Label(text="password: \t",bg="grey")
        self.etiket2.grid(row=3,column=2)

        self.password = tk.Entry(show="*")
        self.password.grid(row=3,column=3)

        # button
        self.login = tk.Button(text="LOGİN", command=self.kontrol)
        self.login.grid(row=4,column=3)

        # uyarı
   
        self.etiket3 = tk.Label(text="",fg="red")
        self.etiket3.grid(row=5,column=4)


    def new_window(self):
            yeni_pencere = tk.Toplevel(self)
            yeni_pencere.geometry("300x300")
            # Yeni pencerede bir etiket oluşturuluyor
            label = tk.Label(yeni_pencere, text=f" merhaba {self.username.get()}")
            label.pack(pady=20)

    def kontrol(self):
            name = self.username.get()
            password = self.password.get()
            durum = kontrol_et(name, password)

            if durum:
                self.new_window()
            else:
                pencere.etiket3["text"] = "sisteme kayıtlı böyle bir kullanıcı yok"


pencere = app()
pencere.mainloop()

