from collections import UserDict

#Тут мы опишем все классы

class AddressBook(UserDict): #потім додамо логіку пошуку за записами до цього класу.
    #Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
    #AddressBook реалізує метод add_record, який додає Record у self.data.
    
    def show_all(self):
        return self.data
    def add_recird(self, record):
        self.data.update(record)

class Record: #відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    #В класі Record є 2 атрибути це name i phones
#name буде екземпляром Name який ви створите в ініт методі Record-a, a phones це список екземплярів класу Phone.
#Логіка програми така ж як і була в 9 дз
#список phones через метод add_phone класу Record наповнюватиметься
#І, відповідно, зі всіма класами працюєте як з екземплярами 
    def __init__(self, name, phone = None, ):
        self.name = name    
        self.phones = list()

        if phone:
            self.phones.append(phone)
        print(phone)
    
class Field: # який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
    #Є клас Field в якому атрибут value в ініті.
#від цього класу наслідується Phone i Name
    def __init__(self, value):
        self.value = value
class Name(Field): #обов'язкове поле з ім'ям
    pass
class Phone(Field): #необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    pass

class PrintData:
    pass

"""юзер, наприклад, добавляє контакт, він ввів щось типу:
add Volodymyr +380111111
ви парсите цю стрічку, отримуєте імʼя і телефон окремо.
створюєте екземпляр Record, передавши імʼя і телефон.
Сам ініт має виглядати, приблизно, так:
class Record:
    def __init__(self, name, phone=None):
         self.name = Name(value=name)
         self.phones = []
         if phone:
             self.add_phone_number(phone)
після того як створили екземпляр Record-a, сетаєте його в AddressBook
address_book  = AddressBook()
address_book.add_record(record)
ну і сам метод add_record якось так:
def add_record(record: Record):
     self.data[record.name.value] = record"""