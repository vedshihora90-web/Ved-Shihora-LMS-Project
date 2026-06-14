print("<<<< Welcome To My Program :- Function Treat >>>>")
print("\nWelcome To Data Analyzer And Transformer Program")

data = []

while True:
    print("\nMain Menu :")
    print("1. Input Data")
    print("2. Display Data Summary (built-in function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (lambda function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit program")

    choice = input("\nChoose an option : ")

    if choice == "1":
        print("\nInput Data")
        
        print("\nEnter data for a 1d array")
        
        values = input("(separated by spaces) : ")
        
        data = list(map(int, values.split()))
        
        print("Data stored successfully!")
        
        print("Data = ", data)

    elif choice == "2":
        print("\nDATA SUMMARY")
        
        if not data:
            
            print("Error : Dataset is empty.")
        else:
            print("Dataset:", data)
            print("Total Elements : ", len(data))
            print("Sum of Values : ", sum(data))
            print("Minimum Value : ", min(data))
            print("Maximum Value : ", max(data))
            print("Average Value : ", sum(data) / len(data))

    elif choice == "3":
        
        print("\nCalculate Factorial.")
        
        number = int(input("Enter a number :  "))

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        print("Factorial is : ", factorial(number))

    elif choice == "4":
        
        print("\nFilter Data by Threshold.")
        
        if not data:
            print("Error: Dataset is empty.")
            
        else:
            threshold = int(input("Enter threshold value : "))
            
            filtered = list(filter(lambda x: x > threshold, data))
            
            print("Filtered Data : ", filtered)

    elif choice == "5":
        
        print("\nSort Data")
        
        if not data:
            
            print("Error: Dataset is empty.")
            
        else:
            print("1. Ascending Order.")
            print("2. Descending Order.")
            
            choice = input("Enter your choice : ")

            if choice == "1":
                
                print("Ascending Order : ", sorted(data))
                
            elif choice == "2":
                
                print("Descending Order : ", sorted(data, reverse=True))
                
            else:
                
                print("Invalid choice!")


    elif choice == "6":
        
        print("\nDataset Statistics.")
        
        if not data:
            
            print("Error: Dataset is empty.")
            
        else:
            
            print("Dataset:", data)
            print("Total Elements : ", len(data))
            print("Sum of Values : ", sum(data))
            print("Minimum Value : ", min(data))
            print("Maximum Value : ", max(data))
            print("Average Value : ", sum(data) / len(data))

    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
        
    else:
        print("Invalid choice!")
