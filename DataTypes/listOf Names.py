names=input("Enter a list of names separated by commas: ")
names.split(",")
Unique_names=list(set(names))
namesSorted=sorted(Unique_names)
numberingNames= [(i+1,names)for i, name in enumerate(namesSorted)]
print(names)
print(Unique_names)
print(namesSorted)
print(numberingNames)