# У класі є одна особлива функція яка називається Конструктор
# У конструкторі зявляються особлива зміна, яка називається self - вказівник на обєкт
# self ніколи явно не передається при виклику обєктів
class WhoHasPetsModule():
    #Класова змінна буде нам зберігати інформацію про кількість учасників (кількість створених обєкті
    user_count = 0
    
    # Ми передаємо у конструктор аргументи для заповнення атрибутів обєкту
    def __init__(self, name:str, surname:str, pets:set={}, pets_age:dict={}) -> None:
        self.name = name
        self.surname = surname
        # ми можемо модифікувати аргументи перш ніж присвоїти їх артибутам обєкту
        self.full_name = name + " " + self.surname
        self.pets = pets if len(pets) > 0 else "!Заведи собі домашніх улюбленців!"
        self.pets_age = pets_age
        WhoHasPetsModule.user_count += 1
        
    @property
    def full_name_property(self):
        return f"{self.name} {self.surname}"
    
    def pets_amount(self):
        return len(self.pets) if isinstance(self.pets, set) else 0

    def add_new_pet(self, breed:str, name:str=None, age:int=None):
        if isinstance(self.pets, set):
            # У даного обєкта вже є улюбленці, тому ми просто додаємо нового до списку
            self.pets.add(breed)
        else:
            self.pets = {breed}
        if name != None and age != None:
            self.pets_age = {name: age}
    
    def remove_pet(self, breed:str):
        print(f"Як шкода що {breed} вже немає :(")
        self.pets.remove(breed)
        
    @staticmethod
    def say_hello(name=None, spam:bool = False):
        if name !=None:
            s = f"Привіт {name}, вітаємо в клубі любителів домашніх тварин!"
        else:
            s = "Привіт всім любителям домашніх тварин!"
        if spam:
            for i in range(10):
              print(f"{s} Кажу це вже {i} раз!!!")
              
        else:
            print(s)
        
    @classmethod 
    def invite_new_user(cls, name:str, surname:str):
        cls.say_hello(name)
        return cls(name, surname)
    
    @classmethod
    def get_user_count(cls):
        #Класовий метод для отримання кількості створених учасників клубу
        print(f"Нас вже є {cls.user_count} учасників клубу!")
        return cls.user_count

if __name__ == "__main__":
    print("Це є виконання команд з самого модуля!")