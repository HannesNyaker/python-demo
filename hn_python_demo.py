#print function
print("This is a showcase of different python functions")

#name input and response
name = input("Please enter your name: ")
print("Nice to meet you, " + name + "!")

#declares and prints a list of numbers, both integers and floating point numbers
numberList = [4, 324, -30.3, -2, 2.5, 2, 5.7, 34, 50.5, 18]
print("The number list: " + str(numberList))

#declaring the counters to start at 0
intCounter = 0
floatCounter = 0

#checks the type of the values in numberList with a for-loop
for number in numberList:
    if type(number) == int:
        intCounter += 1
    elif type(number) == float:
        floatCounter += 1

print("The list consists of " + str(intCounter) + " integers and " + str(floatCounter) + " floating point numbers")

#creates datalist.txt and writes the numberList into the text file
file = open("datalist.txt", "w+")
file.write(str(numberList))
print("The numberlist has been successfully saved in datalist.txt!")
#closing the file afterwards to free up memory
file.close()

#creates datalist_copy.txt and copies everything from datalist.txt into the new file
file1 = open ("datalist.txt")
file2 = open ("datalist_copy.txt", "w+")
#for-loop copies the list from datalist.txt into datalist_copy.txt
for i in file1.readline():
    file2.write(i)
#checks if the content is the same, if yes it prints successfull copy message. If no, prints error
if (file1.readline() == file2.readline()):
    print("The datalist has been successfully copied to datalist_copy.txt!")
else:
    print("Error! The datalist copy was unsuccessful!")
#closing the file afterwards to free up memory
file1.close()
file2.close()

#prints the list in datalist_copy.txt
file = open ("datalist_copy.txt", "r")
content = file.readline()
print("datalist_copy.txt consists of this list: " + content)
#closing the file afterwards to free up memory
file.close()
