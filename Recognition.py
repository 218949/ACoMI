import os
import main

def recognition(List_of_parameters, base_chocie, Parameters_name):

    number_of_created_parameters = len(List_of_parameters)
    del_content_of_recognition = open("./Recognition.txt", mode="w+")
    del_content_of_recognition.close()

    list_of_model_parameters = []
    list_of_diagnosis_parameter = []
    average_list_of_model = []


    open_list_of_diagnosis_file = open("./Models/Diagnosis_model.txt", mode = "r+")
    for line, parameter in enumerate(open_list_of_diagnosis_file):
        list_of_diagnosis_parameter.append(parameter)
    open_list_of_diagnosis_file.close()

    for line, value in enumerate(os.listdir("./Models")):
        list_of_model_parameters.append(value)

    for model in list_of_model_parameters:
        open_list_of_model = open("Models/" + model, mode="r+")

        list_of_difference = []

        len_of_list_parameters = len(open_list_of_model.readlines())
        open_list_of_model.close()

        if len_of_list_parameters != number_of_created_parameters:
            print("Nie zgodność ilości parametrów, stwórz bazę na nowo dla:", model)
            main.main_menu()

        elif len_of_list_parameters == number_of_created_parameters:
            open_list_of_model = open("Models/" + model, mode="r+")
            for number, parameter in enumerate(open_list_of_model):
                if number < len_of_list_parameters:
                    list_of_difference.append(abs(100 - ((float(list_of_diagnosis_parameter[number])*100))/(float(parameter))))
            open_list_of_model.close()

            sum_lis_of_difference = sum(list_of_difference)
            average_list_of_model.append(sum_lis_of_difference/number_of_created_parameters)

        save_to_recognition = open("./Recognition.txt", mode="r+")
        for average in average_list_of_model:
            save_to_recognition.write(str(average))
            save_to_recognition.write("\n")
        save_to_recognition.close()

    list_of_recognation_files = []
    list_of_sort_recognation_files_float = []
    list_of_sort_recognation_files_str = []

    open_file = open("./Recognition.txt", mode="r+")
    for recognation in open_file.readlines():
        list_of_recognation_files.append(recognation)
    open_file.close()

    open_file = open("./Recognition.txt", mode="r+")
    for recognation in open_file.readlines():
        list_of_sort_recognation_files_float.append(float(recognation))
    list_of_sort_recognation_files_float.sort()
    open_file.close()

    for value in list_of_sort_recognation_files_float:
        list_of_sort_recognation_files_str.append(str(value))

    for number, value in enumerate(list_of_recognation_files):
        if list_of_sort_recognation_files_str[1] in value:
            number_of_recognation = number

    print(sep="\n")

    for number, model in enumerate(os.listdir("./Models")):
        if model != "Diagnosis_model.txt":
            print("Procent distance:", round(float(list_of_recognation_files[number].rstrip()), 2), "% for model:", model)

            open_file_of_model = open("./Models/" + model)
            for num, parameter in enumerate(open_file_of_model.readlines()):
                print("Paremter:", Parameters_name[num], " | ", "Value:", parameter.rstrip())
            open_file_of_model.close()

            print(sep="\n")

            if number == number_of_recognation:
                result = model.split("_")

    print("Signal was recognized as:", result[0], "\n")

    main.main_menu()
