#the datetime is imported into the file 
from datetime import datetime

#the reg_user will check if the registered username already exist in the user.txt textfle through a while loop and if stament
#if the username is found the user will be requested to enter a username name unitl one that is not in the file 
def reg_user():
    if register_user not in list1 :
        while register_user not in list1 :
            break
    else:
        print("User already exist")

#the writing to file function will add the new user detials to the user.txt file once the passwords match 
#if the passwords dont match the program will dispaly a message to the user
def writing_to_file(a,b,c,d,e):
    if register_password==register_confirm:
                with open("user.txt","a") as userfile:
                    userfile.write(a)
                    userfile.write(b)
                    userfile.write(c)
                    userfile.write(d)
                    userfile.write(e)
    else:
        print("The passwords dont match returning to main menu\n")

#the view _mine function will use a for loop to display the user's tasks of the screen
#the program will match the user that is logged in and read info from the tasks.txt file and only print the tasks with the logged in username
#once the task displayed the user is given an edit  the information of their task or enter -1 to go to main menu
# option to mark if the task is complete or either edit a username or the due date of the task
#if the user does not have any task a message will be displayed and taken back the main menu
def view_mine():
    task_dict={}
    num_task = 0
    with open ("tasks.txt","r") as mytaskfile:
        for line2 in mytaskfile:
            new_line2=line2.replace("\n","").split(", ")
            num_task+=1
            task_dict[num_task]=new_line2
            if new_line2[0]==login_username:
                print("Your task are :")
                print("\n")
                print(f'''
                The task number is   : {num_task}
                Your Username        : {new_line2[0]} 
                Task title           : {new_line2[1]}
                Task description     : {new_line2[2]}
                Date of issue task   : {new_line2[3]} 
                Due date             : {new_line2[4]} 
                Completeion status   : {new_line2[5]}''')
        print("\n")
        task_choice=int(input("Please enter the id number of the task you would like to edit,mark as complete or enter -1 to return to main menu: "))
        if task_choice!=-1:
            edit_task=int(input("Please choose an option of what you would like to do\n1.Mark the task as complete\n2.Edit the username or due date of task: "))
            if edit_task==1:
                task_dict[task_choice][-1]="Yes"
            elif edit_task==2:
                edit_question=int(input("Would you like to edit:\n1.Username\n2.Due date: "))
                if  edit_question==1:
                    new_username=input("Please enter the new username you would like to change: ")
                    task_dict[task_choice][0]=new_username
                if edit_question==2:
                    new_due_date=input("Please enter the due date")
                    task_dict[task_choice][-2]=new_due_date
        with open('tasks.txt','w') as task_file:
            for value in task_dict.values():
                task_file.write('{}\n'.format(", ".join(value)))
  
#the add_task function simply writes to the file once the user is done entering all the detials needed to enter a new task                       
def add_task():
      with open("tasks.txt","a") as taskfile:
            taskfile.write(name)
            taskfile.write(",")
            taskfile.write(" ")
            taskfile.write(title)
            taskfile.write(",")
            taskfile.write(" ")
            taskfile.write(description)
            taskfile.write(",")
            taskfile.write(" ")
            taskfile.write(date)
            taskfile.write(",")
            taskfile.write(" ")
            taskfile.write(due)
            taskfile.write(",")
            taskfile.write(" ")
            taskfile.write(Completion)
            taskfile.write("\n")
#the view_all fuction will read all the information from the tasks.txt and display it to the user in a user-friendly way so they can read it 
#each task will be displayed using a for loop
def view_all():
        with open("tasks.txt","r") as f:
            print("These are all the task :")
            print("\n")
            for task in f :
                list1 = task.replace("\n", "").split(", ")
                print(f'''
                Task assigned to   :  {list1[0]}
                Task title         :  {list1[1]}
                Task description   :  {list1[2]}
                Date of issue task :  {list1[3]}
                Due date           :  {list1[4]}
                Completeion status :  {list1[5]}''')


#the display_stats function performes the fuction of generate and display all the overviews to the user using the task_overview and user_overview functions
def display_stats():
    generate()
    print(task_overview())
    print(user_overview())


#the generate function performs what contans the task_overview and user_overview functions
def generate():
    task_overview()
    user_overview()


