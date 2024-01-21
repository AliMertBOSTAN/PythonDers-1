import tkinter as tk
from tkinter import messagebox
import random

class RenkTahminOyunu:
    def __init__(self, master):
        self.master = master
        self.master.title("Renk Tahmin Oyunu")
        self.master.geometry("800x400")

        self.gizli_renkler = self.renk_sec()
        self.tahmin_hakki = 10
        self.tahminler = []

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10, padx=10)

        self.tahmin_canvas = tk.Canvas(self.frame, width=400, height=400)
        self.tahmin_canvas.pack(pady=10, padx=10, side=tk.LEFT)

        self.canvas = tk.Canvas(self.frame, width=400, height=300)
        self.canvas.pack(pady=10, padx=10, side=tk.LEFT)

        self.label = tk.Label(self.frame, text="Renkleri harf harf girin ve tahmin edin:")
        self.label.pack(pady=10, padx=10, side=tk.LEFT)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.pack(pady=10, padx=10, side=tk.LEFT)

        self.tahmin_button = tk.Button(self.frame, text="Tahmin Et", command=self.tahmin_et)
        self.tahmin_button.pack(pady=10, padx=10, side=tk.LEFT)

        self.tahmin_hakki_label = tk.Label(self.frame, text=f"Kalan Tahmin Hakkı: {self.tahmin_hakki}")
        self.tahmin_hakki_label.pack(pady=10, padx=10, side=tk.LEFT)

        self.guide_label = tk.Label(self.frame, text=self.renk_guide(), font=("Arial", 12, "bold"))
        self.guide_label.pack(pady=10, padx=10, side=tk.LEFT)

        self.olustur_daireler()

    def olustur_daireler(self):
        renkler = {"k": "black", "y": "yellow", "m": "magenta", "s": "green", "o": "orange", "t": "brown"}

        for i in range(10):
            x_start_tahmin = 20
            y_start_tahmin = 20 + (i * 40)

            for j in range(4):
                self.tahmin_canvas.create_oval(x_start_tahmin, y_start_tahmin, x_start_tahmin + 30, y_start_tahmin + 30, outline="black", width=2, fill="gray")
                x_start_tahmin += 40

        for i in range(10):
            x_start = 20
            y_start = 20 + (i * 40)

            for j in range(4):
                self.canvas.create_oval(x_start, y_start, x_start + 30, y_start + 30, outline="black", width=2, fill="gray")
                x_start += 40

    def renk_sec(self):
        renkler = ["k", "y", "m", "s", "o", "t"]
        return random.sample(renkler, 4)

    def tahmin_et(self):
        tahmin = list(self.entry.get().lower())
        if len(tahmin) != len(self.gizli_renkler):
            messagebox.showwarning("Hata", f"Lütfen {len(self.gizli_renkler)} harf girin.")
        else:
            sonuc = self.tahmin_degerlendir(tahmin)
            self.tahminleri_goster(tahmin, sonuc)
            messagebox.showinfo("Sonuç", f"Siyah: {sonuc['siyah']}, Beyaz: {sonuc['beyaz']}")

            if sonuc["siyah"] == len(self.gizli_renkler):
                messagebox.showinfo("Tebrikler", "Doğru tahmin ettiniz!")
                self.master.destroy()
            else:
                self.tahmin_hakki -= 1
                self.tahmin_hakki_label.config(text=f"Kalan Tahmin Hakkı: {self.tahmin_hakki}")
                if self.tahmin_hakki == 0:
                    messagebox.showinfo("Oyun Bitti", f"Üzgünüm, tahmin hakkınız bitti. Doğru cevap: {self.gizli_renkler}")
                    self.master.destroy()

    def tahmin_degerlendir(self, tahmin):
        sonuc = {"siyah": 0, "beyaz": 0}

        for i in range(len(self.gizli_renkler)):
            if tahmin[i] == self.gizli_renkler[i]:
                sonuc["siyah"] += 1
            elif tahmin[i] in self.gizli_renkler:
                sonuc["beyaz"] += 1

        return sonuc

    def tahminleri_goster(self, tahmin, sonuc):
        renkler = {"k": "black", "y": "yellow", "m": "magenta", "s": "green", "o": "orange", "t": "brown"}
        x_start_tahmin = 20
        y_start_tahmin = 20 + (len(self.tahminler) * 40)

        for renk in tahmin:
            self.tahmin_canvas.create_oval(x_start_tahmin, y_start_tahmin, x_start_tahmin + 30, y_start_tahmin + 30, fill=renkler[renk], outline="black", width=2)
            x_start_tahmin += 40

        x_start = 20
        y_start = 20 + (len(self.tahminler) * 40)

        for renk in tahmin:
            self.canvas.create_oval(x_start, y_start, x_start + 30, y_start + 30, fill=renkler[renk], outline="black", width=2)
            x_start += 40

        self.canvas.create_text(x_start + 20, y_start + 20, text=f"{sonuc['siyah']}/{sonuc['beyaz']}", font=("Arial", 10, "bold"))

        self.tahminler.append(tahmin)

    def renk_guide(self):
        guide_text = "Renk Rehberi:\n"
        for renk in self.gizli_renkler:
            guide_text += f"{renk}: "
            if renk == "k":
                guide_text += "Siyah"
            elif renk == "y":
                guide_text += "Sarı"
            elif renk == "m":
                guide_text += "Magenta"
            elif renk == "s":
                guide_text += "Yeşil"
            elif renk == "o":
                guide_text += "Turuncu"
            elif renk == "t":
                guide_text += "Kahverengi"
            guide_text += "\n"
        return guide_text

if __name__ == "__main__":
    root = tk.Tk()
    app = RenkTahminOyunu(root)
    root.mainloop()
