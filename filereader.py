from random import randint

##################### FileReader Part A - Creating a FileReader class #####################

class FileReader:

    """FileReader object reads the contents from question bank file"""

    def __init__(self, filename):
        "Instantiates filename - private, getters and setters created"
        # instance variable: allows multiple FileReaders with different questions to be instantiated
        self.__filename = filename

##################### FileReader Part B - get_line_amount #####################

    def get_line_amount(self):
        """Returns:
            the number of lines in the file (int)
        """
        # use with open to open the file in read only mode
        #   - with open automatically closes the file after use
        #   - saves the contents to the 'file' variable
        with open(self.__filename, 'r') as file:
        # the readlines() method returns a list of the lines in the file
        #   - then the len function gives the length of that list
        #   - which corresponds to the number of lines in the file
            return len(file.readlines())

##################### FileReader Part C - Filename Getters and Setters #####################

    def get_file_name(self):
        "Getter for file_name"
        return self.__filename

    def set_file_name(self, name):
        "Setter for file_name"
        self.__filename = name

##################### FileReader Part D - read_file #####################

    def read_file(self):
        """Reads all lines in a file except the first line

        Returns:
            the content of the file (str)
        """
        # Opens the file as 'file'
        with open(self.__filename) as file:
            # the readlines method returns the content of the file as a list
            # using list indexing the second line going all the way to the end are selected
            # the join method joins the list items together as a string
            return "".join(file.readlines()[1:])

##################### FileReader Part E - read_random_range #####################

    def read_random_range(self):
        """Randomly selects a range of questions from the file

        Returns:
            Random range of question (str)
        """
        # Opens the file as 'file'
        with open(self.__filename) as file:
            # readlines method turns lines in file into a list
            file_lines = file.readlines()
            # start and stop variables created
            start, stop = 0, 0
            # while loop runs until two different random numbers are selected
            while start == stop:
                # a list is created using a list comprehension
                #   a random number between 1 and the number of lines (inclusive)
                #   are selected for each item in range(2) i.e [1,2]
                #   generating two random numbers in a list
                random_nums = [randint(1, self.get_line_amount()) for i in range(2)]
                # the start value is the lower of the two numbers
                start = min(random_nums)
                # the stop value is the higher of the two numbers
                stop = max(random_nums)
                # if the two numbers are different
                #   - the file_lines are returned
                #   - using list indexing the lines are selected
                #   - and the lines are joined together as a string
            return "".join(file_lines[start:stop+1])

##################### FileReader Part F - get_lines_at #####################

    def get_lines_at(self, line_nums_list):
        """Accesses specific lines in the file

        Args:
            line_nums_list (lst)

        Returns:
            lines specified in the list of numbers
        """
        # opens the file
        with open(self.__filename) as file:
            # readlines method turns lines in file into a list
            file_lines = file.readlines()
            # a list is created using a list comprehension
            #   - for each number in the list of numbers
            #   - the line at the specific index is accessed
            #   - the lines are then joined together as a string and returned
            return "".join([file_lines[num] for num in line_nums_list])

    
    # Property for filename getter and setter
    filename = property(get_file_name, set_file_name)

##################### QuestionFileReader Part A - Creating the class #####################

class QuestionFileReader(FileReader):

    """QuestionFileReader returns content in the format that the QuestionBot will understand.
    """

    def __init__(self, filename):
        super().__init__(filename)
        # the current question dictionary is stored in an instance variable
        self.__questions_dictionary = None

##################### QuestionFileReader Part B - __str__ #####################

    def __str__(self):
        "Returns the name of the file and a description of what the class does"

        return f"File being read: {self.filename}\nQuestionBotReader converts content into a form that QuestionBot can understand"

    def convert_to_nested_dictionary(self, data):
        """Converts the data into the nested dictionary that QuestionBot understands
        
        Args:
            The questions data (str)
            This method is intended to be called by either
                - all_dictionary_questions()
                - random_dictionary_questions()

        Returns:
            A nested dictionary is in the format
            {
                question_number : {
                    'question' : 'question' (str)
                    'answers' : list_of_answers (lst)
                }
            }
        """
        # splits the data on the newline character
        data_as_list = data.split('\n')
        # then for each item in the list it splits the data on the comma
        #   - stores it in the variable = data_as_list
        data_as_list = [i.split(',') for i in data_as_list]
        # a dictionary is created
        nested_dictionary = {}
        # the question number is started from 1
        question_number = 1
        # for each line in the data_as_list
        #   - the question_number is the key
        #   - then the value is a dictionary
        #   - within the dictionary there are question and answers keys
        #   - the question is always the second item in the list
        #   - the answers are the third item in the list and everything until the end
        for line in data_as_list:
            nested_dictionary[question_number] = {
                'question' : line[1],
                'answers' : line[2:]
            }
            # the question number is then incremented by 1
            question_number += 1
        # once the for-loop ends the nested dictionary is returned
        return nested_dictionary

##################### QuestionFileReader Part C - all_dictionary_questions #################

    def all_dictionary_questions(self):
        """Returns all the questions and answers in a format QuestionBot understands 

        Returns:
            Questions and answers (Nested Dictionary)
        """
        # the read_file method is called and the data is stored in a variable
        data = self.read_file()
        # data is then passed into the method to convert the data into a nested dictionary
        all_questions = self.convert_to_nested_dictionary(data)
        # the questions dictionary is stored in the instance variable
        self.__questions_dictionary = all_questions
        # and the the questions dictionary is returned
        return all_questions
        
##################### QuestionFileReader Part D - random_dictionary_questions ##############

    def random_dictionary_questions(self):
        """Returns a random range of the questions and answers in a format QuestionBot understands
        
        Returns:
            Questions and answers (Nested Dictionary) 
            """
        # the read random range method is called and the data is stored in a variable
        data = self.read_random_range()
        #   - the newline character is removed
        if data.endswith('\n'):
            data = data[:-1]
        # data is then passed into the method to convert the data into a nested dictionary
        random_questions = self.convert_to_nested_dictionary(data)
        # the questions dictionary is stored in the instance variable
        self.__questions_dictionary = random_questions
        # and the the questions dictionary is returned
        return random_questions

    def change_question_dictionary(self):
        """Updates the nested dictionary to use new questions and answers"""
        # the current questions are retrieved from the instance variable
        current_dictionary = self.__questions_dictionary
        # a list comprehension is used to extract the questions from the current questions
        list_of_questions = [value["question"] for value in current_dictionary.values()]

        # a new nested dictionary of random questions is created
        random_questions = self.random_dictionary_questions()

        new_questions_dictionary = {}
        key = 1
        # for each for the values in the new random questions dictionary
        for questions_answers in random_questions.values():
            # if the question is not in the list of current questions
            # the question and answers are added to the new dictionary
            if questions_answers["question"] not in list_of_questions:
                new_questions_dictionary[key] = questions_answers
                key += 1 # and the key is incremented by 1
        # using truthy and falsy values 
        # the dictionary is checked to see if it is empty using truthy and falsy values
        if new_questions_dictionary:
            # the instance variable with the new questions in updated
            self.__questions_dictionary = new_questions_dictionary 
            # and the new dictionary is returned
            return new_questions_dictionary
        # if the new dictionary is empty, then the method is called again
        self.change_question_dictionary()