#the user_overview function will write all the user_overview.txt file all the infomation of the users when it is called in the generate function  
#the fuction will also return all the infomation so that it will be displayed on the screen when it is called in the display_stats fuction
def user_overview():   
    with open("user.txt","r") as statsfile:
            num_user=0
            registered_user={}
            new_user=0
            for i in statsfile:
                new_line3=i.replace("\n","").split(", ")
                if i:
                    num_user+=1
                if "admin"!=new_line3[0]:
                    new_user+=1
                    registered_user[new_user]=new_line3
    with open("user.txt","r") as f:
        alldate=f"These is information for the users\nThe total users are {num_user}\nThe total users genrated using the taskmangaer is {len(registered_user)}\n"
        for x in f:
            username,password=x.split(", ")
            alldate+="\n"+for_each_user(username)
    with open("Useroverview.txt","w") as useroverview_file:
        useroverview_file.write(alldate)
        return alldate


#the for_each_user fuction reads infomation from the tasks.txt file 
#the function will return infomtion such as :
# The total number of tasks assigned to that user.
#the percentage of the total number of tasks have
#been assigned to that user
# the percentage of the tasks assigned to that user
#have been completed
#the percentage of the tasks assigned to that user
#must still be completed
#the percentage of the tasks assigned to that user
#have not yet been completed and are overdue
#the information is returned and used when it is called in the user_overview fuction 
def for_each_user(username):
    with open ("tasks.txt","r") as mytaskfile:
        task_dict={}
        num_task = 0
        complete=0
        uncomplete=0
        num_uncompleted_and_overdue=0
        for line2 in mytaskfile:
            new_line2=line2.replace("\n","").split(", ")
            if username==new_line2[0]:
                num_task+=1
                task_dict[num_task]=new_line2
        
        for i in task_dict:
            if task_dict[i][-1]=="No":
                uncomplete+=1
                date_object=datetime.strptime(task_dict[i][-2],'%d %b %Y')
                today_date=datetime.today()
                if date_object<today_date and task_dict[i][-1]=="No":
                    num_uncompleted_and_overdue+=1
            else:
                complete+=1
        
        if complete!=0:
            complete1=round((complete/len(task_dict))*100,2)
        elif complete==0:
            complete1="0%"

        if uncomplete!=0:
            uncomplete1=round((uncomplete/len(task_dict))*100,2)
        elif uncomplete==0:
            uncomplete1="0%"

        if num_uncompleted_and_overdue!=0:
            overdue=round((num_uncompleted_and_overdue/len(task_dict))*100,2)   
        elif num_uncompleted_and_overdue==0:
            overdue="0%"
    
        
        user=f"Deitails for user {username}\n"
        user+=f"the total number of task assigned to {username} is {len(task_dict)}\n"
        user+=f"the percentage of complete is {complete1}\n"
        user+=f"the percentage of uncomplete is {uncomplete1}\n"
        user+=f"the percentage of overdue and incomplete is {overdue}\n"
    return user


#the task_overview function will write all the task_overview.txt file all the infomation of the task when it is called in the generate function  
#the fuction will also return all the infomation so that it will be displayed on the screen when it is called in the display_stats fuction
#the function will return infomation such as:
#The total number of tasks that have been generated and tracked using the task_manager.py
#The total number of completed tasks.
#The total number of uncompleted tasks.
#The total number of tasks that haven’t been completed and
#that are overdue.
#The percentage of tasks that are incomplete.
#The percentage of tasks that are overdue.  
def task_overview():
    task_dict={}
    num_task = 0
    total_task=0
    new_task=0
    registered_task={}
    num_completed_tasks=0
    num_uncompleted_tasks=0
    num_uncompleted_and_overdue=0
    with open ("tasks.txt","r") as statsfile4:
        
        for line2 in statsfile4:
            new_line2=line2.replace("\n","").split(", ")
            num_task+=1
            task_dict[num_task]=new_line2
            if line2:
                total_task+=1
            if "admin"!=new_line2[0]:
                new_task+=1
                registered_task[new_task]=new_line2
        
        for count in task_dict:
            tas=task_dict[count]
            if "Yes"==tas[-1]:
                num_completed_tasks+=1
            elif "No"==tas[-1]:
                num_uncompleted_tasks+=1
        
        for convert in task_dict:
            convert_=task_dict[convert]
            date_object=datetime.strptime(convert_[-2],'%d %b %Y')
            today_date=datetime.today()
            if date_object<today_date and convert_[-1]=="No":
                num_uncompleted_and_overdue+=1
    task_information=f"This is information for the tasks of the users: \nThe total number of task is: {total_task}\n"
    task_information+=f"The total number of task that were registed using the taskmanger is: {len(registered_task)}\n"
    task_information+=f"The total number  of tasks that are completed is: {num_completed_tasks}\n"
    task_information+=f"The total number of tasks that are incompleteed is: {num_uncompleted_tasks}\n"
    task_information+=f"The percentage of tasks that are incomplete is: {round((num_uncompleted_tasks/num_task)*100,2)}\n"
    task_information+=f"The percentage of tasks that are incomplete and overdue is : {round((num_uncompleted_and_overdue/num_task)*100,2)}\n"
    with open("task_overview.txt","w") as task_overview_file:
        task_overview_file.write(task_information)
    return task_information

