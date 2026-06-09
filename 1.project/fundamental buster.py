#1.project

print("Welcome to the Interective Personal Data Collectorr!")
print("\n")

name=str(input("please enter your name:"))
age=int(input("please enter your age:"))
height=float(input("plese enter your height in meters:"))
num=int(input("please enter your name favourite number:"))

print("\n")
print("Thank You! Here is the imformation we collected:")
print("\n")
print(f"Name:{name}(type:{type(name)},Memory address:{id(name)})")
print(f"Age:{age}(type:{type(age)},Memory address:{id(age)})")
print(f"Height:{height}(type:{type(height)},Memory Address:{id(height)})")
print(f"Favourite Number:{num}(type:{type(num)},Memory Address:{id(num)}")

print("\n")
print(f"your birth year is approximately:{2026-age}(based on your age of{age})")
print("Thank You for using the Persanal Data Collector.")
print("Goodbye!")

