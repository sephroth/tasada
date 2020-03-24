import re
import datetime


filename1="readyourself.txt"
filename2="from CERN.txt"
f=open(filename2,"r",encoding='utf-8')
print("The file : {filename} loads successed~".format(filename=filename2))
words=f.readlines()

word=re.findall(r'<meta property=.*?>',str(words))

timenow = datetime.datetime.now()
count=0
for i in word:
    count+=1
print("Now the time is {time}".format(time=timenow))
print("Let me show you the count of the word you search",count)
print('The result you search is:\n',word,sep='\n')


