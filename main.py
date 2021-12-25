from bot import QuestionBot
from filereader import QuestionFileReader

############### GAME SETUP ###############

def setup():
    """Sets up the game to be played
    Asks the user if they want to play the game
    Returns:
        a boolean to be passed into the main game loop
            True if the user wants to play
            False if the user does not want to play
    Error Handling
        If the user inputs an unrecognised response, the while loop continues and asks again
    """
    # Setup initialise to True
    setup = True
    while setup:
        # User is asked if they would like to play
        user_in = input("\nWould you like to play? (y/n): type here -> ")

        # if they enter "y" lowercased or the first letter of the string is "y" (lowercased)
        if user_in.lower() == "y" or user_in[0].lower() =="y":
            # the setup function is set to False ending the loop
            setup = False
            # the True variable to be passed into play_game() is returned
            return True

        # if the user enters "n" or the first letter of the string is "n" (lowercased)
        elif user_in.lower() == "n" or user_in[0].lower() =="n": 
            # the setup function is set to False ending the loop
            setup = False
            # A friendly message is printed to the console
            print("\nThat's okay, just run this python file anytime you feel like playing")
            # and the False variable to be passed into play_game() is returned 
            return False

        # if the user inputs a string that is not recognised
        # a message is printed to the screen and the loop runs again asking for another input
        else:
            print(f"\nSorry, I don't understand '{user_in}' as a command. Have another go...")

############### MAIN PROGRAM GAME CODE ###############
def main():
    "The main code to start the game"

    # An instance of QuestionFileReader is created
    question_file_reader = QuestionFileReader('question_bank_2.txt')

    # An instance of QuestionBot is created
    bot = QuestionBot("Bottie")

    # A random set of questions is read and coverted into a form that can be used by the QuestionBot
    questions = question_file_reader.random_dictionary_questions()

    # question_bot is updated with the random set of questions
    bot.set_question(questions)

    # QuestionBot is displayed to the console
    bot.draw()

    # QuestionBots name is displayed
    bot.display_name()

    # The user is welcomed with instuctions on how to play the game
    print("Welcome to the QuestionBot game!\nIf you choose to play, you will be asked a series of questions.\nSimply type your answer into the input box and press enter")

    # The setup() function is called asking if the user wants to play
    running = setup()

    while running:
        bot.display_score()
        # calls the current question method
        current_question = bot.current_question()

        # if there are no more questions the while-loop is broken
        if current_question is None:
            # and the end the final score is displayed
            bot.final_score()
            break
        
        # otherwise, the current question is printed to the console
        print(current_question)

        # the user is asked for input, and provided with an option to quit
        user_in = input("Typing 'q' quits the program!\nTyping 'c' changes the questions\nTyping 'i' changes the score increment\nUser in: ")
        # if the user chooses to quit then the running argument is set to False
        # ending the game
        if user_in.lower() == "q":
            running = False
        # if the user choose to change the questions
        elif user_in.lower() == 'c':
            # a method is called to change the questions to new questions
            new_questions = question_file_reader.change_question_dictionary()
            bot.set_question(new_questions)
        # if the user chooses to change the score increment
        elif user_in.lower() == 'i':
            # a method is called to change the score increment
            bot.new_increment()
            # the user is asked to answer the current questions
            user_in = input("What is your answer to the current question?: ")
            # and the answer is checked
            bot.check_answer(user_in)
        else:
            # the answer provided by the user is then checked
            bot.check_answer(user_in)

    # QuestionBot wishes you goodbye
    bot.terminate_message()

# if this python file is executed...
if __name__ == "__main__":
    main()







