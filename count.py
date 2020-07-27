file = open("example.txt","r")

fdata=file.read()

s="example" #or input("Enter search term)

countt=fdata.count(lower(s))

print('number of ',s,' = ',countt)
