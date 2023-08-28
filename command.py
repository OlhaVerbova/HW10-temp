global command_word
from notebook import AddressBook

telephone_list = {"Olha":"+380996409040"}
adress_book = AddressBook()

#decorator
def input_error(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Invalid name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "Invalid input format. Give me phone please."
        except TypeError:
            return 'Invalid command'
    return inner

# main functions
def hello():
    return "How can I help you?"

def show_all(address_book): #Ужк используем классы
    adress_info = address_book.show_all()
    result_list = list()
    for key, value in adress_info.items():
        result_list += key
        result_list += value
    return result_list


def say_good_bye():
    return "Good bye!"

@input_error
def add_new_telephone_contact(text):    
    text_list = text.split()    
    telephone_list.update({text_list[1].title():text_list[2]})    
    
@input_error
def change_phone_number(text):
    text_list = text.split()
    telephone_list[text_list[1].title()] = text_list[2] 

@input_error
def show_name_contact(text):
    text_list = text.split()
    for key, value in telephone_list.items():
        if value == text_list[1]:
            return key

def bot_operation(text):
    
    match text:
        case "hello":
            result = hello()   
                     
        case "close":
            result = say_good_bye()  

        case "good bye":
            result = say_good_bye()  

        case "exit":
            result = say_good_bye()   

        case "show all": #The first 
            result = show_all(adress_book)
            
        case "add":
            result = add_new_telephone_contact(command_word)
            
        case "change":
            result = change_phone_number(command_word)
            
        case "phone":
            result = show_name_contact(command_word)
            
    return result