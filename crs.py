from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
from read_curriculum import read_curriculum
from read_student_grades import read_student_grades
from xlrd.sheet import ctype_text



class crs(object):

    curriculum = read_curriculum()
    student_grades = read_student_grades()

    print (curriculum)
    print (student_grades)
   
crs()
