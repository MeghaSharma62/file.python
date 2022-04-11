my_file = open("people1.txt")
file_data = my_file.read()
print (file_data)
my_file.close()


# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("")
# for student in batch1_students:
#         students_file.write(" + student + "\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.close()

# f= open("myfile.txt", "x")


# my_file = open("people1.txt","+")
# file_data = my_file.write("love\nlife\nlive")
# my_file.close()

# file=open('divya.txt',"w")
# file.write("megha "  "sharma")
# file.close()

a="Teena"
i=0
b=[]
j=5
while i<len(a):
        if a[i] not in b:
                c=a[i]
                b.append(c)
                b.append(j)
                j+=5
        i+=1
print(b)