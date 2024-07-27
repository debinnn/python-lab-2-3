list = []
no = int(input("Enter the number of elements to be added to the list: "))
for i in range(no):
    val=int(input("Enter the value: "))
    list.append(val)

print("The list entered is: ", list)
 
a= sum(list)
print("Sum of all the elemets in the list is: ", a)

mul = 1
for i in list:
    mul *= i

print("The product of all the elements in the list is: ", mul)

max = max(list)
print("The largest element in the list is: ", max)

min = min(list)
print("The smallest element in the list is: ", min)