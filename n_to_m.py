# Using a for loop and the range function, 
# prompt the user for the number to start on and the number to end on.

start = int(input("Start from "))
end = int(input("End on ")) + 1 # must add the 1 because the range does not include the ending value

for number in range(start, end):
    print(number)