#!/usr/bin/env python3                    # Shebang für Linux/Mac (optional)
import tkinter as tk                      # Import mit Alias "tk" (Standard)

root = tk.Tk()                            # 1️⃣ Hauptfenster erstellen
root.title("Mein Test")                   # 2️⃣ Titel setzen  
root.geometry("400x300")                  # 3️⃣ Größe festlegen (400x300 Pixel)

label = tk.Label(root, text="Hallo tkinter!", font=("Arial", 16))
                                            # 4️⃣ Label-Widget: Text + große Schrift
label.pack(pady=50)                       # 5️⃣ Widget im Fenster platzieren (+ Abstand)

root.mainloop()     
