'''
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

    Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
    Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
    Polecenie "koniec" - Kończy działanie aplikacji.


Proces tworzenia użytkowników:

    Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
TODO    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
    Polecenie "koniec" - Wraca do pierwszego menu.


Proces zarządzania użytkownikami:

    Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
TODO    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
    Polecenie "koniec" - Wraca do pierwszego menu.


stworzyc system do zarzadzania nasza szkola:
kilka typow menu bedziemy miel
-glowne
-do tworzenia sobie uzytkownikow
-do zarzadzania uzytkownikami

Ogarnac jaka chcemy miec strukture tutaj jezeli chodzi o ta nasza szkole
w momencie tworzenia mozemy sobie skorzystac z jakis funkcji, bo widzimy, ze nasz kod się powtarza

'''
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}"


class Teacher:
    def __init__(self, name, surname, subject, grades):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grades = grades

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Zajęcia: {self.subject}, Klasy: {self.grades}"

class Educator:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return f"Imię: {self.name} Nazwisko: {self.surname}"

#TODO w domu potworzyli sobie klasy dla Nauczyciela i wychowawcy i zmienili je w naszej szkole



our_school = {
    "klasy": {
        "1a": {
            "uczniowie": [Student(name="Jan", surname="Kowalski")],
            "wychowawca": []
            }
        ,
        "2a": {
            "uczniowie": [Student(name="Jan", surname="Nowak")],
            "wychowawca": []

        },
    },
    "nauczyciele": []
}

def create_new_educator(name, surname, grade):
    our_school["klasy"][grade]["wychowawca"].append(Educator(name=name, surname=surname))

def create_new_teacher(name, surname, subject, grade):
    our_school["nauczyciele"].append(Teacher(name=name, surname=surname, subject=subject, grades=[grade]))

def create_new_grade(grade):
    our_school["klasy"][grade] = {
        "uczniowie": [],
        "wychowawca": []
    }

def create_student_in_existing_grade(name, surname, grade):
    our_school["klasy"][grade]["uczniowie"].append(Student(name=name, surname=surname))

def create_new_student(name, surname, grade):
    grade_exists = our_school.get("klasy").get(grade)
    if not grade_exists:
        create_new_grade(grade)
    create_student_in_existing_grade(name, surname, grade)

def find_grade_by_class_number(class_number):
    for grade_number, grade in our_school["klasy"].items():
        if grade_number == class_number:
            return f"Uczniowie to: {grade['uczniowie']} wychowawca to: {grade['wychowawca']}"
    return "Niestety nie znaleziono twojej klasy"

def find_class_teachers(class_number):
    found_teachers = []
    for teacher in our_school.get("nauczyciele"):
        if class_number in teacher.grades:
            found_teachers.append(teacher)
    return found_teachers

def find_student_educator(name, surname):
    found_class = []
    for educator in our_school.get("klasy")[0:]:
        if educator_name == educator.name and educator_surname == educator.surname:
            print("znaleziono")



#found_class += f"Wychowawca {educator_name} {educator_surname} ma pod opieką {}"


def find_teachers_for_class(name, surname):
    found_teacher = []
    for teacher in our_school.get("nauczyciele"):
        if teacher_name == teacher.name and teacher_surname == teacher.surname:
            found_teacher += f"Nauczyciel {teacher_name} {teacher_surname} prowadzi takie klasy jak: {teacher.grades} ".split(",")
            return found_teacher
        else:
            print("Nie znaleziono")

def find_student_by_name(name, surname):
    our_text = ""
    for grade_number, grade in our_school["klasy"].items():
        for student in grade.get("uczniowie"):
            if name == student.name and surname == student.surname:
                teachers = find_class_teachers(grade_number)
                for teacher in teachers:
                    our_text += f" Nauczyciel: {teacher.name} {teacher.surname} z przedmiotem: {teacher.subject} \n"
                return our_text
    return "Niestety twoja klasa nie ma żadnych zajęć"


initial_menu = "Witaj w swojej szkole. Podaj proszę co chcesz zrobić:\n 1.Utwórz\n 2.Zarządzaj\n 3.Koniec\n"
create_menu = "Podaj jakiego użytkownika chcesz utworzyć:\n 1.Uczeń \n 2.Nauczyciel \n 3.Wychowawca \n 4.Koniec\n"
manage_menu = "Podaj kim chcesz zarządzać: \n 1.Klasa \n 2.Uczeń \n 3.Nauczyciel \n 4.Wychowawca \n 4.Koniec\n"
finish_program = False
while not finish_program:
    main_guess = input(initial_menu)
    if main_guess == "1":
        #wchodzimy w tryb dodawania czegokolwiek do naszej szkoly
        create_input = input(create_menu)
        if create_input == "1":
            name = input("Podaj imię ucznia: ")
            surname = input("Podaj nazwisko ucznia: ")
            grade = input("Podaj klasę ucznia: ")
            create_new_student(name, surname, grade)
            print(our_school)
        elif create_input == "2":
            name = input("Podaj imię: ")
            surname = input("Podaj nazwisko: ")
            subject = input("Podaj przedmiot: ")
            grade = input("Podaj klasę: ")
            create_new_teacher(name, surname, subject, grade)
            print(our_school)
        elif create_input == "3":
            name = input("Podaj imię: ")
            surname = input("Podaj nazwisko: ")
            grade = input("Podaj klasę: ")
            create_new_educator(name,surname,grade)
            print(our_school)


    elif main_guess == "2":
        manage_input = input(manage_menu)
        if manage_input == "1":
            class_number = input("Podaj nazwę klasy: ")
            text_to_display = find_grade_by_class_number(class_number)
            print(text_to_display)
        elif manage_input == "2":
            student_name = input("Podaj imię ucznia: ")
            student_surname = input("Podaj nazwisko ucznia: ")
            text = find_student_by_name(student_name, student_surname)
            print(text)
        elif manage_input == "3":
            teacher_name = input("Podaj imię nauczyciela: ")
            teacher_surname = input("Podaj nazwisko nauczyciela: ")
            found_teacher = find_teachers_for_class(teacher_name, teacher_surname)
            print(found_teacher)
        elif manage_input == "4":
            educator_name = input("Podaj imię wychowawcy: ")
            educator_surname = input("Podaj nazwisko wychowawcy: ")
            found = find_student_educator(educator_name, educator_surname)


    elif main_guess == "3":
        finish_program = True