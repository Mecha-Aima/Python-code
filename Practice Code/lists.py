languages = ["C","Python","Javascript","Julia","Dart"]
print(languages)

languages[0] = "C#"     #string indexing
print(languages[0:2])  #string slicing

intlist = [56,25,89,70,5,9,200,66,43,48,49,75,75,100,0]
floatlist = [1.2,0.5,0.62,"floating",8.95,5.5,7.0]

intlist.sort()
print("Sorted list : ",intlist)

intlist.reverse()
print("Reversed List : ",intlist)

floatlist.append(250)
print("Appended list : ",floatlist)

intlist.insert(5,77)
print("Inserted List : ",intlist)

intlist.pop(5)
print("Popped List : ",intlist)

floatlist.remove(250)
print("Modified floatlist : ",floatlist)
