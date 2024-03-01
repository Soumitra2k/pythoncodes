from openpyexcel import load_workbook
#load the work book
workbook = load_workbook("E:\\Data.xlsx")

# extract the data from sheet

sheet1=workbook['Sheet1']
data_sheet1=[]


for row in sheet1.iter_rows():
    data_row=[]
    for cell in row:
        data_row.append(cell.value)
    data_sheet1.append(data_row)

# extract data from sheet2

sheet2= workbook['Sheet2']
data_sheet2=[]

for row in sheet2.iter_rows():
    data_row=[]
    for cell in row:
        data_row.append(cell.value)
    data_sheet2.append(data_row)

# printing the data from sheet1

print("Data from sheet1:")
for row in data_sheet1:
    print(row)

# printing the data from sheet2

print("Data from sheet2:")
for row in data_sheet2:
    print(row)



