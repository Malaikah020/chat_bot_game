from filereader import QuestionFileReader

import random

# EscapeBot class.
class EscapeBot(QuestionFileReader):
    
    # store questions as a class variable to have as a default
    # questions = {
    #     1: 
    #         {
    #             'question': 'what value is stored in c1 when the following code is executed?', 
    #             'stimulus': 'c1 = (2 * 3) - 3 * (10 - 9)', 
    #             'answers': ['3', '-12', '12', '10']
    #         }, 
    #     2: 
    #         {
    #             'question': 'what variable type is stored inside c2 when the code below is executed?', 
    #             'stimulus': 'c2 = int((str(c1) + str(c1**c1**c1))[::c1])', 
    #             'answers': ['int', 'list', 'str', 'float']
    #         }, 
    #     3: 
    #         {
    #             'question': 'what value is stored inside c2 when the code below is executed?', 
    #             'stimulus': 'c2 = int((str(c1) + str(c1**c1**c1))[::c1])', 
    #             'answers': ['32988', '3', '376', '25597']}, 
    #     4: 
    #         {
    #             'question': 'c3 holds the value to obtain the key to open the safe! When executed c3 should hold the int value of 88. What operators should be replaced by the OP characters to receive this value?', 
    #             'stimulus': 'c2 OP 10000 OP 1000 OP 100', 
    #             'answers': ['%', '/', '*', '+']
    #         }, 
    #     5: 
    #         {
    #             'question': 'The code needed to open the safe with the key is stored in the variable c4! What value is storied in c4 when the code is executed?', 
    #             'stimulus': 'c4 = int(str((c3*c3%1000)+29234)[::-1])', 
    #             'answers': ['87992', '29978', '5787', '5282']
    #         }
        
    #     }
    
    
    
    
    "-----------------------------------------------------------------------------------------------"
    # feature 1
    
    questions = {}
     
    def newo(self,filer = "no"):
        '''this is a child class function that that inherits the parent class method randomising dictionary to give the bot instance a new value from a 
        file instead of hard codding it'''
        # i want it to even work if an error occurs with a default text file
        try:
            # make sure the file name is string which is most likely will be because input returns string
            filer = str(filer)
            # this is just parameter checker so to know if it is a text file or not
            end = filer[:-4]
            # if they don't have a file in mind it would use the default one
            if filer == "no":
                # create an instance from parent plass in child class
                file1 = QuestionFileReader("python-game-file.txt")
                # reassign instance variable to a random dictionary order from the parent class method
                self.questions = file1.random_dictionary_questions()
            # if the file is a string with txt then reassin the instance variable to the file you want with the same method
            # but it not ending correct it should go to default
            else:
                if end == ".txt":
                    file1 = QuestionFileReader(filer)
                    self.questions = file1.random_dictionary_questions()
                else:
                    file1 = QuestionFileReader("python-game-file.txt")
                    self.questions = file1.random_dictionary_questions()
        except:
            file1 = QuestionFileReader("python-game-file.txt")
            self.questions = file1.random_dictionary_questions()

    "-----------------------------------------------------------------------------------------------"




    def __init__(self, BotName):
        ''' create an instance with __init'''
        # name is a instance variable so you can alter the name if you want
        self.name = BotName
        # position is a instance variable to beable to reuse it and add to it
        self.position = 1
        # goodbye is a instance variable to be able to change goodbye message and be able to reuse it
        self.goodbye = "Thank you for playing Escape Room Game!"
        # lives is a instance variable- unable to change so user does not cheat
        self.lives = 3
        # correct answer -be able to reuse
        self.correct = "That answer was correct!"
        # incorrect anser message - to be able to reuse
        self.incorrect = "That answer was incorrect!"
        # variable for questions so now we get an option to change the file and keep it in an instance variable which we can reuse throughout the code and maybe even in a potential child classes
        self.questions = {}




    '''-----------------------------------------------------------------------------'''
    # feature 2
    
    def set_lives(self,level):
        '''set to a new number of lives related to its level'''
        # 1 is if easy
        if level == 1:
            self.lives = self.lives + 1
        # 2 is if hard
        if level == 0:
            self.lives = self.lives - 1
        # basically it will give medium
        else:
            self.lives = self.lives
        

    '''-----------------------------------------------------------------------------------'''








    # give information for the ron instance / return reader friendly information as a string
    def __str__(self):
        '''  give information for the ron instance / return reader friendly information as a string'''
        # description of the bot
        desc = "Bot Name: %s" % (self.name)
        # must return a string
        return desc
    


   
        
    





    def check_answer(self, response:str):
        '''this function takes the string input : response and checks if the response is the answer if right return
        True otherwise return False'''
        # get the correct answer from the class variable "questions" the answer would be the the first index in "answers"
        correct_answer = self.questions[self.position]["answers"][0]
        #  correct_answer is also converted to lower case :)
        correct_answer = str(correct_answer)
        correct_answer = correct_answer.lower()
        # make response lower so even if captalised it will change and so all the responses should be constant
        response = response.lower()
        # remove spaces on responses
        response = response.strip(" ")
        # use if statement to check if response and answer is the same or not
        if response  == correct_answer:
            return True
        else: 
            return False
        







    def draw(self, display:str ="happy"): 
        '''draw my bot when happy and sad this function can take a string to print the mood of the bot '''
        # use if statements to print right mood
        if display == "happy":
            print(
        "          _|\_/|_       \n",
        "       _/       \_     \n",
        "      / |       | \    \n",
        "     /  |__   __|  \   \n",
        "    |__/((o| |o))\__|  \n",
        "    |      | |      |  \n",
        "    |\     |_|     /|  \n",
        "    | \           / |  \n",
        "     \| / \___/ \ |/   \n",
        "      \ |   _   | /    \n",
        "       \_________/      \n",
        "        _|_____|_        \n",
        "   ____|_________|____   \n",
        "  /                   \  \n")
        if display == "sad":
                 print(
        "          _______       \n",
        "       _/       \_     \n",
        "      / |       | \    \n",
        "     /  |__   __|  \   \n",
        "    |__/((x| |x))\__|  \n",
        "    |      | |      |  \n",
        "    |\     |_|     /|  \n",
        "    | \           / |  \n",
        "     \| /  ___  \ |/   \n",
        "      \ | / _ \ | /    \n",
        "       \_________/      \n",
        "        _|_____|_        \n",
        "   ____|_________|____   \n",
        "  /                   \  \n")
            
 







    def display_name(self):
        '''display the name in greeting'''
        # reuse instance variables as name when make instance 
        print("Hi, my name is %s the robot!"%(self.name))

    









    def current_question(self):
        '''should return the current question and possible answers for that current question from the nested question/
        answer dictionary as a string.
        -The possible answers should be displayed in a random order. This means that you will need to use the 
            random library to navigate through the list of possible answers. '''
        # get question from the class variable
        ques = self.questions

        # use a while loop to split get the question, stimulus and answer
        quest = ques[self.position]['question']
        sti = ques[self.position]['stimulus']
        ans = ques[self.position]['answers']
       
        # open an empty string

        # randomise my answer
        ans1 = list(ans)
        random.shuffle(ans1)
        

        ans2 = ''
        # split the string and add to new line and string
        for i in ans1:
            ans2 += ' \n'+ i

        # print with other contextualise information
        print("The question is...\n",quest, "\n","->",sti,"\n","Possible answers are:\n",ans2,"\n" )
            
    









    # print insructions
    def instructions(self):
        '''print the instructions this can be reused and stored as a default'''
        # reuse name instance again
        print("Hello! My name is %s the EscapeBot! I am on a mission.\nI must retrieve the key to open this safe in front of me!\nBut only you can help me...\nYou must help me get the answers to these questions correct before I run out of lives.\nOnly then will I be able to retrieve the key to open the safe!\n "%(self.name))
    








    
    def display_lives(self):
        '''displays lives'''
        # reuse instance variables 
        print("You have",self.lives, "lives ..." )










    def increment_position(self):
        ''' increment position with each question answered correct'''
        self.position = self.position + 1
        # some element of reuse - reuse instance variables 
        # ------len of question is the same as the amount of positions
        amount_questions = len(self.questions)
        if self.position > amount_questions:
            self.position = self.position - 1
            return True
        else:
            return False

    









    def display_correct(self):
        '''display correct message'''
        print(self.correct)








    def reveal_answer(self):
        '''give the correct anser'''
        # get correct answer from 
        correct_answer = self.questions[self.position]["answers"][0]
        print("The correct answer is: %s" % correct_answer)
    







    def display_incorrect(self):
        '''message for incorrect'''
        print(self.incorrect)







    def set_questions(self, new_questions):
        '''use if statement to make sure the format is correct for new question'''
        if type(new_questions) != dict:
            print("Questions must be of type dictionary (nested). Questions not reset.")
            return
        for key in new_questions:
            if str(key).isdigit() == False:
                print("Questions are not in the correct format. Questions not reset")
                return
            else:
                keys = new_questions[key]
                if type(keys) != dict:
                    print("Questions must be of type dictionary (nested). Questions not reset.")
                    return
                if len(keys) != 3:
                    print("Questions are not in the correct format. Questions not reset")
                    return -1
                if "question" not in keys and "answers" not in keys and "stimulus" not in keys:
                    print("Questions are not in the correct format. Questions not reset")
                    return
        print("questions reset!")    
        self.questions = new_questions









    def reset(self):
        '''reset the position to be 1 again'''
        self.position = 1






    def decrement_lives(self): 
        # decremented lives
        self.lives = self.lives - 1
        # if lives run out print sad face and lost message
        if self.lives == 0:
            self.draw("sad")
            print("\n You lost!")
            
        
     




    def finished_game(self):
        '''when all questions are done print message'''
        print("All questions have now been played!")





    def terminate(self, l = 0):
        '''give goodbye message'''
        if l != 0:
            print(self.goodbye)
            print(self.terminate_message())
        else:
            print(self.goodbye)
    




    def terminate_message(self):
        '''give terminate message with bot name'''
        print("the escape game with", self.name, "has been terminated")
    


    def display_position(self):
        '''print my position'''
        print("you are now at position %s " % self.position)

    def get_Botname(self):
        '''getter for botname'''
        print(self.name)

    def set_Botname(self,new:str):
        # setting bot name with new string
        self.name = new
    
    def get_goodbye(self):
        '''getter for botname'''
        print(self.goodbye)

    def set_goodbye(self,new:str):
        # setting bot name with new string
        self.goodbye = new

    def get_lives(self):
        # getter for lives don't need a setter because i thing 3 lives is a fair game
        '''getter for botname'''
        return self.lives
    
    # properties 
    bot_prop = property(get_Botname,set_Botname)
    goodbye_prop = property(get_goodbye,set_goodbye)
    lives_prop = property(display_lives,set_lives)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
