# list comprehension program

#1.square from 1 to 10

square=[x*x for x in range (1,11)]
print(square)

#2.only even numbers

even_numbers=[x for x in range(1,21)if x%2==0]
print(even_numbers)

#3.converting string to lower case:
words=["HYello","WORLD","PytHoN"]
lowercase_words=[w.lower() for w in words]
print(lowercase_words)
