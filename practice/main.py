score = int(input("Please Enter your score: "))

if(score >= 70 and score <= 100):
    print("Excellent, you got A "+ score)
elif (score >= 60 and score< 70):
    print("You got B", score)
elif (score >= 50 and score < 60):
    print("You got C", score)
elif (score >= 40 and score< 50): 
    print("You got D", score)
elif (score >= 35 and score <40):
    print("You got", score)
elif(score >=0 and score < 35):
    print("You got F", score)
else :
    print("invalid")