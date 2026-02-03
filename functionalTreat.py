def display_menu() :
    """Display main menu"""
    print("\n----Main Menu----")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial using Recursion")
    print("4. Filter Data by Threshold using Lambda Function")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

def InputData() :
    """Input for 1D Array Data"""
    val = input("\nEnter data of 1D Array\n(space separated) : ").split()

    data = []
    for v in val :
        data.append(int(v))
        print("\nYour data has been stored successfully!")
        return data

def DataSummary(data) :
    """Display data summary using built-in functions"""
    print("\nData Summary:")
    print(f"  - Total elements: {len(data)}")
    print(f"  - Minimum value: {min(data)}")
    print(f"  - Maximum value: {max(data)}")
    print(f"  - Sum of all values: {sum(data)}")
    print(f"  - Average value: {sum(data)/len(data):.2f}")

def Factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * Factorial(n - 1)

def FactorialMenu():
    """Factorial menu"""
    num = int(input("\nEnter a number to calculate factorial: "))
    print(f"\nFactorial of {num} is: {Factorial(num)}")

def LambdaFunction(data):
    """Filter data using lambda function"""
    tS = int(input("\nEnter a threshold value to filter out data above that value: "))
    filter = list(filter(lambda x: x >= tS, data))
    print(f"\nFiltered Data (values >= {tS}):")

    for item in filter:
        print(item, end=", ")
    print()

def SortData(data):
    """Sort data menu"""
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        sorted_data = sorted(data)
        order = "Ascending"
    else:
        sorted_data = sorted(data, reverse=True)
        order = "Descending"

    print(f"\nSorted Data in {order} Order:")
    for item in sorted_data:
        print(item, end=", ")
    print()

def DatasetStatisticsValue(data):
    """Return multiple dataset statistics"""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)
    return minimum, maximum, total, average

def DatasetStatistics(data):
    """Display dataset statistics"""
    mn, mx, total, avg = DatasetStatisticsValue(data)
    print("\nDataset Statistics:")
    print(f"- Minimum value: {mn}")
    print(f"- Maximum value: {mx}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {avg:.2f}")

def main():
    """Main controller function"""
    data = []
    print("Welcome to the Data Analyzer and Transformer Program")
    
    while True :
        display_menu()
        ch = int(input("\nEnter your choice : "))

        if ch == 1:
            print(InputData(__doc__))
            data = InputData()

        elif ch == 2:
            print(DataSummary(__doc__))
            DataSummary(data)

        elif ch == 3:
            print(FactorialMenu(__doc__))
            FactorialMenu()

        elif ch == 4:
            print(LambdaFunction(__doc__))
            LambdaFunction(data)

        elif ch == 5:
            print(SortData(__doc__))
            SortData(data)

        elif ch == 6:
            print(DatasetStatistics(__doc__))
            DatasetStatistics(data)

        elif ch == 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")

