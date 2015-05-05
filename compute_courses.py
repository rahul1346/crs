import unicodedata


def compute_failed_courses(student_grades):
    list_of_failed_courses = []
    for key,value in student_grades.iteritems():
 #       print (key, value)
        #if value == "text:u'F'":
        if (type (value) == unicode):
            student_grade = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            if ((student_grade == 'F') | (student_grade == 'D-')):
                if ((key[:2] == 'L1') | (key[:2] == 'L2') | (key[:2] == 'L3') | (key[:2] == 'L4')):
                    pass
                else:
                    keystr = unicodedata.normalize('NFKD',key).encode('ascii','ignore')
                    list_of_failed_courses.append(keystr)
            #        print (type (value))

    list_of_failed_courses.sort(key=lambda x: x.split(" ")[-1])
    return list_of_failed_courses

def process_curriculum(curriculum):
    # pass
    curriculum_str = []
    for key in curriculum:
        # print (type (key), key)
        curriculum_str.append(unicodedata.normalize('NFKD', key).encode('ascii','ignore'))

    return curriculum_str

def fetch_class(curriculum, student_grades):
    return None

def compute_courses(student_grades, curriculum) :
    #print (student_grades)
    # print (curriculum)
    list_of_rec_courses = []
    list_of_failed_courses = compute_failed_courses(student_grades)
    # print (list_of_failed_courses[:6])
    curriculum_str = process_curriculum(curriculum)
    # print (curriculum_str)

    if (len(list_of_failed_courses) >=10):
        return list_of_failed_courses[:6]

    list_of_rec_courses = list_of_failed_courses

    num_of_additional_courses_to_propose = 10 - len(list_of_rec_courses) 

    for i in range(num_of_additional_courses_to_propose):
        list_of_rec_courses.append(fetch_class(curriculum, student_grades))

    return list_of_rec_courses






    
