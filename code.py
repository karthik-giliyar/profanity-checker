import urllib
from better_profanity import profanity

count=0

files  = open("racial-words.TXT","r")
lines=files.read().split("\n")

k=1
for i in lines:

    profanity.load_censor_words()
    word = profanity.censor(i)
    words=word.split()

    for j in words:
        if j=="****":
          count+=1
    

    print("Degree of profanity for the line ",k,"is ",count)
    count=0
    words=[]
    k+=1
  
      
    
  

        



