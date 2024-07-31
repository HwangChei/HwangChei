print("Quiz")


def start():    
    play=input("Do you want to play??? ")
    if play !="yes":
        quit()
    strt=input("Type Start to proceed: ")
    if strt !="Start":
        quit()


def quiz():
    count=0
    print("Starting...")
    answer=input("What country has the highest life expectancy?\n 1.Hong Kong \n 2.India \n 3.Japan \n 4.Korea\n:")
    if answer == "1":
        print("correct")
        count+=1
    else:
        print("incorrect")        
    answer=input("Full form of CPU? \n 1.Calu Po Unit \n 2.Central Processing Unit \n 3.Cell Pres Unit \n 4.Cow Pass Urine\n:")            
    if answer == "2":
        print("correct")
        count+=1
    else:
        print("incorrect")  
    answer=input("What’s the national flower of Japan??\n 1.Tulip \n 2.Sunflower \n 3.Strawberry \n 4.Cherry Blossoms\n:")
    if answer == "4":
        print("correct")
        count+=1
    else:
        print("incorrect") 
    answer=input("Where is Billie Eilish from?\n 1.California \n 2.Los Angeles \n 3.Okawa \n 4.Pennsylvania\n:")
    if answer == "2":
        print("correct")
        count+=1   
    else:
        print("incorrect") 
    answer=input("What was the most-watched series on Netflix in 2019? \n 1.Doraemon \n 2.Big Bang Theory \n 3.Peaky Blinders \n 4.Stranger Things\n:")
    if answer == "4":
        print("correct")
        count+=1   
    else:
        print("incorrect")
    if count ==5:
        print("Congratulations you got all Correct 5/5")
    else:                                   
        print(f"This is the end of your quiz!!You got {count}/5 correct!!!")  


start()
quiz()
