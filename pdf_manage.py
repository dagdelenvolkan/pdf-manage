import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter
import os


class PdfManager():

    def __init__(self):
        self.window = tk.Tk()
        self.file_p = tk.StringVar()
        self.file_n = tk.StringVar()
        self.process_msg = tk.StringVar()
        self.pdfs = []

    def file_path(self):
        """
        Create a function that select a file path for tkinter button
        """

        file_name = filedialog.askopenfilename()
        self.file_p.set(file_name)
        self.file_n.set(self.file_p.get().split('/')[-1])

    def output_path(self):
        """
        Select folder path to save output
        """

        os.chdir(filedialog.askdirectory())

    def files_path(self):
        """
        Create a pdf paths list for multiple files
        """

        file_names = filedialog.askopenfilenames()
        files = list(file_names)
        self.pdfs.append(files)


    def pdf_split(self, range_s, range_e, pdf_name):
        """
        Split pdf files with selected page numbers

        :param string path: The pdf's file path
        :param int range_s: Page number which start split process.
        :param int range_e: Page number which end splitting process.
        :param string pdf_name: The pdf file output name which created after splitting process.
        """
        
        pdf = PdfFileReader(self.file_p.get())
        
        pdf_writer = PdfFileWriter()

        for i in range(int(range_s), int(range_e) + 1):
            pdf_writer.addPage(pdf.getPage(i))

        
        output_fname = pdf_name + '.pdf'

        with open(output_fname, 'wb') as out:
            pdf_writer.write(out)   

        self.process_msg.set('Split process has successfully done') 

    def pdf_merge(self, out_name):
        """
        Function create merge the selected pdf files

        :param string out_name: The pdf file output name which created after merging process.
        :param List pdfs_path:  The list of pdf files pathes list.
        """

        pdf_writer = PdfFileWriter()

        for path in self.pdfs[0]:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
                
        with open(out_name + '.pdf', 'wb') as out:
            pdf_writer.write(out)

        self.process_msg.set('Merge process has successfully done')

