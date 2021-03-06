import random
import re
import json
import datetime 

def sample_page():
    import SamplePage


#FEATURE Calculate and display data based on an external factor...SEE ALSO def christmas_greeting
from datetime import date, time, datetime
date_format = "%m/%d/"
now = datetime.now()
christmas = datetime(now.year, 12, 25)
delta = christmas - now
final = delta.days

today = date.today()

#FEATURE Create and call at least 3 functions, ..."Return" is found on the SamplePage
def christmas_greeting():
    if final > 0:
        print(final, "days until Christmas!")
    elif final == 0:
        print ("Merry Christmas!")
    elif final < 0:
        print ("I hope you had a great Christmas.  Have a Happy New Year. \n")

       
#FEATURE: Implement a log that records ... and writes them to a text file
#save the answer into a text file
def quiz_answer(answer):
    with open("answers.txt", "a") as file:
        file.write(answer+"\n")

def show():
    with open("answers.txt") as file:
        for line in file:
            print(line)
            
if __name__ =='__main__':
    quiz_answer(input("How are you today? ")) #Need to add answer to the end of the list???

#Collect user's infomation  
def user_info():
    user_name = input("What is your name? (First + Last)").title()
    print("Hello ", user_name, ". \n")
    christmas_greeting()
    user_phone = input("What is your phone number? (###-###-####)")
    regex= "\w{3}-\w{3}-\w{4}"

    if re.search(regex, user_phone):
        print("Valid phone number: You entered:",user_phone," ")
    else:
        print("Invalid phone number")
        user_info()
    
    travel_distance = input("How many miles do you travel to work or school? (miles) ")
    weight = input("What is your ideal weight? ")  #OK,...not so politically correct, but for educational purposes.
    #FEATURE Build a conversion tool that converts user input to another type ...
    travel_distance = int(travel_distance)
    km_travel_distance = round((travel_distance/0.62137119), 2)
    weight = int(weight)
    kg_weight = round((weight * 0.453592), 1)
    print("You travel",travel_distance,"miles, which is", km_travel_distance, "kilometers.")
    print("Your ideal weight is",weight, "pounds, which is equal to",kg_weight, "kilograms.")
    main_menu()

#FEATURE: Implement a "master loop" console ...
#Create Main Menu to chose to play or to exit

def opening_menu():
    print("Welcome Visiter \n")
    print("Today is ",today) 
    print(" ")
    user_info_request = input("Would you like to tell us about yourself? Y/N ").lower()
    if user_info_request == "y":
        user_info()
    else:
        print("Enjoy your visit. \n")
        main_menu()

def main_menu():
    print("**************************************")
    print("Welcome to the Main Menu")
    print("------------------------")
    print("Please select an option below.")
    print("1. Answer World Statistics Questions")
    #option to play a game feature
    print("2. Play Pong Game")
    print("3. Choose Your own adventure Game ")
    print("4. Test some Sample Python code ")
    print("h. Go to Help Screen ")
    print("Enter 0 to Exit the Program")
    choice = input("\n Enter 1, 2, 3, h, or 0: ").lower()
    if choice == "1":
        world_stat_quiz()
    elif choice =="2":
        print("*** Sorry, that feature is not complete yet. \n")
        main_menu() 
    elif choice =="3":
        print("*** Sorry, that feature is not complete yet. \n")
        main_menu()
    elif choice =="4":
        sample_page()
    elif choice =="h":
        help_screen()                      
    elif choice == "0":
        print("\n Thanks for visiting \n")
        quit()

#Questions for our test

def world_stat_quiz():
    score = 0  
    count = 5 #this is the number of questions in the quiz.  
    print("\nAccording to the United Nations: ... ") 
    
    # Ask question
    answer1 = input("\n What is the percent of the world's population that has access to electricity? \n a. 20% \n b. 50% \n c. 80% \n \n Answer: ").lower() #c
    '''#for loop to check for valid answer
    if answer1 != "a" or "b" or "c":
        print("Your answer has been tallied.")
    else:
        answer1 = input("That is not a valid answer, please re-enter your answer a, b, or c: ").lower()
    '''
    if answer1 == "c":
        score += 1

    answer2 = input("\n In all low income countries, how many girls finish primary school? \n a. 10% \n b. 40% \n c. 60% \n \n Answer: ").lower() #c
    if answer2 == "c":
        score += 1

    answer3 = input("\n Were does the majority of the world's population live? \n a. In Low Income Countries \n b. In Middle Income Countries \n c. In High Income Countries \n \n Answer: ").lower() #b
    if answer3 == "b":
        score += 1

    answer4 = input("\n In the last twenty (20) years, the proportion of the world's population that lives in extreme poverty has...? \n a. almost doubled \n b. remained approximately the same \n c. almost dropped by half. \n \n Answer: ").lower() #c
    if answer4 == "c":
        score += 1

    answer5 = input("\n What is the life expectancy of the world today? \n a. 50 years \n b. 60 years \n c. 70 years \n \n Answer: ").lower() #c
    if answer5 == "c":
        score += 1

    print("Your final score for the quiz is", score, "out of", count,"questions. \n")
    #calculate the percentage of correct answers =correctAnswers/totalQuestions
    score_percent = score/count*100

    #Give a score result message
    if score_percent == 100:
        print("You got a perfect score! 100% \n")
        main_menu()
    elif score_percent >= 70:
        print("You scored a ", str(score_percent), "%.  That is impressive. \n")
    elif score_percent >=33:
        print("You scored a ", str(score_percent), "%.  That is actually better than most people. \n")
    else: 
        print("You scored a ", str(score_percent), "%.  A wild chimpanzee making random guesses would likely score higher than you did. \n")
    retry = input("Would you like to re-try the quiz? Y/N ").upper()
    if retry == "Y":
        world_stat_quiz()
    else:
        results = input("Would you like to see the correct answers? Y/N ").upper()
        if results == "Y":
            #Print the answers to the questions
            print("_______________________________________________________________")
            print("80% percent of the world's population has access to electricity.")
            print("In all low income countries, 60% of girls finish primary school.")
            print("The majority of the world's population lives in Middle Income Countries.")
            print("In the last twenty (20) years, the proportion of the world's population that lives in extreme poverty has almost dropped by half.")
            print("The life expectancy of the world population today is 70 years.")
            print("_______________________________________________________________")
            main_menu()
        else:
            print("")
            main_menu()

def help_screen():
    print()
    print("#####################################")
    print("#    Welcome to the Help Screen     #")
    print('#                                   #')
    print('# Follow the on screen instructions #')
    print('#           o  o                    #')
    print('#           _ ^ _                   #')
    print('#                                   #')
    print("#####################################")
    print()
    main_menu()


opening_menu()

