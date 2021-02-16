score = int(input("Please Enter your score: "))
scoreArr = []

if(score >= 70 and score <= 100):
    print("Excellent, you got A ", score)
    scoreArr.append(score)
elif (score >= 60 and score < 70):
    scoreArr.append(score)
    print("You got B", score)
elif (score >= 50 and score < 60):
    scoreArr.append(score)
    print("You got C", score)
elif (score >= 40 and score < 50): 
    scoreArr.append(score)
    print("You got D", score)
elif (score >= 35 and score < 40):
    scoreArr.append(score)
    print("You got", score)
elif(score >=0 and score < 35):
    scoreArr.append(score)
    print("You got F", score)
else :
    print("invalid")
print(scoreArr)