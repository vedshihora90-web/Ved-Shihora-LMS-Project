#2.project

print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\n")
    print("select an option:")
    print("1.Generate a pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")
    print("\n")
    num=(int(input("enter your choice:")))

    if num==1:
        row=(int(input("Enter the number of rows for the pattern:")))
        
        print("\n")
        print("pattern:")
        for i in range(1,row+1):
            for j in range(i):
                print("*",end="")
            print()
    elif num==2:
        total=0
        start=(int(input("Enter the start of the range:")))
        end=(int(input("enter the end of the range:")))
        for num in range(start,end+1):
            if num%2==0:
                print(f"number {num} is even")
            else:
                print(f"number {num}is odd")
            total+=num
        print(f"sum of all numbers from {start} to {end} is:{total}")
    
    elif num==3:
        print("Exiting the program ! good bye")
        break
    else:
        print("invalid choice!")

