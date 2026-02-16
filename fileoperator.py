from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def get_timestamp(self):
        today = datetime.now()
        return today.strftime("%d-%m-%Y")

    def addEntry(self):
        try:
            entrytime = self.get_timestamp()
            entry = input("Write journal entry: ")

            with open(self.filename, 'a') as file:
                file.write(f"{entrytime} - {entry}\n")

            print("Entry added successfully.")
    
        except Exception as e:
            print(f"Error: {e}")

        print()

    def viewEntries(self):
        try:
            with open(self.filename, 'r') as file:
                entries = file.readlines()

                if entries:
                    print("Journal Entries:")
                    for entry in entries:
                        print(entry.strip())
                else:
                    print("No entries found.")

        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")
        except Exception as e:
            print(f"Error: {e}")

        print()

    def searchEntries(self):
        try :
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, 'r') as file:
                for line in file:
                    if keyword in line:
                        print(line.strip())

                if not keyword in line:
                    print("No matching entries found.")

        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")
        except Exception as e:
            print(f"Error: {e}")

        print()


    def deleteEntries(self):
        try:
            confirmation = input("Are you sure for delete all your entries? (yes/no): ")

            if confirmation.lower() == 'yes':
                with open(self.filename, 'w') as file:
                    file.write("")
                print("All entries deleted successfully.")
            else:
                print("Deletion cancelled.")

        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")
        except Exception as e:
            print(f"Error: {e}")    
            
        print()
        
manager = JournalManager()

while True:
    print("---File Operator : Personal Journal---")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("0. Exit")

    try:
        ch = int(input("Enter your choice: "))

        if ch == 1: 
            manager.addEntry()

        elif ch == 2:
            manager.viewEntries()

        elif ch == 3:        
            manager.searchEntries()

        elif ch == 4:
            manager.deleteEntries()

        elif ch == 0:        
            print("Exiting the program. Have a greate day !")   
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a valid number.\n")