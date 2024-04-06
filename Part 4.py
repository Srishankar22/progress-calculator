# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1954015

# Date: 14.12.2022


valid_range = [0, 20, 40, 60, 80, 100, 120]
total_marks = 0
count = 0
exclude_count, progress_count, trailer_count, retriever_count = 0, 0, 0, 0
decision = True
marks_dict= {}

def check():
    '''
    This function checks the user-entered mark to see if it is in the valid range. If it is a valid mark, it will be added to the total_marks variable.
    If not, it will display an "Out of Range" message. The try-except block used will prevent the programme from crashing when adding the marks to total
    if the user enters a value other than an integer,it will display the "Enter only an integer" message.
    '''
    try:
        checking_marks = int(student_marks)
        if checking_marks in valid_range:
            global total_marks
            total_marks += checking_marks
            global count
            count += 1
        else:
            print("Out of range.\n")

    except ValueError:
        print('Integer required\n')

def id():
    '''This function checks for a valid uow_id input (displaying message telling that the ID cannot be empty, if user didn't enter anything.) '''
    global uow_id
    while uow_id=='':
        print("Should enter the student ID")
        uow_id=input('\nEnter your student ID : ')
        

while decision:
    uow_id=input('\nEnter your student ID : ')
    id()                                           # calling id function
        
    for x in marks_dict.keys():                    # checking if the id already exists in dictionary
        while True:
          if uow_id== x:
             print('Student id already exists.')
             uow_id=input('\nEnter Student ID : ')
             id()
             
          else:
              break
            
    while count == 0:
        student_marks = input("\nplease enter your credit at pass: ")
        check()                                                         #calling the check function
    pass_mark = int(student_marks)                                      #input taken from the user is converted to integer type and assigned to pass_mark variable.

    while count == 1:
        student_marks = input("please enter your credit at defer: ")
        check()
    defer_mark = int(student_marks)

    while count == 2:
        student_marks = input("please enter your credit at fail: ")
        check()
    fail_mark = int(student_marks)

    if total_marks == 120:   # Here the total_marks is checked, if it is 120 then the progression outcome type is checked, else programme will tell the user that the total is incorrect.
        if fail_mark >= 80:  # Checking condition for Exlude 
            print('Exclude')
            marks_dict[uow_id]=f"Exclude - {pass_mark}, {defer_mark}, {fail_mark}"

        elif pass_mark == 120:      # Checking condition for Progress
            print('Progress')
            marks_dict[uow_id]=f"Progress - {pass_mark}, {defer_mark}, {fail_mark}"
            
        elif pass_mark == 100:      # Checking condition for Module trailer
            print('Progress (module trailer)')
            marks_dict[uow_id]=f"Progress (module trailer) - {pass_mark}, {defer_mark}, {fail_mark}"

        elif pass_mark <= 80 and fail_mark < 80:  # Checking condition for Module retriever
            print('Do not progress - module retriever')
            marks_dict[uow_id]=f"Module retriever - {pass_mark}, {defer_mark}, {fail_mark}"
            
    else:
        print('Total incorrect.')

    question = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')

    if question != 'q':      # If user willing to enter another data set, then count and total_marks variables will be assigned to zero and programme loops.
        count = 0
        total_marks = 0

    elif question == 'q':   # This condition will break the loop display the data inside the dictionary, if user willing to exit.
        decision = False
        for id_num in marks_dict.keys():                          # iterating over the dictionary and printing
            print(f'{id_num} : {marks_dict[id_num]}',end=' ')      

