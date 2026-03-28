# Copyright (C) 2026 Abdullah Yiğit KARAKUŞ
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def calculate(raw_number1, raw_number2, operator):
    try:
        number1 = float(raw_number1)
        number2 = float(raw_number2)
        if operator == "+" :
           result = number1 + number2
        elif operator == "-" :
            result = number1 - number2
        elif operator == "x" :
            result = number1 * number2
        elif operator == "/" :
            if number2 == 0:
                lbl_result.configure(text="Bölme işleminde bölen 0 olamaz.")
            else:
                result = number1 / number2
        lbl_result.configure(text=f"{number1} {operator} {number2} = {result}")
    except ValueError:
        lbl_result.configure(text="Lütfen sadece sayı girin.")
    

def logout():
    root.destroy()

root = ctk.CTk()
root.title("YinegelOS Basic Calc")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
frm1 = ctk.CTkFrame(root)
frm1.pack(pady=10, padx=20)
ent1 = ctk.CTkEntry(frm1, font=("Arial", 16))
ent1.pack(pady=10, padx=20)
ent2 = ctk.CTkEntry(frm1, font=("Arial", 16))
ent2.pack(pady=10, padx=20)
frm2 = ctk.CTkFrame(root)
frm2.pack(pady=10, padx=20)
btn_plus = ctk.CTkButton(frm2,  text="Topla",  font=("Arial", 16), command=lambda: calculate(ent1.get(), ent2.get(), "+"))
btn_plus.pack(pady=10, padx=20, side="left")
btn_minus = ctk.CTkButton(frm2,  text="Çıkar",  font=("Arial", 16), command=lambda: calculate(ent1.get(), ent2.get(), "-"))
btn_minus.pack(pady=10, padx=20, side="left")
btn_impact = ctk.CTkButton(frm2,  text="Çarp",  font=("Arial", 16), command=lambda: calculate(ent1.get(), ent2.get(), "x"))
btn_impact.pack(pady=10, padx=20, side="left")
btn_divide = ctk.CTkButton(frm2,  text="Böl",  font=("Arial", 16), command=lambda: calculate(ent1.get(), ent2.get(), "/"))
btn_divide.pack(pady=10, padx=20, side="left")
lbl_result = ctk.CTkLabel(root, text="", font=("Arial", 16))
lbl_result.pack(pady=10, padx=20)
btn_exit = ctk.CTkButton(root, text="Çıkış yap", command=logout, font=("Arial", 16))
btn_exit.pack(pady=30, padx=40, side="bottom")
root.mainloop()
