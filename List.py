from __future__ import print_function
import Model

class List():

    def writing_to_lists(f_max_amp, f_roll_off, amp_roll_off, zero, cent_roll_off, dyn, har_num, euc_dis,
                       i, ilosc_probek, base_choice, number_of_files, number_of_file, user_choice,
                       lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7, lista_8, lista_9, lista_10):

        lista_1.insert(i, f_max_amp)
        lista_2.insert(i, f_roll_off)
        lista_3.insert(i, amp_roll_off)
        lista_4.insert(i, zero)
        lista_5.insert(i, cent_roll_off)
        lista_6.insert(i, dyn)
        lista_7.insert(i, euc_dis)
        lista_8.insert(i, har_num)

        if ilosc_probek > 2048 or ilosc_probek < 2048:

            # print("f max amp         : ", lista_1)
            # print("f roll off        : ", lista_2)
            # print("Amp roll off      : ", lista_3)
            # print("Zer crosssing     : ", lista_4)
            # print("Centroid roll off : ", lista_5)
            # print("Dynamic           : ", lista_6)
            # print("Euclides distance : ", lista_7)
            # print("Harmonic Number:  : ", lista_8, "\n")

            Freq_max_amp = sum(lista_1) / len(lista_1)
            Freq_roll_off = sum(lista_2) / len(lista_2)
            Amp_roll_off = sum(lista_3) / len(lista_3)
            Zero_cros = sum(lista_4) / len(lista_4)
            Cent_roll_off = sum(lista_5) / len(lista_5)
            Dyn = sum(lista_6) / len(lista_6)
            Euc = sum(lista_7) / len(lista_7)
            Harm = sum(lista_8) / len(lista_8)

            Parameters = [lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7, lista_8]
            Average_of_Parameters = [Freq_max_amp, Freq_roll_off, Amp_roll_off, Zero_cros, Cent_roll_off, Dyn, Euc, Harm]

            for num, list in enumerate(Parameters):
                for number, value in enumerate(list):
                    if value >= Average_of_Parameters[num] + 0.5 * Average_of_Parameters[num] or value <= Average_of_Parameters[num] - 0.5 * Average_of_Parameters[num]:
                        list.pop(number)

            Freq_max_amp = sum(lista_1) / len(lista_1)
            Freq_roll_off = sum(lista_2) / len(lista_2)
            Amp_roll_off = sum(lista_3) / len(lista_3)
            Zero_cros = sum(lista_4) / len(lista_4)
            Cent_roll_off = sum(lista_5) / len(lista_5)
            Dyn = sum(lista_6) / len(lista_6)
            Euc = sum(lista_7) / len(lista_7)
            Harm = sum(lista_8) / len(lista_8)

            List_of_parameters = [Freq_max_amp, Freq_roll_off,Amp_roll_off,Zero_cros, Cent_roll_off, Dyn, Harm, Euc]

            Parameters_name = ["Freq_max_amp ",
                               "Freq_roll_off",
                               "Amp_roll_off ",
                               "Zero_cros    ",
                               "Cent_roll_off",
                               "Dyn          ",
                               "Harm         ",
                               "Euc          "]

            Model.Model.creating_model(List_of_parameters, Parameters_name, base_choice, number_of_files, number_of_file, user_choice)