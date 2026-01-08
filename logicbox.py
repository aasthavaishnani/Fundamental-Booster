print("Welcome to The Pattern Generator & Number Analyzer!")
while True:
    print("\nChoose an option:")
    print("1.Pattern Generation")
    print("2.Number Analysis")
    print("3.Exit")
    ch = int(input("Enter your choice (1-3): "))
    
    match ch:
        case 1:
            while True :
                print("\nChoose Pattern Type:")
                print("1. Star Triangle")
                print("2. Inverted Star Triangle")
                print("3. Number Triangle")
                print("4. Repeating Number Triangle")
                print("5. Star Pyramid")
                print("6. Floyd's Number Triangle")
                print("7.Exit")
            
                pt = int(input("Enter your choice (1-7): "))
                print("\nGenerated Pattern:\n")
                
                match pt:
                    case 1:
                        rows = int(input("Enter the number of rows: "))
                        for i in range(1, rows + 1):
                            print("*" * i)
                    case 2:
                        rows = int(input("Enter the number of rows: "))
                        for i in range(rows, 0, -1):
                            print("*" * i)
                    case 3:
                        rows = int(input("Enter the number of rows: "))
                        for i in range(1, rows + 1):
                            for j in range(1, i + 1):
                                print(j, end=" ")
                            print()
                    case 4:
                        rows = int(input("Enter the number of rows: "))
                        for i in range(1, rows + 1):
                            print(str(i) * i)
                    case 5:
                        rows = int(input("Enter the number of rows: "))
                        for i in range(1, rows + 1):
                            print(" " * (rows - i) + "* " * i)
                    case 6:
                        rows = int(input("Enter the number of rows: "))
                        num = 1
                        for i in range(1, rows + 1):
                            for _ in range(i):
                                print(num, end=" ")
                                num += 1
                            print()
                    case 7:
                        break
        case 2:
            start = int(input("Enter starting range: "))
            end = int(input("Enter end of the range: "))
            
            if start>end:
                start,end=end,start
                
            total = 0
            for i in range(start,end + 1):
                if i%2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")

                total += num
            print(f"Sum of {start} to {end} is: {total}")
            
        case 3:
            print("\nThank you for using the Student Data Organizer. Goodbye!\n")
            break
        
        case _ :
            print("Invalid choice! Please enter between 1-6.")