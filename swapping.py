#Take input using input()

#input() takes input in form of the string
in_string=input()

#here extract the two numbers from the string

x,y = in_string.strip().split(',')
#print x and y before swapping

x = int(x)
y = int(y)
print("x before swapping:",x)
print("y before swapping:",y)

#Writing your swapping code here
x = x+y
y = x-y
x = x-y

print()
#print x and y after swapping
print("x after swapping:",x)
print("y after swapping:",y)


