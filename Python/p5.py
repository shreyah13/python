# Accept average score from the student of his exam and print his result as follows: 0-49:Fail, 50-74:Second Class, 75-90: First Class, 91-100:Distinction. Also check for invalid score.

avg_score = int(input('Enter your gross average score: '))
print('RESULT')
if avg_score >=75 and avg_score <= 90:
    print('Good job! You have passed with First Class!')
elif avg_score >= 91 and avg_score <= 100:
    print('Congratulations! You have passed with Distinction!')
elif avg_score >= 50 and avg_score <= 74:
    print('You have passed with Second Class!')
elif avg_score >= 0 and avg_score <= 49:
    print('You have Failed!')
else:
    print('Invaild input')