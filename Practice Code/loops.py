# Prints 'Hello' 5 times.
i=0
while(i<5):
    print('Hello')
    i += 1
    
mylist = [12,45,12.0,4.7,'strings','some more strings']
i=0
while(i<len(mylist)):
#    Prints each element of a list.
   print(mylist[i])
   i += 1

for i in range(len(mylist)):
#    Prints each element of a list using a for loop with range.
   print(mylist[i])

for item in mylist:
    # Prints each element of a list using a for loop with iteration.
    print(item)