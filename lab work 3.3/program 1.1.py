#list of dictionaries

students=[{"id":"101","name":"alice","score":86},
                  {"id":"102","name":"bob","score":34},
                  {"id":"101","name":"alice","score":75}]
print(students)

#print the name of each student using loop
print("students name:")
for student in students:
      print(student["name"])

#print the average score of all students

total=0
for student in students:
    total+=student["score"]

average=total/len(students)
print(f"\n average score:{average:.2f}")

#a new student record to the list

new_student={"id":"104","name":"zeel","score":99}
students.append(new_student)
print(students)

#update a scor of a student

for student in students:
    if student["id"] ==102:
        student["score"] ==87
print("\n aafter upadeting score")
print(students)
