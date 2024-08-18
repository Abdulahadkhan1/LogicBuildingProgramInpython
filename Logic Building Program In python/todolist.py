def add(task,):
    list = input("Enter a new task: ")
    task.append(list)
    print(f"Task '{task}' added.")
def remove(task,):
    list = input("Enter a task to remove: ")
    if task in task:
        task.remove(list)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")
def view(task):
    if task:
        print("\ntask:")
        for index , task in  enumerate(task  , start =1):
            print(f"{index},{task}")
    else:
        print("No task found ")
def display():
    print("Welcome to the List")
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

def to_do_list():
    task = []
    while True :
        display()        
        choice = input("Enter your choice")

        match choice:
         case '1':
            add(task)
         case '2':
            remove(task)
         case '3':
            view(task)
         case '4':
            print("Exiting the list")
            break
         case _:
            print("invalid")
if __name__ == "__main__":
    to_do_list()