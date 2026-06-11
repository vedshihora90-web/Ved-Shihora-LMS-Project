#1.check evenn number using type error and value error

def check_even():
    num=int(input("enter an integer:"))

    if not isinstance(num,int):
        raise TypeError("input must be an integer")
    if num %2!=0:
        raise ValueError("number is odd")
    print("number is even")

try:
    check_even()
except TypeError:
        print("enter value must be only int")
except ValueError:
        print("enter value must be onli num")
except Exception as e:
        print("error:",e)
