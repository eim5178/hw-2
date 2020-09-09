#Author: Evelyn Moore eim5178@psu.edu
#Collaborator: None
def  getGradePoint(course_grade):
  if course_grade == 'A' :
    gp_course = 4.0
    return gp_course
  elif course_grade == 'A-' :
    gp_course = 3.67
    return gp_course
  elif course_grade == 'B+' :
    gp_course = 3.33
    return gp_course
  elif course_grade == 'B' :
    gp_course = 3.0
    return gp_course
  elif course_grade == 'B-' :
    gp_course = 2.67
    return gp_course
  elif course_grade == 'C+':
    gp_course = 2.33
    return gp_course
  elif course_grade == 'C' :
    gp_course = 2.0
    return gp_course
  elif course_grade == 'D' :
    gp_course = 1.0
    return gp_course
  elif course_grade == 'F' :
    gp_course = 0.0
    return gp_course
  else:
    gp_course = 0.0
    return gp_course

def run():
  calc_num = 0
  total_course_credit =0
  for i in range (3):
    course_grade = input(f"Enter your course {i+1} letter grade: ")
    course_credit = int(input(f"Enter your course {i+1} credit: "))
    gp_course = getGradePoint(course_grade)
    print (f"Grade point for course {i+1} is: {gp_course}")
    calc_num = course_credit * gp_course + calc_num
    total_course_credit = total_course_credit + course_credit
  calc_total = calc_num/total_course_credit
  print(f"Your GPA is: {calc_total}")
if __name__ == '__main__':
  run()