import random

wordslist=[]
text=open("words.txt","r") #openinf readable text file where from which we will get words
passwordFile=open("passwords.txt","w") #file to write filtered passwords-- words  ==>optional
lines=text.readlines() # reading  word.txt file
for line in lines:
    words = line.split() #making single words from sentence

    for word in words:
        if len(word)>5 :
            wordslist.append(word.capitalize())  #appending words in  wordslist and capitalizing them
            passwordFile.write("  {0}  ,".format(word))  #==>optional


special=["!","@","#","$","%","^","&","*" ]   
password=(random.choice(wordslist))+(random.choice(special))+(str(random.randint(100,999)))
print(password)
# ------------------------------------------------------------------------------------------
