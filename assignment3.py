#assignment
#print the middle names
#add masha at the fourth position
#update the name phionah to "Aladinah"
#display the length of the students list.
#print all the students names using a for loop.
#calculate the total marks for the students marks variable and the answer
StudentsNames = ["Sandra","Patricia","Phionah","Anitah"]
StudentsMarks = [80, 56, 78, 90]

StudentsNames.insert(4, "Masha")
print(StudentsNames)

StudentsNames[2] = "Phionah Aladinah"
print(StudentsNames)

total_length = len(StudentsNames)
print(f"the total length of the students list is: {total_length}")

for names in StudentsNames:
    print(names)

    sum = (80 + 56 + 78 + 90)
    print(f"the total mark is {sum}")