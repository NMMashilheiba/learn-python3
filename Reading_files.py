textfile = open("C:/Users/ningt/Documents/words.txt", "r")

for word in textfile.readlines():
    print(word)
    
textfile.close()



#print(textfile.readlines()[1])
#print(textfile.readline())
#print(textfile.readline())



