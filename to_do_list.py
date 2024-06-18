def adding():
    new_task=input("\nEnter new task:")
    l.append(new_task)
def display():
    if len(l)!=0:
        for serial,value in enumerate(l,start=1):
            print(serial,value)
    else:
        print("No task exist")
def removing():
    if len(l)!=0:
        remove_task=input("\nEnter task to be removed:")
        if remove_task in l:
                l.remove(remove_task)
        else:
            print("\nTask not found")
    else:
        print("\nNo task exist")
def updating():
    if len(l)!=0:
        old_task=input("Enter task to be updated:")
        if old_task in l:
            pos=l.index(old_task)
            new_task=input("Enter updated task:")
            l[pos]=new_task
        else:
            print("Task does not exist")
    else:
        print("\nNo task exist")
def exit():
    print("\nProgram over\nThank you")

l=[]

while True:
    try:
        print("\nMenu\n1.Add\n2.Display\n3.Remove\n4.Update\n5.Exit")
        ch=int(input("\nEnter choice from above:"))
        if ch==1:
            adding()
        elif ch==2:
            display()
        elif ch==3:
           removing()
        elif ch==4:
            updating()
        elif ch==5:
            exit()
            break
        else:
            print("\nInvalid choice Enter again")
    except ValueError:
        print("\nInvalid input Enter again")