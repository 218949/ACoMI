import os
import Recognition
import main

class Model():

    def creating_model(List_of_parameters, Parameters_name, base_choice, number_of_files, number_of_file, user_choice):
        path = "Models/" + base_choice + "_model.txt"
        dir_path = os.path.join(path)

        if number_of_files == 1 and user_choice == "1":

            print(sep="\n")
            print(base_choice, "model parameters:")
            writing_file = open(path, mode="w+")
            for number, parameter in enumerate(List_of_parameters):
                print(Parameters_name[number], parameter)
                writing_file.write(str(parameter))
                writing_file.write("\n")
            writing_file.close()
            print(sep="\n")
            main.main_menu()

        if number_of_files > 1 and user_choice == "1":

            list = open(dir_path, "r+")
            if list.readlines() == []:
                for number, parameter in enumerate(List_of_parameters):
                    writing_file = open(path, mode="a+")
                    writing_file.write(str(parameter))
                    writing_file.write("\n")
                    writing_file.close()
                list.close()

            else:

                list.close()
                list_of_add_parameters = []
                list = open(dir_path, "r+")
                for number, line in enumerate(list.readlines()):
                    list_of_add_parameters.append(float(line) + List_of_parameters[number])
                list.close()
                writing_file = open(path, mode="w+")
                for number, parameter in enumerate(list_of_add_parameters):
                    writing_file.write(str(parameter))
                    writing_file.write("\n")
                writing_file.close()

# Średnia z parametrów dla modelu
        if number_of_file + 1 == number_of_files and number_of_files > 1:
            print("!!!")
            list_of_parameters = []

            writing_file = open(path, mode="a+")
            for number, parameter in enumerate(writing_file.readlines()):
                list_of_parameters.insert(number, parameter)
            writing_file.close()

            average_list_of_parameters = []

            for number, parameter in enumerate(list_of_parameters):
                average_list_of_parameters.insert(number, parameter / number_of_files)

            writing_file = open(path, mode="w+")
            print(sep="\n")
            print(base_choice, "model parameters:")
            for number, parameter in enumerate(average_list_of_parameters):
                print(Parameters_name[number], parameter)
                writing_file.write(str(parameter))
                writing_file.write("\n")
            writing_file.close()
            print(sep="\n")

            main.main_menu()

        if user_choice == "2":
            print(sep="\n")
            print("RECOGNATION!!!")

            writing_file = open("./Models/Diagnosis_model.txt", mode="w+")
            for number, parameter in enumerate(List_of_parameters):
                writing_file.write(str(parameter))
                writing_file.write("\n")
            writing_file.close()

            Recognition.recognition(List_of_parameters, base_choice, Parameters_name)

        #main.main_menu()