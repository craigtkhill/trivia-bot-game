# Shuffle method imported to shuffle the possible answers
from random import randint, sample


class Bot:
    "An Object to represent a general Bot class"

        # Class variable storing Bots appearance
        # Made with the help of https://manytools.org/hacker-tools/convert-images-to-ascii-art/ki
        # and http://www.clker.com/cliparts/Q/3/f/L/3/n/cartoon-robot-hi.png
    display = ['                             @@                             ',
 '                           @#####                           ',
 '                            %%%%@                           ',
 '                             %%/                            ',
 '                            %%%%                            ',
 '               .............%%%%,.............              ',
 '               %.*******  (*******   #****(((%              ',
 '            %%%%.***** @@@   ***.@@@   ***(((%%%%           ',
 '            %**%******@@@@  *****@@@@ .***(((%**#           ',
 '            %/%%%%%***********************%&&&&*#           ',
 '              #*************************#((((((,            ',
 '              #.*************************((((((,            ',
 '              #*************************(((((((,            ',
 '                %%%%%/   #**********%  #%%%%%               ',
 '              /%%%%/#%%%%%%%%%%%%%%%%%%%%*%%%%              ',
 '              %%%%%/%   (                *%%%%%             ',
 '            ,%%%%%%/%  / (       (( (    *%%%%%%            ',
 '           %%%%%%  /%,,            (     *. %%%%%#          ',
 '          %%%%%    /%        .           *.   %%%%%         ',
 '        %%%%%%     /(%%%%%%%%%%%%%%%%%%%%*.    %%%%%%       ',
 '   %%%%%%%%%%      /*%%#**/////////**(%%#*.     %%%%%%%%%%  ',
 ' %%%%%%%%%%        /**********************.       %%%%%%%%%%',
 '%%%%  ,%%%%           *.*****((#(*****..*         %%%%   %%%',
 ' %  /%%%%             %#######%%((((((*%            %%%%   %',
 '                      %..****(%%((((((*%                    ',
 '                      (.*****((#(*****..                    ',
 '                    (%/*//#%#((#(#%/****/%                  ',
 '                 *************((/***********,%              ',
 '               ,********//(((((#(((((///******%  ']

    def __init__(self, bot_name):
        self.__name = bot_name

    def __str__(self):
        """Returns: Bots name and a description of what the class does"""

        return f"Bot Name: {self.__name}\nCreates an instance of a general bot class"

    def display_name(self):
        """Prints: Bots name to the console
        """  
        print(f"Hi! I'm {self.__name} the Robot!")

    def draw(self, display=display):
        """Draws Bot to the console
        Args:
            list of strings representing the Bots appearance.
        Prints:
            Bot appearance to the console
        """
        for line in display:
            print(line)

    def get_name(self):
        """Returns: Bots name"""
        return self.__name

    def set_name(self, new_name):
        """Args:
            New name (str)
        Sets:
            A new name for the Bot
        """
        self.__name = new_name

    # Property for name
    name = property(get_name,set_name)
        

