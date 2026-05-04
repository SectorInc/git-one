#GRADE CALCULATOR

# while True:
#  studentName=input('Hello,what is your name?')
#  studentScore=int(input('what is your score?'))
#  if studentScore>=89:
#     print('congratulations',studentName,'you got an A!')
#  elif studentScore>=79:
#     print('congratulations',studentName,'you got a B!') 
#  elif studentScore>=69:
#     print('congratulations',studentName,'you got a C!')
#  elif studentScore>=59:
#     print('congratulations',studentName,'you got a D!')
#  elif studentScore<=49: 
#      print('sorry',studentName,'you got an F!')
#  else:
#      print('invalid score')
#  break
#PERSONAL EXPENSE TRACKER

# Expenses={}
# userName=input('Hello,what is your name?')
# userExpenses=int(input('how many expenses do you have for today?'))

# for i in range(userExpenses):
#    expenseName=input(f'enter expense {i+1} : ')
#    expensePrice=int(input('enter the price of your expense : $'))
#    Expenses[expenseName]=expensePrice

# print(userName, 'these are your expenses for today',Expenses)

# totExpenses=input('do you want to see your total expenses? (y/n)')

# if totExpenses=='y':
#    print(userName, 'your total expense is : $',sum(Expenses.values()))   
# elif totExpenses=='n':  
# #    print('thank you.')

# #Contacts(name,phone number,email)
# Contacts=[]
# uName=input('Hello,what is your name?')
# contactsBook=int(input('how many contacts do you want to add?'))
# for i in range(contactsBook):
#     cName=input(f'enter contact name : ')
#     cPhone=int(input('enter contact phone number : '))
#     cEmail=input('enter contact email : ')
  
#     contact={'name':cName,'phone':cPhone,'email':cEmail}
    
#     Contacts.append(contact)

# print(uName,'these are your contacts:')
# for contact in Contacts:
#     print(contact)

# addcontact=input('do you want to add a contact? (y/n)')
# if addcontact=='y':
#     contactsBook=int(input('how many contacts do you want to add?'))
#     for i in range(contactsBook):
#         cName=input(f'enter contact name : ')
#         cPhone=int(input('enter contact phone number : '))
#         cEmail=input('enter contact email : ')
  
#     contact={'name':cName,'phone':cPhone,'email':cEmail}
    
#     Contacts.append(contact)
#     print(uName,'these are your contacts:')
#     for contact in Contacts:
#         print(contact)
# elif addcontact=='n':
#     print('thank you.')

# while a_list[4]==5: 
#       counter=0 while counter<a_list[4]: print(a_list[4]) counter+=1    

# a_list=[1,2,3,4,5]
# for i in a_list:
#     if i==2:
#         print('the value is 2')
#     else:
#         print('the value is not 2')
# if a_list[4]==5:
#     counter=0
#     while counter<=a_list[4]:
#         print('last item')
#         counter+=1     

#GUESS NUMBER GAME
        
# import random
# uName=input('Hello, what is your name?')  
# print("Hello", uName, " welcome to my guessing game!")  
# ranNum=random.randint(1,10)
# counter=0
# num=0
# while counter<5 and num!=ranNum:  
#     num=int(input("Guess a number between 1 and 10: "))
#     if num==ranNum:
#         print('you guessed right.',ranNum,' was the lucky number.')             
#     else:
#         print('the lucky number was not ',num,'. Try again.')
#     counter+=1

#     if counter==5 and num!=ranNum:
#         print('sorry, you have used all your attempts. The lucky number was ',ranNum,'. Better luck next time!')
    
#CALCULATOR

#ask user what operation he want to carry out
#ask user to enter the task he wants to do 
#ask user if he wants to end task
# while True:
#     print('1)Add 2)Subtract 3)Divide 4)Multiply 5)Exit')
#     i=input('what operation would you like to carry out?')
#     a=int(input('enter your first value:'))
#     b=int(input('enter your second value:'))
#     if i== '1':
#         print(a + b)
#     elif i == '2':
#         print(a - b)
#     elif i == '3':
#         print(a / b)
#     elif i ==  '4':
#        print(a * b)
#     elif i =='5':
#         print('End.')
#         break
#     else:
#         print('sorry mathemitacal operation not recognised. Please try again.')

#SORTING A LIST AND FINDING THE THIRD LARGEST NUMBER

# numbers=[4,6,2,10,8]
# mun=sorted(numbers)
# print(mun)
# print(numbers)
# print(mun[-3])
#FINDING ODD AND EVEN NUMBERS IN A LIST

# x=0
# num=[1,2,3,4,5,6,7,8,9,10]
# for x in num:
#     if x%2==0:
#         print(f"{x} is even")

#     else:
#         print(f"{x} is odd")

#FIND THE LEAP YEAR
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
#     print(year % 400 == 0)

#ATM WITHDRAWAL SYSTEM
users={
     '1234':2000,
     '0000':4000
}
def check_pin():
    pin=int(input('enter your pin: '))
    if pin==1234:
        return True
    else:
        print('incorrect pin. Please try again.')
        return False
def show_menu():
    print("Welcome to the ATM!")
    print("1) Withdraw 2) Balance check 3)Transfer 4)Exit")
    task=input('what task would you like to carry out?')
    return task
def withdraw(balance):
    input('enter your pin: ')
    withdrawal=int(input('enter the amount you want to withdraw: $'))
    if withdrawal>balance:
        print('insufficient funds')
        return balance
    else: 
        balance-=withdrawal
        print(f"you have withdrawn ${withdrawal}")
        return balance
def balance_check(balance):
    print(f"your balance is ${balance}")
def transfer(balance):
    transfer=int(input('enter the amount you want to transfer: $'))
    if transfer>balance:
        print('insufficient funds')
        return balance
    else:
        usertf=input("input user account number: ")
        balance-=transfer
        print(f"you have transferred ${transfer} to {usertf}")
        return balance

balance=1000
while True: 
    if check_pin():
        task=show_menu()
        if task=='1':
            withdraw(balance)
        elif task=='2':
            balance_check(balance)
        elif task=='3':
            transfer(balance)
        elif task=='4':
            print('Thank You.')    
            break
        else:
            print('invalid input. Please try again.')
            break
