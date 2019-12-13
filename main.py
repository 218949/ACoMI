from __future__ import print_function
import Read
import os


def main_menu():

    print(sep="/n")
    print("1. Stwórz bazę dla instrumentów \n2. Rozpoznaj instrument \n3. Zakończ program!")
    print(sep="/n")
    user_choice_main = input("Wybierz akcję: ")
    print(sep="/n")

    if user_choice_main == "1":
        list_of_flies = []
        print(sep="/n")
        for number, file in enumerate(os.listdir("./Instruments")):
            print(number + 1, ". ", file, sep="")
            list_of_flies.insert(number, file)
        print(sep="/n")

        if len(list_of_flies) == 0:
            print("Folder jest pusty.")

        elif len(list_of_flies) > 0:
            user_choice = input("Wybierz numer katalogu, do stworzenia bazy:")
            list_of_numbers = []
            for number in range(0, len(list_of_flies) + 1):
                list_of_numbers.append(number)
            exist = "no"
            for number, element in enumerate(list_of_numbers):
                if str(element) == user_choice:
                    exist = "yes"

            if exist == "yes":
                for number, folder in enumerate(os.listdir("./Instruments")):
                    if int(user_choice) == number + 1:
                        base_choice = folder
                        print("Wybrałeś:", base_choice)
                        print(sep="/n")

                path = "./Models/" + base_choice + "_model.txt"
                writing_file = open(path, mode="w+")
                writing_file.close()

                number_of_files = len(os.listdir("./Instruments/" + base_choice))
                print(number_of_files)

                for number_of_file, file in enumerate(os.listdir("./Instruments/" + base_choice)):
                    Read.Read_file.read(file, base_choice, number_of_files, number_of_file, user_choice_main)

            elif exist == "no":
                print(sep="\n")
                print("Podałeś nieprawidłowy znak!1")
                print(sep="\n")
                main_menu()





    elif user_choice_main == "2":



                list_of_flies_to_classification = []
                for number_of_file, file in enumerate(os.listdir("./Instruments/Diagnosis")):
                    print(number_of_file + 1, ". ", file, sep="")
                    list_of_flies_to_classification.insert(number_of_file, file)
                print(sep="\n")

                if len(list_of_flies_to_classification) == 0:
                    print("Folder jest pusty.")
                else:
                    user_choice_file_classification = input("Wybierz sygnał do klasyfikacji:")

                    list_of_numbers = []
                    for number in range(0, len(list_of_flies_to_classification) + 1):
                        list_of_numbers.append(number)
                    exist = "no"
                    for number, element in enumerate(list_of_numbers):
                        if str(element) == user_choice_file_classification:
                            exist = "yes"

                    if exist == "yes":
                        for number_of_file, file in enumerate(os.listdir("./Instruments/Diagnosis")):
                            if int(user_choice_file_classification) == number_of_file + 1:
                                file_choice = file
                                print("Wybrałeś:", file_choice)
                                print(sep="/n")
                                Read.Read_file.read(file_choice, "Diagnosis", 1, number_of_file, user_choice_main)

                    elif exist == "no":
                        print(sep="\n")
                        print("Podałeś nieprawidłowy znak!2")
                        print(sep="\n")
                        main_menu()

    elif user_choice_main == "3":
        print("Koniec programu")

    else:
        print(sep="\n")
        print("Podałeś nieprawidłowy znak!4")
        print(sep="\n")
        main_menu()

