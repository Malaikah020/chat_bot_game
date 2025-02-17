# a main python file to place your python code, instantiate the EscapeBot class, call its 
# methods and control the overall gameplay


from bot import EscapeBot
# ------- main code section
# call class and instant variable with the bot's name
escape_bot = EscapeBot("Lola")
# print the string representative for bot Ron
print(escape_bot)

# get instructions
escape_bot.instructions()
# draw bot happy
escape_bot.draw()
# display bot name
escape_bot.display_name()
# start game with false 
in_play = False
# to start game user must have an input y 
user_in = input("Press Y to continue. Any other key quits the game!")
# if they type y in play is True and game starts --must change y to lower so not case sensitive
if user_in.lower() == "y":
    # if they want to play ask if they want a new file of questions
    user_ques = input("Enter file name to change questions, if not enter no: ")
    if user_ques.lower() != "no":
        # use newo class function that will reassign the file name
        escape_bot.newo(user_ques)
        user_li = input("Would you like to play easy mode or medium or hard mode? Enter hard, medium or easy! ")
        level = user_li.lower()
        escape_bot.set_lives(level) 
         
        in_play = True
        
    else:
        # use newo class function that will reassign the file name to a default file name
        escape_bot.newo()
        # keep a default file for questions
        user_li = input("Would you like to play easy mode or medium or hard mode? Enter hard, medium or easy! ")
        if user_li.lower() == "easy":
            escape_bot.set_lives(1)  
            escape_bot.display_lives() 
            in_play = True
        if user_li.lower() == "hard":
            escape_bot.set_lives(0) 
            escape_bot.display_lives()  
            in_play = True
        else:
            escape_bot.set_lives("sdfghj")  
        in_play = True
                
# if anything else is types game is terminated
else:
    print("\n"*10)
    escape_bot.terminate()
    
# using while loop to play the game 
while in_play:
    print("\n"*5)
    # display the position 
    escape_bot.display_position()
    # display the question your on
    escape_bot.current_question()
    # want user to answer the question
    user_ans = input( "What is your guess? Type the full answer." )

    # if right ---using func check_answer 
    if escape_bot.check_answer(user_ans) == True:
        # give a message indicating you are right
        escape_bot.display_correct()
        # give them an option to go to next question
        user_in = "y"
    
    # if wrong   ---using func check_answer 
    if escape_bot.check_answer(user_ans) == False:
        # lose means lives must be decremented -lose a life
        escape_bot.decrement_lives()
        # display message for incorrect
        escape_bot.display_incorrect()
        # # display now new life
        # escape_bot.display_lives()
        # if lives have run out end game
        if escape_bot.get_lives() == 0:
            escape_bot.display_correct()
            in_play = False
        # if wrong give them an option to do the question again
        user_in = "n"
        

# give option to answer -check_question
    # using if statement to check user_in
    if user_in.lower() == "n":
        escape_bot.display_lives()

    elif user_in.lower() == "y":
        # reveal the correct answer
        escape_bot.reveal_answer()
        # increment position
        no_questions_left = escape_bot.increment_position()
        # if after incrementing it is above number of question finish gane
        if no_questions_left == True:
            escape_bot.finished_game()
            escape_bot.draw()
            # if inplay false in play loop in broken
            in_play = False
        
    # if type other terminate your game and give message
    else:
        break
    
print("\n"*5)
# terminate the bot game -lola
escape_bot.terminate(0)
# reset your position at end of game
escape_bot.reset()



