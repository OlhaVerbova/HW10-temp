from notebook import AddressBook
from notebook import Record
from command import bot_operation
from parser_1 import command_recognizer
import command

stop_words = ["good bye", "close", "exit"]

def main():    
    command.command_word = ""
    while command.command_word not in stop_words:
        command.command_word = input("Enter the command: ").lower() # The bot is not sensitive to the case of the entered commands
        temp_run = command_recognizer(command.command_word)
        for i in range(len(temp_run)):
            if bot_operation(temp_run[i]) != None:
                print(bot_operation(temp_run[i]))
            else:
                continue
if __name__ == "__main__":
    main()