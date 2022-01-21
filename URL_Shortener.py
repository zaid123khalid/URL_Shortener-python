from tkinter import *
from tkinter import ttk
import pyshorteners
import pyperclip


def short():
    URL = e1.get()
    url_shortener = pyshorteners.Shortener()
    Short_url = url_shortener.tinyurl.short(URL)
    short_url.set(Short_url)


def copy_url():
    pyperclip.copy(short_url.get())


win = Tk()
win.resizable(False, False)

main_url = StringVar()
short_url = StringVar()

st = ttk.Style()
st.configure('W.TButton', background='#345', foreground='black', font=('Arial', 14))

l1 = ttk.Label(win, text="Enter URL to short", font=("poppins", 20))
l1.pack(pady=5)

e1 = ttk.Entry(win, textvariable=main_url, width=75)
e1.pack(pady=5)

b1 = ttk.Button(win, text="Generate short URL", style='W.TButton', command=short)
b1.pack(pady=5)

l2 = ttk.Label(win, text="Short URL", font=("poppins", 20))
l2.pack(pady=5)

e2 = ttk.Entry(win, textvariable=short_url, width=50)
e2.pack(pady=5)

b2 = ttk.Button(win, text="Copy Short URL", style='W.TButton', command=copy_url)
b2.pack(pady=5)

win.mainloop()
