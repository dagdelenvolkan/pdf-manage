import tkinter as tk
import gui as gui
import pdf_manage as pdf


pdf = pdf.PdfManager()
pdf.window.title('Pdf Manager')



gui.Label(tk.Label(), pdf.file_n, 0,0,3)

output_split = tk.Entry()
gui.Entry(output_split,'Split Output Pdf Name',1,0)

gui.Button(tk.Button(), 'Browse pdf to split',0, 3, lambda: pdf.file_path())

output_path = tk.Button()
gui.Button(output_path, 'Select output path', 0, 4, lambda: pdf.output_path())

split_start = tk.Entry()
gui.Entry(split_start, 'Starting Page number', 1, 1)

split_end = tk.Entry()
gui.Entry(split_end, 'Ending Page number', 1, 2)

gui.Button(tk.Button(), 'Split', 1, 3, lambda : pdf.pdf_split(split_start.get(), split_end.get(),  output_split.get()))
gui.Button(tk.Button(), 'Browse pdfs to merge', 2, 3, lambda: pdf.files_path())

output_merged = tk.Entry() 
gui.Entry(output_merged, 'Merged Output Name', 2, 1)

gui.Button(tk.Button(), 'Merge', 2, 2, lambda: pdf.pdf_merge(output_merged.get()))

gui.Label(tk.Label(), pdf.process_msg, 3, 0, 5, 'red')

tk.mainloop()


    