#GPA_CALC.py
#this program calcultes the unweighted gpa 
#Will expand to include weighted gpa 

def main():
    print ('This program calcultes the weighted gpa ')
    print('Hope this works')

    class_num = eval(input("Enter number of classes: "))
    classes = []
    #for i in range(class_num):
        #class_name = input("Enter Class Name: ")
        #classes.append(class_name)

    credits_list= []
    for x in range(class_num):
        class_credit = eval(input("Enter number of credits of class(In same order as imputed earlier)"))
        credits_list.append(class_credit)

    grades =[]
    for y in range(class_num):
        class_grade = input("Enter Letter grade recived in class(In same order as imputed earlier)")
        grades.append(class_grade)
    
    #print('Class list is: ',classes )
    print('Credits for each class is:',credits_list)
    print('Grades for each class is: ',grades)

    grade_value = []
    for z in range(class_num):
        if grades[z]in ('A','a'):
            grade_value.append(4)
        elif grades[z]in('B','b'):
            grade_value.append(3)
            #return grade_value
        elif grades[z]in('C','c'):
            grade_value.append(2)

        elif grades[z ]in('D','d'):
            grade_value.append(1)
        else:
            grade_value.append(0)
            
    grades_classes= []
    for i in range(class_num):
        class_grade = credits_list[i]*grade_value[i]
        grades_classes.append(class_grade)

    GPA = sum(grades_classes) / sum(credits_list)

    print('Value of each class is: ', grades_classes)
    print("GPA is ", GPA) 
    
main()



    
