
# kon_banega_karodpati
# print("WELCOME TO KBC")
# print("per question is 2000 rupeese")
# print()
# print("...........KON BANEGA CRORPATI................")
# print()
# questions=[["Q1.How many continents are there?"],              
#             ["Q2.What is the capital of India?"],            
#             ["Q3.NG mei kaun se course padhaya jaata hai?"]]
# option=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#         ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#         ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
# solution=[3,4,1]
# i=0
# while i<len(questions):
#     print(questions[i])
#     j=0
#     while j<len(option):
#         print(option[i][j])
#         j=j+1
#     num=int(input("enter the answer"))
#     if num==solution[i]:
#         print("your answer is right")
#         print("you win 2000 rupeese")
#     else:
#         print("game quite")
#         i=i+1

# print("WELCOME TO KBC")
# print("per question is 2000 rupeese")
# print()
# print("...........KON BANEGA CRORPATI................")
# print()
# questions=[["Q1.How many continents are there?"],              
#             ["Q2.What is the capital of India?"],            
#             ["Q3.NG mei kaun se course padhaya jaata hai?"]]
# option=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#         ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#         ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
# solution=[3,4,1]
# answer=["3.seven","4.eight","3.chennai","4.delhi","1.Software Engineering","2.Counseling"]
# i=0
# a=1
# b=0
# count=0
# amount=2000
# while i<len(questions):
#     print(questions[i])
#     j=0
#     k=1
#     while j<len(option[i]):
#         print(option[i][j])
#         j=j+1
#     lifeline=input("do you want 50 50 lifeline")
#     if lifeline=="yes":
#         print("50 50 lifeline ")
#         if count==0:
#             print(answer[b+i])
#             print(answer[b+a])
#             num=int(input("enter the answer"))
#             if num==solution[i]:
#                 print("your answer is right")
#                 print(amount)
#                 print()
#             else:
#                 print("your answer is wrong")
#                 print("you looes the game")
#                 break
#             count=count+1
#             print()
#         else:
#             print("you already used lifeline")
#             e=int(input("enter the answer"))
#             if e==solution[i]:
#                 print("your answer is right")
#                 print(amount)
#             else:
#                 print("your answer is wrong")
#                 print("you looes the game")
#                 break 
#     else:
#         f=int(input("enter the answer"))
#         if f==solution[i]:
#             print("your answer is right")
#             print(amount)
#         else:
#             print("your answer is wrong")
#             print("you looes the game")
#             break
#         amount=amount+4000
#     i=i+1
#     a=a+1
#     b=b+1
# print("you won",amount)
# print("thank you for playing")
            