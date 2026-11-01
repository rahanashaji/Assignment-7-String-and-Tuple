# Strings (Concatenation, Slicing and Other methods) :
# 1. String Concatenation:

string1 = "Hello "
name = input("Enter your name : ")
string2 = string1 + name 
print(string2)

string3 = ", welcome to Python programming"
string2 = string2 + string3
print(string2)

# 2. String Slicing and Indexing:

string = input("Enter the concatenated string: ")
print("First character: ", string[0])
print("Last character: ", string[-1])
print("First 5 characters: ", string[:5])
print("Last 11 characters: ", string[-11:])
print("Reverse: ", string[::-1])
print("Word Python: ", string[23:29])

# 3. String Methods:

strM = "Python beginner tutorial"
print("Uppercase: ",strM.upper())
print("Lowercase: ",strM.lower())
print("Capitaliza: ",strM.capitalize())
print("Count of 't': ",strM.count("t"))
print("Replacing Python with Machine Learning: ",strM.replace("Python","Machine Learning"))

# Tuples (Creation, Modification and Access) :

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t_combine = t1 + t2
print("Combined tuple: ",t_combine)
print("Repeated tuple: ",t_combine*3)
print("3rd element: ",t_combine[2])
print("First 3 elements: ",t_combine[0:3])
print("Last 3 elements: ",t_combine[-3:])
