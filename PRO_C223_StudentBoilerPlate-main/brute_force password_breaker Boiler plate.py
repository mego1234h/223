import PyPDF2 as pd
filename = input('Path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdfReader(file)
from random import randint
import time

d1=0
d2=0
d3=0
d4=0
tried = 0
triedPasswords=[]

if not pdfReader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile=open("wordList.txt")
    body=wordListFile.read().lower()
    words=body.split("\n")
    # for i in range(len(words)):
    #     word=words[i]
    #     print(f"trying to decode password by {word}")
    #     result=pdfReader.decrypt(word)
    #     if result==1:
    #         print(f"Success! We're in! The password is {word}!")
    #         break
    #     elif result==0:
    #         tried=tried+1
    #         triedPasswords.append(word)
    #         print(f"Tried passwords:{triedPasswords}")
    #         continue
    while True:
        letter=["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","!","£","$","%","&","*","(",")","{","}",":","?","@","'",",","/",".","#",";"]
        #word=letter[randint(1,len(letter)-1)]+letter[randint(1,len(letter)-1)]+letter[randint(1,len(letter)-1)]+letter[randint(1,len(letter)-1)]
        d1=d1+1
        if d1==len(letter)-1:
            d2=d2+1
            d1=0
        if d2==len(letter)-1:
            d3=d3+1
            d2=0
        if d3==len(letter)-1:
            d4=d4+1
            d3=0
        if d4==len(letter)-1:
            d4=0
        word=(str(letter[d1])+str(letter[d2])+str(letter[d3])+str(letter[d4]))
        print(f"trying to decode password by {word}")
        #time.sleep(0.001)
        result=pdfReader.decrypt(word)
        if result==1:
            print(f"Success! We're in! The password is {word}!\nTried passwords:{triedPasswords}\n That's {tried} passwords!")
            break
        elif result==0:
            tried=tried+1
            triedPasswords.append(word)
            #print(f"Tried passwords:{triedPasswords}")
            continue