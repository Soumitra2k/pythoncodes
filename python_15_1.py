# How to access Excel data in python

import openpyexcel

# go to the location of the excel file
book=openpyexcel.load_workbook("E:\\Data.xlsx")

#to open the excel sheet

sheet=book.active  # open the excel sheet  programmatically

# to identify the rows and columns in the excel sheet

cell = sheet.cell(row=2, column=5)   ## pointing to the the cell where the data is

# to print the values of the cell

print(cell.value)