import tkinter as tk
import random

messages = [
    "Anh nhớ em lắm 💗",
    "Anh yêu em",
    "Đừng buồn nữa nhé",
    "Anh luôn ở đây",
    "Smile đi nào ✨",
]

# ---------- POPUP ----------
def create_window():
    popup = tk.Toplevel(root)
    popup.geometry("340x170")
    popup.overrideredirect(False)
    popup.title("Tràn ngập bộ nhớ")

    # Outer frame (shadow feel)
    frame = tk.Frame(popup, bg="white", padx=3, pady=3)
    frame.pack(expand=True, fill="both")

    # Inner gradient-like color
    inner = tk.Frame(frame, bg="#FFC0CB")
    inner.pack(expand=True, fill="both")

    text = random.choice(messages)

    label = tk.Label(
        inner,
        text=text,
        bg="#FFC0CB",
        fg="black",
        font=("Helvetica", 16, "bold"),
        wraplength=300,
        justify="center"
    )
    label.pack(expand=True)

    # Random screen position
    popup.update_idletasks()
    x = random.randint(0, popup.winfo_screenwidth() - 340)
    y = random.randint(0, popup.winfo_screenheight() - 170)
    popup.geometry(f"340x170+{x}+{y}")


# ---------- SPAWN ----------
def create_windows_with_delay(count=60, delay=120):
    if count > 0:
        create_window()
        root.after(delay, create_windows_with_delay, count-1, delay)


def on_click():
    create_windows_with_delay()


# ---------- MAIN ----------
root = tk.Tk()
root.geometry("420x220")
root.title("Anh muốn nói là...")
root.configure(bg="#FFC0CB")

# Center window
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 210
y = (root.winfo_screenheight() // 2) - 110
root.geometry(f"+{x}+{y}")

# Button
btn = tk.Button(
    root,
    text="Muốn nói là...",
    command=on_click,
    font=("Helvetica", 22, "bold"),
    bg="white",
    fg="black",
    activebackground="#ff9bb3",
    relief="flat",
    padx=20,
    pady=10
)
btn.pack(expand=True)

root.mainloop()
