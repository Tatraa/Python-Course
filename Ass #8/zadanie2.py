import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
# dodać tytuł, rozmiar

# dodać widget Text i umieściś z jakimś marginesem

def clear_text():
   pass

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   pass

# utworzyć widget Menu i jego strukturę jak na rysunku
# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app

okno.mainloop()