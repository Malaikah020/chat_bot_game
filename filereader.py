# FileReader.py file should include the FileReader class and 
# QuestionFileReader class. 


import random
# this is the parent class which will read the a file and count lines of a file
class FileReader:
    # the only parent instant variable we need is filename because it needs it to open and close the file it is a private variable
    def __init__(self, filename):
        self.__filename = filename
        # print a message to show that an instance has been created
        print("instance of FileReader class created!")
    
    def __str__(self):
        '''  give information for the file instance / return reader friendly information as a string'''
        # description of the bot
        desc = "the file that is read to give a nested dictionary:" ,self.__filename
        # must return a string
        return desc
    
    
    def read_all(self):
        '''this class method open, closes and reads all lines in a file and returns lines as a string'''
        try:
            # open file
            file_1 = open(self.__filename)
            # read file and give it a variable to be stored in
            lines = file_1.readlines()
            # close the file after getting the lines from the file
            file_1.close()
            # return what you saved in lines
            return lines
        except:
            
            print("file not opened. Terminating method")
            return False
    # counts the lines using another parent method which will be useful in child class
    def line_count(self):
        # read file to give the file
        lines = self.read_all()
        # used the length of the file as line amount
        line_amount = len(lines)
        return line_amount  

    def get_filename(self):
        filename = self.__filename
        return filename

# read contents from a file and converts it into a specified dictionary format extend upon the FileReader class.
# This return a set of questions in a format that will eventually be readable by the EscapeBot class. .
# this class can take any amount of questions 
class QuestionFileReader(FileReader):
    # we had a child variable because we needed more instance variables that are exclusive to this class
    def __init__(self, filename):
        # we get the private variable filename using super so we get the filename
        super().__init__(filename)
        # this is an instance variable we are keeping in our child class
        self.filename = filename
        # created a instance variable because i wanted a variable to store the number of question so when i need to call it or change it, i can use it
        # reused a parent method to get number of questions
        # self.line_count() = self.line_count()
        # created a error message to be able to reuse or if i want to change the message i can
        self.error = "error has occurred"
    
    # creating a string representation containing reader-friendly information concerning the object’s instance like name of file and what class can do.
    def __str__(self):
        # print the 2 messages to give the user some background on what file is being used and what action is can take
        print("The file that is used is %"%self.filename)
        print("This class is for taking in a file and make a dictionary of question")

    
    
    def all_dictionary_questions(self) :
        '''
        this class method formats the file into a nested dictionary with question numbers and questions, stimulus and answers in a list
        this methods can not take into account the first line of the file 
        its default is not to take into account line 0 to give a functional dictionary 
       '''
        # used error handlers if something unexpected happens
    
        num_of_lines = self.line_count() -1
        num_of_lines = int(num_of_lines)
        # we use inherited parent class method read all that opens, reads ,saves and closes the file to get the information we need to make our dictionary
        var = self.read_all()
        # first pop the first line so we format from line 1
        var.pop(0)
        # use a instance variable to save the length of the file now which we will need because it is the same amount of questions that are in the dictionary
        # helps us reuse it in other class methods
        
        # questions1 dictionary is our inner dictionary that has keys of "questions","stimulus","answers"
        # questions2 dictionary is our outer dictionary that has keys as number of questions and value as inner dictionary
        # this is the format we want
        questions2 = {}
        # we will use a while loop to use for each question and for the key
        # this is the counter which is also the number of question it is
        question_num = 0
        # we reuse our class instance because we want it to be able to work 
        while question_num < num_of_lines:
            questions1 ={}
            # variable that first get the line we are one by using while loop
            lines_no = var[question_num]
            # take away \n because we don't need it in our format
            lines_no = lines_no.strip("\n")
            # split it at , because our question, sti and ans are split at them
            lines_no = lines_no.split(",")
        
            # the question will always be at index 0 of our split line list
            v_ques = lines_no[0]
            # now we put that in a dictionary with the key question
            questions1["question"] = v_ques
        
            # the stimulus will always be at 1 index 
            v_sti = lines_no[1]
            # now we add that after the question with key stimulus
            questions1["stimulus"] = v_sti
            
            # answer list is with the values at index 2,3,4,5 so we 
            ans_list = lines_no[2:]
            # now put that after stimulus follwing the format
            questions1["answers"] = ans_list
            # now move to outer dictionary, the key must be plus 1 because key must 1 when at qustion_num is 0
            questions2[int(question_num)+1] = questions1
            # before repeating the loop we must go to the next line of the file
            question_num+=1
        # after we run out of lines we return our formatted dictionary
        return questions2
    
       

