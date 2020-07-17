import tkinter as tk


def Entry(entry,insert_text, row, column):
    """
    Create Tkinter Entry Widget

    :param string insert_text: Placeholding text for Entry
    :param int row: Row number for Entry's grid
    :param int column: Column number for Entry's grid
    """
    
    entry.insert(0, insert_text)
    entry.bind('<FocusIn>', lambda args: entry.delete('0', 'end'))
    entry.grid(row = row, column= column)

def Button(button, text, row, column, command):
    """
    Create Tkinter Button Widget
    """
    button['text'] = text
    button['command'] = command
    button.grid(row=row, column=column)

def Label(label, text_variable, row, column, columnspan = 1, foreground_c = 'black'):
    """
    Create Tkinter Label Widget
    """
    label['textvariable'] = text_variable
    label['foreground'] = foreground_c
    label.grid(row = row, column = column, columnspan = columnspan)