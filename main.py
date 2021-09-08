import json

#read the json file
jfile=open('quiz.json','r')
jsondata=jfile.read()

#parse
obj=json.loads(jsondata)
score = 0

def quize(qtype,q):
    global score
    print(obj['quiz'][qtype][q]['question'])
    print('options')
    j=1
    for i,j in zip(obj['quiz'][qtype][q]['options'],range(1,5)):
        print(j,".",i)
    raw_ans=input('type correct option')
    ans=int(raw_ans)
    answer=obj['quiz'][qtype][q]['options'][ans-1]
    #print(type(answer))
    if (answer == obj['quiz'][qtype][q]['answer']):
        score=score+1
    



print("which quiz do you  want to take")
print("1. maths")
print("2. sport")

raw_val=input("enter the number")
val=int(raw_val)

if (val == 1):
    quize("maths","q1")
    quize("maths","q2")
    print("final score is",score)
elif (val ==2):
    quize("sport","q1")
    print("final score is",score)
else: print('choose correct option')