# line_nums_list (list: int): an integer list, containing line numbers to obtain from the file. 
# The list may be of any length greater than or equal to 1.  
# You can assume that all line numbers in the list are contained in the file and there are no duplicate 
# line numbers listed. 
    def lines_as_dictionary(self, line_nums_list:list):
        ''' line_nums_list (list: int): an integer list, containing line numbers to obtain from the file. 
        The list can be of any length greater than or equal to 1.  
        You can assume that all line numbers in the list are contained in the file and there are no duplicate 
        line numbers listed. '''
        # error handlers
        # try:
        #     return_dict = {}
        #     # get the formatted dictionary
        #     dict_all = self.all_dictionary_questions()
        #     # so for each element in a list we want that element in that dictionary in a new dictionary
        #     for x in line_nums_list:
        #         # we all elements in the line_num_list to be above 1 or equal and less than our line_count() that saves the number of questions
        #         if x >= 1 or x<= self.line_count():
        #             # we get the value at the x which is same as the key for that question 
        #             val = dict_all.get(x)
        #             # add to dictionary that we will repeat
        #             return_dict[x] = val
        #     return return_dict
        # except:
        #     return self.error
        
    #    error handlers
        try:
            i = 1
            len_list = len(line_nums_list)
            while i <= len_list:
                return_dict = {}
                # get the formatted dictionary
                dict_all = self.all_dictionary_questions()
                # so for each element in a list we want that element in that dictionary in a new dictionary
                for x in line_nums_list:
                    # we all elements in the line_num_list to be above 1 or equal and less than our line_count() that saves the number of questions
                    if x >= 1 or x<= self.line_count():
                        # we get the value at the x which is same as the key for that question 
                        val = dict_all.get(x)
                        # add to dictionary that we will repeat
                        return_dict[i] = val
                        i+=1
            return return_dict
        except:
            return self.error
   

    def get_dictionary_range(self, ran:list) :
        '''read from a range of values (provided in ran) from the file from a given line range. It 
        returns those questions, stimuli and answers in the dictionary format. 
        one parameter, ran (list): 
 
            • contains a list of two integer values only.  
            • The first value in the list corresponds to the starting value. The last value in the list corresponds to 
                the ending value. 
            • The starting value should always be lower than the ending value. 
            • The range should be inclusive of the starting and ending value. '''
        # error handler
        try:
            # make sure ran is 2 values long and that it is a list with smallest first and larger next
            if len(ran) == 2 and type(ran) == list:
                # use sort in descending order
                ran.sort()
                
                # index 0 or ran is start and 1 is end
                start = ran[0]
                end = ran[1]
                # make sure the type of start and end is int and they are in the range we want
                if type(start) == int and type(end) == int and start >=0 and start <= self.line_count() and end >=0 and end <= self.line_count():
                    # if start is 0 it should start at 1 not 0 cause there is nothing at 0
                    if start == 0 or start == 1:
                        start = 1
                        # then use a while loop with the dictionary we get from child method all_dictionary_questions
                        return_dict = {}
                        dict_all = self.all_dictionary_questions()
                        x = start
                        # use a while loop to go from start to end
                        while x <= end:
                            # get the value at x and add them to return dictionary
                            val = dict_all.get(x)
                            return_dict[x] = val
                            x+=1
                        
                        return return_dict 
                    # if start isn't 0 then leave start and do the same but don't make start 1 
                    else:
                        # return_dict = {}
                        # dict_all = self.all_dictionary_questions()
                        # x = start
                        # j = 1
                        # endo = end+1
                        # while j <= endo:
                        #     while x <= endo:
                        #         val = dict_all.get(x)
                        #         return_dict.update({j:val})
                        #         x+=1
                        #     j+=1
                        # return return_dict
                        
                        # to make in order i changed the way i got my dictionary
                        # i added one to end because range takes the last on off
                        end = end +1
                        # made a list using range function
                        list_range = range(start, end)
                        # reused function lines_as_dictionary to get my nested ordered dictionary
                        return_dict = self.lines_as_dictionary(list_range)
                        return return_dict
                     
                # if anything is not right error message returned
                else:
                    return self.error
                
            else:
                return self.error
        except:
            self.error

        

    def random_dictionary_questions(self) :
        '''create a random dictionary with same format. 
        '''
        # error handlers
        
        # make sure l is in the range of the questions
        l = self.line_count() -1
        # use a while loop to get a list of numbers because random.sample wouldn't work because sample was too small
        num_list = []
        x = 1
        while x <= l:
            num_list.append(x)
            x+=1
        
        # # create a random list that is in the range of 1 to the l we found by using parent method
        random.shuffle(num_list)
        # # reuse child class method to get the list of questions with the random list
        l_dict = self.lines_as_dictionary(num_list)
        return l_dict
            
        
        
        
    def exclude_dictionary_questions(self, line_nums_list:list): 
        '''get a list of intergers that you want to delete from your dictionary'''
        try:
            # # reuse method to get dictionary
            # original_dict = self.all_dictionary_questions()
            # l = self.line_count()
            # # use for loop
            # for x in line_nums_list:
            #     # each element must be in the range of how many questions there are in the dictionary
            #     if x >= 1 and x <= l:
            #         # delete them by popping them
            #         original_dict.pop(x)
            # # return the dictionary you have deleted from
            # return original_dict
            
            # tried a new way reusing old class functions
            l = self.line_count() 
            # got a list of all intergers which are in order
            lister = range(1,l)
            # made sure its a list so i can use remove
            lister = list(lister)
            # nested for loops to go through both lists and remove the common ones
            for x in line_nums_list:
                for y in lister:
                    if x == y:
                        lister.remove(y)
            # after the common one removed from my basically key list which i have hard coded because i want them to be numbers and not other types of variables
            # reuse lines_as_dic.. to shorten code and ensure all values are intergers and have no value above or below the range in file
            return_dict = self.lines_as_dictionary(lister)
            # return the new dictionary also arranged in order due to the lines_dict funnction
            return return_dict
        except:
            # reuse error message
            return self.error


    def exclude_dictionary_range(self,questions_range:list): 
        '''this function excludes a range from a dictionary of questions'''
        
        # reuse parent method to make sure we are getting a non modified length of questions
        l = self.line_count()
        questions_range.sort()
        # range has to be a list and 2 long
        if len(questions_range) == 2 and type(questions_range) == list:
            # start is index 0 and end is 1
            start = questions_range[0]
            end = questions_range[1]
            # making sure the types are int and it starts after 0 and ends before
            if type(start) == int and type(end) == int and start >=0 and start <= l and end >=0 and end <= l:
                # make sure if start is 0 you make it 1 so your inclusive but actually have something at 1
                if start == 0:
                    # got a list of all intergers which are in order
                    lister = range(1,l)
                    # made sure its a list so i can use remove
                    lister = list(lister)
                    start = 1
                    x = end
                    while start <= end:
                        # delete from start to end
                        lister.remove(x)
                        x+=1
                    return_dict = self.lines_as_dictionary(lister)
                    return return_dict
                
                else:
                    # got a list of all intergers which are in order
                    lister = range(1,l)
                    # made sure its a list so i can use remove
                    lister = list(lister)
                    # if start is not 0 then don't change start
                    x = start
                    while x <= end:
                        # delete from start to end
                        lister.remove(x)
                        x+=1
                    return_dict = self.lines_as_dictionary(lister)
                    return return_dict 
            else:
                return self.error
            
        else:
            return self.error

            