#  Creating a program capable of displaying question to the user like KBC  store the question and their correct answers. Display the final amount the person is taking home after playing the game
print("Welcome To KBC") 
id = input("Enter Your Id : ")
Pass = input("Enter Your Password : ")
user = input("Enter Your Full Name : ")
def account(win):
    acc=("Enter Your Account Number : ")
    print("Amount",win,"Transfered In account of",user,"Account No is :",acc)
if(Pass == user):
    print("\nLogin Successfully\n")
    win=0
    print("About game \n\nQue 1 for 1000\nQue 2 for 5000\nQue 3 for 10000\nQue 4 for 20000\nQue 5 for 40000\nQue 6 for 100000\nQue 7 for 200000\nQue 8 for 400000\nQue 9 for 800000\nQue 10 for 1000000")
    print("\nRules of Game:\n\t1. Each question is compulsary to attend for attending next question\n\t2. If you Entered wrong Answer then your game will be Ended\n\t3. In this game you don't have any LifeLine\n\t4. Play Carefully")
    r=input("\nAre You Ready For Play KBC\nPress R for Ready and press N for Not Ready : ")
    if(r=='R'):
        print("Good Luck\n")
        ans=input("\nQue 1 for 1000 rupees \n\nWhich is The Capital of india  \n\na. Bhopal\nb. Delhi\nc. Nagpur\nEnter Your Answer : ")
        if(ans=='b'):
            print("\nYour Choose Correct Option\n")
            win=win+1000
            ans=input("\nQue 2 for 5000 rupees \n\nWhich is The Capital of MP \n\na. Bhopal\nb. Delhi\nc. Nagpur\nEnter Your Answer : ")
            if(ans=='a'):
                print("\nYour Choose Correct Option\n")
                win=win+5000
                ans=input("\nQue 3 for 10000 rupees \n\nWho is the PM of India now\n\na. Narendra Modi\nb. Kejriwal\nc. Kamalnath\nEnter Your Answer : ")
                if(ans=='a'):
                    print("\nYour Choose Correct Option\n")
                    win=win+5000+5000
                    ans=input("\nQue 4 for 20000 rupees \n\nWhich is the Capital of Maharashtra \n\na. Goa\nb. Mumbai\nc. Delhi\nEnter Your Answer : ")
                    if(ans=='b'):
                        print("\nYour Choose Correct Option\n")
                        win=win+20000
                        ans=input("\nQue 5 for 40000 rupees \n\nSum of 1000+100+10+1 \n\na. 11110\nb. 111\nc. 1111\nEnter Your Answer : ")
                        if(ans=='c'):
                            print("\nYour Choose Correct Option\n")
                            win=win+40000
                            ans=input("\nQue 6 for 100000 rupees \n\n1000-551= \n\na.200\nb. 500\nc. 449\nEnter Your Answer : ")
                            if(ans=='c'):
                                print("\nYou Choose correct Option\n")
                                win=win+100000
                                print("Congratulation\nYou won =",win)
                                ans=input("\nQue 7 for 200000 rupees \n\nWhat is the Age for vote in India \n\na.20\nb. 18\nc. 5\nEnter Your Answer : ")
                                if(ans=='b'):
                                    print("\nYou Choose correct Option\n")
                                    win=win+200000
                                    print("Congratulation\nYou won =",win)
                                    ans=input("\nQue 8 for 400000 rupees \n\nWhat is the Formula of Calculating area of Square \n\na. side x side\nb. side x height\nc. height x height\nEnter Your Answer : ")
                                    if(ans=='a'):
                                        print("\nYou Choose correct Option\n")
                                        win=win+400000
                                        print("Congratulation\nYou won =",win)
                                        ans=input("\nQue 9 for 800000 rupees \n\ncube of 300 = \n\na. 27000000\nb. 2700000\nc. 270000000\nEnter Your Answer : ")
                                        if(ans=='a'):
                                            print("\nYou Choose correct Option\n")
                                            win=win+800000
                                            print("Congratulation\nYou won =",win)
                                            ans=input("\nQue 10 for 1000000 rupees \n\n1000-551-449+101-99= \n\na.200\nb. 50000\nc. 2\nEnter Your Answer : ")
                                            if(ans=='c'):
                                                print("\nYou Choose correct Option\n")
                                                win=win+100000
                                                print("Congratulation\nYou won =",win)
                                            else:
                                                print("\nYou Entered wrong Answer\n\nRight Answer is Option c. 2\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                                        else:
                                            print("\nYou Entered wrong Answer\n\nRight Answer is Option c. 449\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                                            
                                    else:
                                        print("\nYou Entered wrong Answer\n\nRight Answer is Option c. 449\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                                else:
                                    print("\nYou Entered wrong Answer\n\nRight Answer is Option b. 18\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                            else:
                                print("\nYou Entered wrong Answer\n\nRight Answer is Option c. 449\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                        else:
                            print("\nYou Entered wrong Answer\n\nRight Answer is Option c. 1111\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                    else:
                        print("\nYou Entered wrong Answer\n\nRight Answer is Option b. Mumbai\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
                else:
                    print("\nYou Entered wrong Answer\n\nRight Answer is Option a. Narendra Modi\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
            else:
                print("\nYou Entered wrong Answer\n\nRight Answer is Option a. Bhopal\n\nGame Over You Played Well\n\nCongratulations",user,"You won Amount is ",win)
        else:
            print("\nYou Entered wrong Answer\n\nRight Answer is Option b. Delhi\n\nGame Over You Played Well\n\nTry Again")   
    else:
        print("\nThanks for sharing your wish")
else:
    print("Wrong Id / Password \nEnter Correct Id / Password")