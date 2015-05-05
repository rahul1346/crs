import unicodedata



def compute_failed_courses(student_grades):
    for key,value in student_grades.iteritems():
 #       print (key, value)
        #if value == "text:u'F'":
        if (type (value) == unicode):
            student_grade = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            if (student_grade == 'F'):
                print key
            #        print (type (value))
    

def compute_courses(student_grades, curriculum) :
    print (student_grades)
    print (curriculum)
    compute_failed_courses(student_grades)
    