# # ------- main code section
# # call class and instant variable with the bot's name
# escape_bot = EscapeBot("Lola")
# # print the string representative for bot Ron
# print(escape_bot)

# # get instructions
# escape_bot.instructions()
# # draw bot happy
# escape_bot.draw()
# # display bot name
# escape_bot.display_name()
# # start game with false 
# in_play = False
# # to start game user must have an input y 
# user_in = input("Press Y to continue. Any other key quits the game!")
# # if they type y in play is True and game starts --must change y to lower so not case sensitive
# if user_in.lower() == "y":
#     in_play = True
# # if anything else is types game is terminated
# else:
#     print("\n"*10)
#     escape_bot.terminate()
#     escape_bot.terminate_message()
# # using while loop to play the game 
# while in_play:
#     print("\n"*10)
#     # display the position 
#     escape_bot.display_position()
#     # display the question your on
#     escape_bot.current_question()
#     # want user to answer the question
#     user_ans = input( "What is your guess? Type the full answer." )

#     # if right ---using func check_answer 
#     if escape_bot.check_answer(user_ans) == True:
#         # give a message indicating you are right
#         escape_bot.display_correct()
#         # give them an option to go to next question
#         user_in = input("Enter 'Y' to move to the next question.")
#     # if wrong   ---using func check_answer 
#     if escape_bot.check_answer(user_ans) == False:
#         # lose means lives must be decremented -lose a life
#         escape_bot.decrement_lives()
#         # display message for incorrect
#         escape_bot.display_incorrect()
#         # display now new life
#         escape_bot.display_lives()
#         # if lives have run out end game
#         if escape_bot.get_lives() == 0:
#             in_play = False
#         # if wrong give them an option to do the question again
#         user_in = input("Enter 'N' if you would like to remain at the same question position.\n")
        

# # give option to answer -check_question
#     # using if statement to check user_in
#     if user_in.lower() == "n":
#         escape_bot.display_lives()

#     elif user_in.lower() == "y":
#         # reveal the correct answer
#         escape_bot.reveal_answer()
#         # increment position
#         no_questions_left = escape_bot.increment_position()
#         # if after incrementing it is above number of question finish gane
#         if no_questions_left == True:
#             escape_bot.finished_game()
#             escape_bot.draw()
#             # if inplay false in play loop in broken
#             in_play = False
        
#     # if type other terminate your game and give message
#     else:
#         break
    
# print("\n"*5)
# # terminate the bot game -lola
# escape_bot.terminate()
# # print that you have terminated the game
# escape_bot.terminate_message()
# # reset your position at end of game
# escape_bot.reset()














# ascii face is from https://www.asciiart.eu/electronics/robotsy