#info list varible is an empty list
#the program request user to enter his/her details
info_list=[]
login_username=input("Please enter your username: ")

login_password=input("Please enter your password: ")
#the user.txt file is opened with "with as" which will close automaically
#the for loop is used to create a list from the information that is in the user.txt
#the infofile list is added into the empty list info_list
with open("user.txt","r") as infofile:
    for line in infofile:
        new_line=line.strip().replace(",","")
        content=new_line.split()
        info_list.append(content)

#the while is vaule to true which means it run until the its false
#two varibles are valued to true
#the for loop will check if the username input is in the info_list list if its found varible correct_user will be valued to true and will move to the password
#if the username is found then the index [1] should be match the password input the correct password will value to true
#if the username is not found in the list it will remain false and message will be shown and the user is aked to enter again same as the password 
while True:
    correct_user=True
    correct_password=True
    for i in info_list:
        if login_username in i:
            correct_user=False
            if login_password==i[1]:
                correct_password=False
                print("logging in....")
                break
    if correct_user:
        print("invalid user name")
        login_username=input("Please enter your username: ")
        login_password=input("Please enter you password: ")
    
    elif correct_password:
        print("incorrect password")
        login_username=input("please enter your username: ")
        login_password=input("Please enter your password: ")  
    else:
        break     

#once the login info is correct a menu is presented
# the while loop is true and is used to show the menu once the person has logged in and once they are done with any option   
# the if statment only allows the admin to access it if not a message will be shown
#there are two menus the other users menu then the admin menu
#the first option request information from the admin 
#the reg_user fuction is called when the admin selects r
#if it is not the admin logged in and they try to register a message will be displayed
while True:
    print("Main menu")
    print("\n")
    if login_username=="admin":
        print("r- Register user\na- Add task\nva- View all task\nvm- View my task\ngr- Generate reports\nds-Display statistics\ne- Exit")
        action=input("Please select one of the options above by enter only the number of the option: ")
    
    if login_username!="admin":
            print("r- Register user\na- Add task\nva- View all task\nvm- View my task\ne- Exit")
            action=input("Please select one of the options above by enter only the number of the option: ")
            print("\n")
    
    if action.upper()=="R":
        if login_username=="admin":
            num_user = 1
            with open("user.txt", "r") as userFile :
                list1 = userFile.read().replace("\n", ", ").split(", ")
                while num_user == 1:
                    register_user=input("Please enter your username: ")
                    reg_user()
                    if register_user not in list1:
                        num_user-=1
                        register_password=input("Please enter a new password: ")
                        register_confirm=input("please re-enter the password: ")
                        writing_to_file(register_user,","," ",register_confirm,"\n")
        else:
            print("you are not authorised to register new users")
    
#if the user selects vm the prpgram will call the view_mine fuction
# this fution will display fuctions of the user logged in   
    if action.upper()== "VM":
        view_mine()

#if the user select the "a" option they be requested to entered information about the task
#then the add_task fuction is called and the tasks.txt file is opened with "with as" which will close automaically
    if action.upper()=="A":
        import datetime
        date=datetime.date.today().strftime('%d %b %Y')
        name=input("Please enter the username of the person the task is assigned to: ")
        title=input("Please enter the title of the task:")
        description=input("Please enter a the description of the task: ")
        due=input("Please enter the due date of the task: ")
        Completion="No"
        add_task()

#if the user selects "va" all the infomation from tasks.txt will be read by the view_all fuction being called
#the tasks.txt file is opened with "with as" which will close automaically  
    if action.upper()=="VA":
        view_all()

# only admins have this option 
#this will call the generate fuction and write to the two files task and user overview.txt
    if action.upper()=="GR":
        generate()
#
# only the admin has this option 
#this will call the generate fuction and write to the two files task and user overview.txt and display all the staticts on to the screen
    if action.upper()=="DS":
        display_stats()

# if the user selects e it will print a message and close the program  
    if action.upper()=="E":
        print("Logging out.....")
        break
    #number=