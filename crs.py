from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd



class crs():




    fname = join(dirname(dirname(abspath(__file__))), 'crs', 'sampleStudent.xls')

    #open the workbook

    xl_workbook = xlrd.open_workbook(fname)
    
    sheet_names = xl_workbook.sheet_names()

    print ('Sheet Names', sheet_names)

    print ('hello')

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    
    row = xl_sheet.row(0) 

    print (type (row))

    from xlrd.sheet import ctype_text

    print ('(Column # ) type:value')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print ('(%s) %s %s ' % (idx, cell_type_str, cell_obj.value))

    #print columns 0,1,2,3,5

    listOfColumnIndices = [0,1,2,3,5]

    for row_idx in range(1, xl_sheet.nrows):
        print ('-'*40)
        print ('Row: %s ' % row_idx) #print row number
        for col_idx in listOfColumnIndices:
            cell_obj = xl_sheet.cell(row_idx, col_idx)
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
    

crs()
