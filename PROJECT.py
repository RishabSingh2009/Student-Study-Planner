print("================================")
print("STUDENT STUDY PLANNER")
print("================================")

tasks = []

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice=="1":
        subject = input("Enter subject:")
        task_description = input("Enter study task:")

        tasks.append({
            "subject":subject,
            "task":task_description,
            "completed":False
        })

        print("Task added successfully!")    

    elif choice=="2":
        print("\nYour Study Tasks:")

        if len(tasks)==0:
            print("No tasks available")
        else:
           for i,task in enumerate(tasks, 1):
               status="Completed" if task["completed"]else"Pending"
           print(i,task["subject"],"-",task["task"],"-",status)

    elif choice =="3":
        if len(tasks)==0:
            print("No tasks available") 
        else:
            for i, task in enumerate(tasks,1):
             print(i,task["subject"],"-",task["task"]) 

             number = int(input("Enter task number to complete:")) 

             if 1 <= number<=len(tasks):
                 tasks[number-1]["completed"]= True
                 print("Task completed successfully!")      
            else:
               print("Invalid task number.") 

    elif choice =="4":
        if len(tasks)==0:
            print('No tasks available')  
        else:
           for i,task in enumerate(tasks,1):
               print(
                  i,
                  task["subject"],
                  "-",
                  task["task"]
               )

               number = int(input("Enter task number to delete")) 

               if 1 <=number<=len(tasks):
                     tasks.pop(number-1)
                     print("Task deleted successfully")
               else:
                   print("Invalid task number.")      

    elif choice =="5":
        print("Thank you for using Study Planner!")
        break

    else:
        print("Invalid choice. Please try again.")                

