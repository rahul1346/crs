from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd


class crs(object):


    fname = join(dirname(dirname(abspath(__file__))), 'crs', 'sampleStudent.xls')
    #open the workbook

    xl_workbook = xlrd.open_workbook(fname)
    
    sheet_names = xl_workbook.sheet_names()

    # print ('Sheet Names', sheet_names)

    # print ('hello')

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    
    row = xl_sheet.row(0) 

    # print (type (row))

    from xlrd.sheet import ctype_text

    # print ('(Column # ) type:value')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        # print ('(%s) %s %s ' % (idx, cell_type_str, cell_obj.value))

    #print columns 0,1,2,3,5

  #  listOfColumnIndices = [0,1,2,3,5]
    listOfColumnIndices = [0,5]

    col = {}
    
    for row_idx in range(1, xl_sheet.nrows):
        #print ('-'*40)
        #print ('Row: %s ' % row_idx) #print row number
        cell_obj_key = xl_sheet.cell(row_idx, 0)
        cell_obj_val = xl_sheet.cell(row_idx, 5)
        #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        col[cell_obj_key] = cell_obj_val



    print (col)

    cname = join(dirname(dirname(abspath(__file__))), 'crs', 'EE-curriculum-October2014 (11).xls')
    cl_workbook = xlrd.open_workbook(cname)

    sheet_names = cl_workbook.sheet_names()

    print ('Sheet Names', sheet_names)

    print ('hello')

    cl_sheet = cl_workbook.sheet_by_name(sheet_names[0])

    row = cl_sheet.row(0) 

    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print ('(%s) %s %s ' % (idx, cell_type_str, cell_obj.value))


    num_cols = cl_sheet.ncols
    list_of_courses = []

    for row_idx in range(1, cl_sheet.nrows):
        print ('-'*40)
        print ('Row: %s ' % row_idx) #print row number
        for col_idx in range(0, num_cols):  # Iterate through columns
            cell_obj = cl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

     
    for row_idx in range(7, 14):
            #print ('-'*40)
            #print ('Row: %s ' % row_idx) #print row number
            list_of_courses.append(cl_sheet.cell(row_idx,0))
            list_of_courses.append(cl_sheet.cell(row_idx,7))

            #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

    # print (list_of_courses)

    for row_idx in range(19, 25):
            #print ('-'*40)
            #print ('Row: %s ' % row_idx) #print row number
            list_of_courses.append(cl_sheet.cell(row_idx,0))
            list_of_courses.append(cl_sheet.cell(row_idx,7))
            
            #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

    # print (list_of_courses)

    for row_idx in range(30, 36):
            #print ('-'*40)
            #print ('Row: %s ' % row_idx) #print row number
            list_of_courses.append(cl_sheet.cell(row_idx,0))
            list_of_courses.append(cl_sheet.cell(row_idx,7))
            
            #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

    # print (list_of_courses)

    for row_idx in range(41, 46):
            #print ('-'*40)
            #print ('Row: %s ' % row_idx) #print row number
            list_of_courses.append(cl_sheet.cell(row_idx,0))
            list_of_courses.append(cl_sheet.cell(row_idx,7))
            
            #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

    list_of_courses.append(cl_sheet.cell(15,7))


    print (list_of_courses)


crs()
