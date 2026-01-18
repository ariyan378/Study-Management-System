from datetime import datetime

study = {}
day_count = 0  

def add_Data(name, time):
    if name in study:
        # If subject exists, add the new time to existing time
        study[name] += time
        print(f"Subject '{name}' already exists!")
        print(f"Added {time} minutes to existing time.")
        print(f"New total time for '{name}': {study[name]} minutes")
    else:
        # If subject doesn't exist, create new entry
        study[name] = time
        print(f"Subject name '{name}': study time {time} min - Added Successfully!")

def update_Data(name, time):
    if name in study:
        study[name] = time
        print(f"Updated! Subject '{name}': New study time {time} min")
    else:
        print(f"This Subject Name '{name}' is Not Found!")

def delete_Data(name):
    if name in study:
        del study[name]
        print(f"Subject name '{name}' is Deleted")
    else:    
        print(f"This Subject Name '{name}' is Not Found!")

def view_data():
    if study:
        print("\n--- Current Study List ---")
        for name, time in study.items():
            print(f"{name}: {time} minutes")
    else:
        print("No Study Plan Found")     

def show_statistics(): 
    global day_count  

    if study:
        day_count += 1 
        
        total = 0
        for time in study.values():  
            total += time
        
        sub_count = len(study)
        
        average = total // sub_count if sub_count > 0 else 0
        
        print(f"\n📊 Study Day Count : {day_count}")
        print(f"Total Subjects: {sub_count}")
        print(f"Total Study Time: {total} minutes")
        print(f"Average Study Time per Subject: {average} minutes")

        if average <= 80:
            print("\n You Need To Study More")
        else:
            print("Keep Going")    
    else:
        print("No Data")           


def main():
    while True:
        print("\n=== Study Management System ===")            
        print("1. ADD")            
        print("2. Update")            
        print("3. Delete")            
        print("4. View")            
        print("5. Show Statistics")            
        print("6. Exit")     
         
        choice = int(input('Enter Your choice 1/2/3/4/5/6: '))

        if choice == 1:
            name = input("Enter Subject Name: ")
            time = int(input("Enter Study Time (minutes): "))
            add_Data(name, time) 
        elif choice == 2:
            name = input("Enter Subject Name to Update: ")
            time = int(input("Enter New Study Time (minutes): "))
            update_Data(name, time) 
        elif choice == 3:
            name = input("Enter Subject Name to Delete: ")
            delete_Data(name)
        elif choice == 4:
            view_data() 
        elif choice == 5:
            show_statistics()
        elif choice == 6:
            print('Closing the Program\n')
            break
        else:
            print("Invalid Choice")

main()