class QuestionBot(Bot):
    """An object to represent QuestionBot"""

    # Class variable storing Bots appearance
    # Made with the help of https://manytools.org/hacker-tools/convert-images-to-ascii-art/
    # and https://cdn4.iconfinder.com/data/icons/robot-avatars-flat/60/040_-_Question_Bot-512.png
    display = ['                             @@                             ',
 '                           @#####                           ',
 '                       *(((((((((((((,                       ',
 '                   ((((((,,,,,,,,,((((((                   ',
 '                 ((((,,,,,,&&&&&,,,,,*((((               ',
 '               .(((((,,,,,@&,,,,,&&,,,,,((((( ,.              ',
 '            %(((((,,,,,*&,,,,,,&&/,,,,,((((((%%            ',
 '           %%%((((*,,,,,,,,,,,&&&,,,,,,,(((((,%%%         ',
 '         %%%%%#(((((,,,,,,,,,#&(,,,,,,,,,(((((#%%%%          ',
 '         (%%%%#((((((,,,,,,,,,,,,,,,,,,,((((((#%%%%           ',
 '          %%%%#(((((((*,,,,,,,##,,,,,,((((((((#%%%             ',
 '           %#(((((((((((,,,,,,,,,(((((((((((#%%%            ',
 '              (((((((((((((((((((((((((((((((            ',
 '                %%%%%/   #**********%  #%%%%%               ',
 '              /%%%%/#%%%%%%%%%%%%%%%%%%%%*%%%%              ',
 '              %%%%%/%   (                *%%%%%             ',
 '            ,%%%%%%/%  / (       (( (    *%%%%%%            ',
 '           %%%%%%  /%,,            (     *. %%%%%#          ',
 '          %%%%%    /%        .           *.   %%%%%         ',
 '        %%%%%%     /(%%%%%%%%%%%%%%%%%%%%*.    %%%%%%       ',
 '   %%%%%%%%%%      /*%%#**/////////**(%%#*.     %%%%%%%%%%  ',
 ' %%%%%%%%%%        /**********************.       %%%%%%%%%%',
 '%%%%  ,%%%%           *.*****((#(*****..*         %%%%   %%%',
 ' %  /%%%%             %#######%%((((((*%            %%%%   %',
 '                      %..****(%%((((((*%                    ',
 '                      (.*****((#(*****..                    ',
 '                    (%/*//#%#((#(#%/****/%                  ',
 '                 *************((/***********,%              ',
 '               ,********//(((((#(((((///******%  ']

    # Class variable storing QuestionBots default questions
    questions = { 1: {
        "question": "Which countries do cities of Perth, Adelade & Brisbane belong to?",
        "answers": ['Australia', 'Austria','USA','Finland']
    },
    2: {
        "question": "How many languages are written from right to left?",
        "answers": ["12","11","3","4"]
    },
    3: {
        "question": "How long is an Olympic swimming pool (in metres)?",
        "answers": ["50 metres","40 metres","80 metres","30 metres"]
    },
    4: {
        "question": "From which country does Gouda cheese originate?",
        "answers": ["Netherlands","Belgium","France","Germany"]
    },
    5: {
        "question": "What was the first soft drink in space?",
        "answers": ["Coca Cola","7up","Fanta","Pepsi"]
    }
}
    
    def __init__(self, bot_name, questions=questions):
        super().__init__(bot_name)
        """Initializes QuestionBot with a name and questions"""

        # Name of the QuestionBot
        # Private because getter and setter methods provided
        self.__name = bot_name
        
        # Questions & answers stored in a nested dictionary
        # Don't need to be accessible outside of class, set questions method provided
        self.__questions = questions
        
        # Total Number of questions
        # Don't want it changed outside of class as the
        # number of questions should be determined by the questions passed into QuestionBot 
        self.__number_of_questions = len(self.__questions)
        
        # Current question number
        # Don't want it changed outside of class as a reset method is provided
        self.__question_number = 0 
        
        # Current correct answer
        # Don't want it changed outside of class as this should not be changed at all
        self.__correct_answer = ''

        self.__correct_number_of_answers = 0
        
        # Total number of correct answers
        # Don't want it changed outside of class as it is determined by how the user plays the game
        self.__score = 0

        # Value by which the score is incremented
        # Don't want it changed outside of class as it is determined by how the user plays the game
        self.__score_increment = 1
        
        # All possible answers of the current question
        # Don't want it changed outside of class as they should not be changed
        self.__answers = []
        
        # Goodbye message displayed on ending the program
        # Getters and setters provided for goodbye message
        self.__goodbye_message = "Thank you for playing, QuestionBot is now terminating, have a good day...goodbye!"
        

    def __str__(self):
        "Returns: QuestionBots name, number of questions and current question number"
        return f"QuestionBot Name: {self.__name}\nTotal Number of Questions Loaded: {self.__number_of_questions}\nCurrent Question {self.__question_number}"

    def draw(self, display=display):
        """Draws QuestionBot to console window
        Args:
            list of strings
        Prints:
            QuestionsBots appearance to the console
        """
        for line in display:
            print(line)

    def display_name(self):
        "Prints QuestionBots name to the console"   
        print(f"Hi! I'm {self.__name} your QuestionBot host!")

    def increment_score(self):
        "Increments score by 1 when question is correct"
        self.__score += self.__score_increment

    def new_increment(self):
        """Updates the new increment score by a random number between number of questions 
         and the current score"""
        # if the current score increment is equal to the number of questions,
        # then a random number between that number and itself squared is selected
        
        if self.__score == self.__number_of_questions:
            self.__score_increment = randint(self.__score, self.__score*2)

        # otherwise a random number between the current score and the number of questions is generated
        elif self.__number_of_questions > self.__score:
            self.__score_increment = randint(self.__score,self.__number_of_questions)
        else:
            self.__score_increment = randint(self.__number_of_questions, self.__score)
        # if by chance the score increment returns 0 or 1, then the score increment is set to 2
        if self.__score_increment <= 1:
            self.__score_increment = 2
        # the current score is updated to the account for the new increment
        self.__score =  (self.__correct_number_of_answers * self.__score_increment)
        print(f"The new score increment is {self.increment}")

    def get_score_increment(self):
        return self.__score_increment

    def display_score(self):
        print(f"Your current score is {self.__score}")

    def display_correct(self):
        "Displays to the user that they got the correct answer on the console"
        print("\nThat is the correct answer!")

    def display_incorrect(self):
        """Displays to the user that they got the incorrect answer on the console
        The correct answer is provided.
        """
        print(f"\nsorry, that is incorrect. The correct answer is {self.__correct_answer}")

    def current_question(self):
        """Updates the current answers instance variable (lst)
        Updates the current correct answer intance variable (str)
        
        Returns:
            The current question and possible answers
        """
        # increment the current question number by 1 (starts at 0)
        self.__question_number += 1

        # check if the current question number is greater than the total number of questions
        if self.__question_number > self.__number_of_questions:
            # If the current question number excedes the total number of questions
            # Then the main game loop is set to false ending the program
            return None
        # if the current question does not excede the total number of questions
        # A new variable is created called question_answer_dict
        """
        The current question number accesses dictionary of the current question 
        .i.e if question_number == 1 then this dictionary is saved
        -> {
            "question": "Which countries do cities of Perth, Adelade & Brisbane belong to?",
            "answers": ['Australia', 'Austria','USA','Finland']
        },
        """

        # Then the 'question' key accesses the question as a string 
        # and stores it in question_answer_dict
        question_answer_dict = self.__questions[self.__question_number]

        # the 'questions' key accesses the question string
        question = question_answer_dict['question']
        # and the 'answers' key accesses the list of possible answers
        answers = question_answer_dict['answers']

        # the list of answers are stored as a instance variable 
        # so they are accessible outside the method
        self.__answers = answers

        # the answers are then shuffled using the sample method to randomise the order
        # without chaning the original list
        shuffled_answers = sample(answers, len(answers))
        # If it is the first question then a custom first message is saved in a variable

        if self.__question_number == 1:
            custom_message = "First question"
        # If it is the last question then a custom last message is saved in a variable
        elif self.__question_number == self.__number_of_questions:
            custom_message = "Last question"
        # Otherwise then a standard message is saved in a variable
        else:
            custom_message = "Next question"

        # The enumerate function returns a enumerate object with the number 
        # (starting at 1) stored in i and the answer. 
        # A list of strings is created for each number (i) and corresponding answer
        # The join method then joins the strings into a formatted answer
        
        formatted_answers = "".join(
            f"{i}. {shuffled_answers}\n" for i, shuffled_answers in enumerate(shuffled_answers, start=1)
        )

        # The custom question message, 
        # the question 
        # and the possible answers are returned using an f-string literal
        return f"\n{custom_message}:\n{question}\n\nThe possible answers are...\n" + formatted_answers


    def check_answer(self, response):
        """Calls display_correct() if the response matches the correct answer
            Returns: True
        Calls display_incorrect() if the response does not match the correct answer
            Returns: False
        Error Handling:
            If the user inputs an answer that is not in the list the method is called again
        with a new input from the user
        """
        # the correct answer (at index position 0) is stored as an instance variable 
        self.__correct_answer = self.__answers[0]
        
        # The answer is transformed into lowercase a stripped of any whitespace
        answer = response.lower().strip()

        # If the user inputs "q" then the main game loop is set to False ending the program
        if answer == "q":
            return False
        # if the answer is not in the list of possible answers 
        # (stored in an instance variable)
        # then a message is displayed to the console 
        # and the user is invited to make another response
        # A list comprehension is used to make a temporary list 

        elif answer not in [ans.lower() for ans in self.__answers]:
            print(f"{response} is not one of the possible answers, perhaps you made a typo. ")
            response = input("Have another go... ")
            # The method is called again with the new response
            # This code loops until the user inputs an answer from the list 
            # or quits the program
            self.check_answer(response)

        # if the user gets the correct answer
        elif answer == self.__correct_answer.lower():
            # update the correct number of answers
            self.__correct_number_of_answers += 1
            # then the number of correct answers instance variable is increased by 1
            self.increment_score()
            # the display_correct() method is called printing to the console
            # that the user got the correct answer
            self.display_correct()
            return True

        else:
            # if the answer is in the list of possible answer but not the correct answer
            # then the display_incorrect() method is called printing to the console
            # that the user got an incorrect answer | the correct answer is displayed
            self.display_incorrect()
            return False

    def set_question(self, new_questions):
        """
        Checks to see if new_questions are in the correct format
        Resets the question number to 0
        Resets the score to 0
        Sets new questions passed in the nested dictionary format
        """
        # checks to see if the new questions are in the right format
        # by calling the check_question_format method
        if self.check_question_format(new_questions) == True:
            # reset questions and set current question position back to 1
            self.__question_number = 0
            # sets new questions to the questions instance variable
            self.__questions = new_questions
            # updates the number of questions
            self.__number_of_questions = len(new_questions)
            # resets the score to 0
            self.__score = 0

    def check_question_format(self, questions):
        """
        Returns: 
            Whether the questions are in the right format (bool)
            and prints a helpful message to the console if False
        """
        # checks to see if the questions are contained in a dictionary using ininstance()
        if isinstance(questions, dict) == False:
            # if the questions are not in a dictionary a message is printed to the console
            print(f"This is not a dictionary: Got type {type(questions)} instead")
            # and the value of false is returned
            return False

        # Uses a for loop to go through the keys in the first dictionary
        for question_number in questions:
            # checks to see if the key is of type int using isinstance
            if isinstance(question_number, int) == False:
                print(f"The key should be an integer: Got '{question_number}' of type {type(question_number)} instead")
                return False

        # A for-loop checks to see if the values contained in the dictionary are also dictionarys 
        # i.e a nested for loop
        for nested_dictionary in questions.values():
            if isinstance(nested_dictionary, dict) == False:
                print(f"The value of the questions should be in a dictionary format: Got '{nested_dictionary}' of type {type(nested_dictionary)} instead")
                return False

            # while in the same for-loop other checks are made
            # if the string 'question' does not appear in the keys of the nested dictionary
            # then a message is printed and the value of False returned
            if 'question' not in nested_dictionary.keys():
                print(f"The nested dictionary should contain a key 'question' as a string: Got {nested_dictionary.keys()} instead")
                return False

            # The 'answers' key is similarly checked
            if 'answers' not in nested_dictionary.keys():
                print(f"The nested dictionary should contain a key 'answers' as a string: Got {nested_dictionary.keys()} instead")
                return False

            # The last check makes sure the answers key in the nested for-loop is a list
            if isinstance(nested_dictionary['answers'], list) == False:
                print(f"The value of 'answers' in the nested dictionary should be of type lst: Got {type(nested_dictionary['answers'])} instead")
                return False

            # then the loop starts with the next question number 
            # until all requirements for all questions are checked
            # if there are no problems then the value of True is returned
        print("Questions successfully set")
        return True

    def reset(self):
        "Resets the question number to 0"
        self.__question_number = 0

    def terminate_message(self):
        "Displays a goodbye message to the console"
        print(self.__goodbye_message)    
        
    def get_goodbye(self):
        "Returns: goodbye message instance variable"
        return self.__goodbye_message

    def set_goodbye(self, new_message):
        """Args:
            New message (str)
        Sets: 
            A new message for the goodbye message instance variable"""
        self.__goodbye_message = new_message

    def final_score(self):
        "Prints: the total correct answers out of the total answers (str)"
        # number of correct answers stored in score
        score = self.__score
        # total number of questions stored in total and takes into account
        # new score increments
        total = self.__number_of_questions * self.__score_increment
        print(f"\nYour final score is {score} out of {total}")


    goodbye = property(get_goodbye, set_goodbye)

    increment = property(get_score_increment)