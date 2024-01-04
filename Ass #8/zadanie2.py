import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
# dodać tytuł, rozmiar
okno.title("PDF Reader")

# dodać widget Text i umieściś z jakimś marginesem

text = tk.Text(okno, wrap="word", width=50, height=50)
text.pack(padx=5, pady=5)

def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   okno.destroy()

menu_bar = tk.Menu(okno)
okno.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

okno.mainloop()