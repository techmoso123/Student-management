students={}
def add_student():
    name=input("Enter student name:")
    age=input("Enter students age:")
    gender=input("Enter students gender:")
    class_=input("Enter students class:")
    
    
    #using the global variale student to pass in the name as the first key in the dictionary
    students[name]={'Age':age,'Gender':gender,'Class':class_}
    print(f'Student {name} added succesfully!')

def update_student(name):
    if name in students:
        age = input(f'Enter New age for{name}: ')
        gender = input(f'Enter New gender for{name}: ')
        class_ = input(f'Enter New class for{name}: ')
        
        
        students[name]={'Age':age,'Gender':gender,'Class':class_}
        print(f'Student {name} updated succesfully!')
    else:
        print(f'No student found with this particular name,{name}.Thank you')

def delete_student(name):
    if name in students:
        del students[name]
        print(f'Student {name} has being deleted succesfully!')
    else:
        print(f'student{name} not found!')
def search_students(name):
    if name in students:
        print(f'Here is the students details for {name}: {students[name]}')
    else:
        print(f'user{name}not found, Try again!')
 
while True:
    print("welcome to woolwich poly STUDENTS MANAGEMENT SYSTEM USING PHYTON CREATED BY MOSO")
    print("1.Add a new student")                   
    print("2.Update Student detail")                   
    print("3.Delete Student")                   
    print("4.search for a Student")                   
    print("5.EXIT")
     
    choice=input('Enter your choice (1-5) listed above:')
    if choice =='1':
        add_student()
    elif choice =='2':
        name = input('Enter student name to update:')
        update_student(name)
    elif choice =='3':
        name = input('Enter student name to delete:')
        delete_student(name)
    elif choice =='4':
        name = input('Enter student name to search:')
        search_students(name)
    elif choice =='5':
        break
    else:
        print('Enter the write choce, please try again')    
             
