from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
from read_curriculum import read_curriculum
from xlrd.sheet import ctype_text

def read_student_grades():
    fname = join(dirname(dirname(abspath(__file__))), 'crs', 'sampleStudent.xls')
    #open the workbook

    xl_workbook = xlrd.open_workbook(fname)
    
    sheet_names = xl_workbook.sheet_names()

    # print ('Sheet Names', sheet_names)

    # print ('hello')

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    
    row = xl_sheet.row(0) 

    # print (type (row))

    # print ('(Column # ) type:value')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        # print ('(%s) %s %s ' % (idx, cell_type_str, cell_obj.value))

    #print columns 0,1,2,3,5

  #  listOfColumnIndices = [0,1,2,3,5]
    listOfColumnIndices = [0,5]

    student_grades = {}
    
    for row_idx in range(1, xl_sheet.nrows):
        #print ('-'*40)
        #print ('Row: %s ' % row_idx) #print row number
        cell_obj_key = xl_sheet.cell(row_idx, 0)
        cell_obj_val = xl_sheet.cell(row_idx, 5)
        #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        if (cell_obj_key.value in student_grades):
            pass
        else:
            student_grades[cell_obj_key.value] = cell_obj_val.value



    # print (student_grades)
    return student_grades
