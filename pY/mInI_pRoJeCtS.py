#Grade calculator
while True:

 studentName=input('Hello,what is your name?')
 studentScore=int(input('what is your score?'))
 if studentScore>=89:
    print('congratulations',studentName,'you got an A!')
 elif studentScore>=79:
    print('congratulations',studentName,'you got a B!') 
 elif studentScore>=69:
    print('congratulations',studentName,'you got a C!')
 elif studentScore>=59:
    print('congratulations',studentName,'you got a D!')
 elif studentScore<=49: 
     print('sorry',studentName,'you got an F!')
 else:
     print('invalid score')
 break
#personal expense tracker
userName=input('Hello,what is your name?')
userExpenses=input({'enter your expenses'})
print=(userName', these are your expenses for today')
