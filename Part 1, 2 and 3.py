# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1954015

# Date: 14.12.2022


#initializing variables
valid_range = [0, 20, 40, 60, 80, 100, 120]
total_marks = 0
count = 0
exclude_count, progress_count, trailer_count, retriever_count = 0, 0, 0, 0
exclude_marks, progress_marks, trailer_marks, retriever_marks = [], [], [], []
decision = True

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
            print("Out of range.")

    except ValueError:
        print('Integer required\n')

def print_list(term,mark_list):
    '''Progression outcome and list name are passed as arguments into the fucntion. This function uses 'for loop' to read the marks inside the nested list and print them.'''
    for loop in mark_list:
        print(f"{term} - {loop[0]},{loop[1]},{loop[2]}")

def marking():
    '''This function is used to convert the marks to string type in order to append them into the text file.'''
    f.write(str(pass_mark))
    f.write(", ")
    f.write(str(defer_mark))
    f.write(", ")
    f.write(str(fail_mark))
    f.write("\n")

def arranging(end,name):
    '''This function is used for reading the data inside the text file and arranging them in order, comparing the first word and print them.'''
    with open("marks sheet.txt", "r") as x:
        for i in x:
            if i[0:end] == name:
                print(i, end = "")

while decision:
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
    
    if total_marks == 120:  # Here the total_marks is checked, if it is 120 then the progression outcome type is checked, else programme will tell the user that the total is incorrect.                                                 
        if fail_mark >= 80: # Checking condition for Exlude 
            print('Exclude')
            exclude_marks.append([pass_mark, defer_mark, fail_mark]) 
            with open("marks sheet.txt","a") as f:                      # Opening a textfile in order to write the given user inputs 
                f.write("Exclude - ")
                marking()
            exclude_count += 1                                          # keep count of the progression outcome.

        elif pass_mark == 120:      # Checking condition for Progress 
            print('Progress')
            progress_marks.append([pass_mark, defer_mark, fail_mark])
            with open("marks sheet.txt","a") as f:                      
                f.write("Progress - ")
                marking()
            progress_count += 1

        elif pass_mark == 100:      # Checking condition for Module trailer
            print('Progress (module trailer)')
            trailer_marks.append([pass_mark, defer_mark, fail_mark])
            with open("marks sheet.txt","a") as f:                      
                f.write("Progress (module trailer) - ")
                marking()
            trailer_count += 1

        elif pass_mark <= 80 and fail_mark < 80: # Checking condition for Module retriever
            print('Do not progress - module retriever')
            retriever_marks.append([pass_mark, defer_mark, fail_mark])
            with open("marks sheet.txt","a") as f:                      
                f.write("Module retriever - ")
                marking()
            retriever_count += 1

    else:
        print('Total incorrect.')

    question = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')

    if question != 'q': # If user willing to enter another data set, then count and total_marks variables will be assigned to zero and programme loops.
        count = 0
        total_marks = 0

    elif question == 'q': # This condition will break the loop and display the histogram , if user willing to exit.
        decision = False
        print(f'''
---------------------------------------------------------
Histogram
Progress  {progress_count} : {progress_count * '*'}
Trailer   {trailer_count} : {trailer_count * '*'}
Retriever {retriever_count} : {retriever_count * '*'}
Excluded  {exclude_count} : {exclude_count * '*'} 

{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.
----------------------------------------------------------\n''')

print("Part 2: Printing stored data from nested lists.\n")
#calling the print_list function and passing the arguments.
print_list("progress",progress_marks)                     
print_list("trailer",trailer_marks)
print_list("Module retriever",retriever_marks)
print_list("Exclude",exclude_marks)


print("\nPart 3: Accessing data and printing from text file.\n")
#calling the arranging function and passing the arguments.
arranging(8,"Progress")                                   
arranging(25,"Progress (module trailer) - ")
arranging(6,"Module")
arranging(7,"Exclude")
