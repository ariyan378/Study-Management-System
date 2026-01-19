from datetime import datetime

study = {}
day_count = 0  
study_history = []  # List to store daily study records

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

def save_day_to_history():
    """Save current day's study data to history"""
    global day_count
    
    if study:
        day_count += 1
        
        # Create a copy of current study data with timestamp
        day_record = {
            'day': day_count,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'subjects': study.copy(),
            'total_time': sum(study.values()),
            'subject_count': len(study)
        }
        
        study_history.append(day_record)
        print(f"\n✅ Day {day_count} saved to history!")
        
        # Clear current study for next day
        study.clear()
    else:
        print("No data to save for today!")

def view_history():
    """View complete study history"""
    if not study_history:
        print("\n📚 No study history available yet!")
        return
    
    print("\n" + "="*50)
    print("📚 STUDY HISTORY")
    print("="*50)
    
    for record in study_history:
        print(f"\n📅 Day {record['day']} - {record['date']}")
        print(f"   Total Subjects: {record['subject_count']}")
        print(f"   Total Study Time: {record['total_time']} minutes")
        print(f"   Subjects studied:")
        
        for subject, time in record['subjects'].items():
            print(f"      • {subject}: {time} minutes")
        print("-" * 50)
    
    # Show overall statistics
    total_days = len(study_history)
    total_all_time = sum(record['total_time'] for record in study_history)
    avg_per_day = total_all_time // total_days if total_days > 0 else 0
    
    print(f"\n📊 Overall Statistics:")
    print(f"   Total Days Studied: {total_days}")
    print(f"   Total Study Time (All Days): {total_all_time} minutes")
    print(f"   Average Study Time per Day: {avg_per_day} minutes")

def show_statistics(): 
    """Show statistics for current day"""
    if study:
        total = sum(study.values())
        sub_count = len(study)
        average = total // sub_count if sub_count > 0 else 0
        
        print(f"\n📊 Current Day Statistics:")
        print(f"Total Subjects: {sub_count}")
        print(f"Total Study Time: {total} minutes")
        print(f"Average Study Time per Subject: {average} minutes")

        if average <= 80:
            print("\n💪 You Need To Study More")
        else:
            print("✨ Keep Going!")    
    else:
        print("No Data for current day")           


def main():
    while True:
        print("\n=== Study Management System ===")            
        print("1. ADD")            
        print("2. Update")            
        print("3. Delete")            
        print("4. View Current Day")            
        print("5. Show Current Statistics")
        print("6. Save Day & Start New Day")
        print("7. View Complete History")            
        print("8. Exit")     
         
        choice = int(input('Enter Your choice 1/2/3/4/5/6/7/8: '))

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
            save_day_to_history()
        elif choice == 7:
            view_history()
        elif choice == 8:
            print('Closing the Program\n')
            break
        else:
            print("Invalid Choice")

main()