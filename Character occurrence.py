string = input("please enter own word:")
char = input("please enter own character:")
i = 0
count = 0
while (i < len(string)):
    if (string[i]== char):
        count = count +1
    i =i + 1
print ("total number of times ", char ,"has occurred is = "  ,count)
