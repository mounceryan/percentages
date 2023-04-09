# Note that percentage difference is not the same as percentage change.

print("This is for calculating the percentage difference between x and y.")

print("First number: ") 
x = int(input())
print("Second number: ") 
y = int(input())

percentage_difference = ((x-y)/((x+y)/2))*100

print(percentage_difference)