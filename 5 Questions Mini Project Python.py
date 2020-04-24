print('hello, welcome to my quiz')

ans = input('Are you ready to play 5 Questions? (yes/no): ')
score = 0
total_q = 2


if ans.lower() == 'yes':
    ans = input(' 1. What did I major in? ')
    if ans.lower() == "finance": 
        score +=1
        print('Correct')
    else:
        print('Incorrect')

    ans = input(' 1. What is my last name? ')
    if ans.lower() == "rodriguez": 
        score +=1
        print('Correct')
    else:
        print('Incorrect')



print('Thank you for playing you go',score, "questions correct.")
        
        
Tscore = (score/total_q) * 100
print(" Total Score", Tscore)
print( " Bye Bye")
