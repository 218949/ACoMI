from __future__ import print_function
import List
import numpy as np
import math

class Parameters():
    def parameterization(data, part_of_data, fs_rate, number_of_samples_in_frame, number_of_frame,
                         base_choice, number_of_files, number_of_file, user_choice,
                         lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10,):
# FFT
        spectrum = part_of_data / np.max(np.abs(data))
        spectrum_data = 10 * np.log10(np.abs(np.fft.rfft(spectrum * np.hamming(number_of_samples_in_frame))) / 1024)
        frequency_data = np.fft.rfftfreq(2048, 1 / fs_rate)

        Frequency = []
        Amplitude = []
        for number, amplitude in enumerate(spectrum_data):
            if frequency_data[number] <= 20000:
                Frequency.insert(number, frequency_data[number])
                Amplitude.insert(number, spectrum_data[number])

        spectral_roll_off = (sum(Amplitude) / len(Amplitude)) * 0.85

        frequency_spectral_roll_off = 0
        spectral_roll_off_amp = 0

        for number, amplitude in enumerate(Amplitude):
            if (Amplitude[number] <= spectral_roll_off + 1) and (Amplitude[number] >= spectral_roll_off - 1):
                spectral_roll_off_amp = amplitude
                frequency_spectral_roll_off = number

# Zero crossing
        zero_crossing_rate_counter = 0  # licznik przejsc przez zero
        for number in range(0, len(part_of_data) - 1):
            if part_of_data[number] * (-1) > 0 and part_of_data[number + 1] > 0:
                zero_crossing_rate_counter += 1
        zero_crossing_rate = zero_crossing_rate_counter / len(part_of_data)

# Spectrall centroid
        sum_spectral_centroid_roll_off = 0
        for number, amplitude in enumerate(Amplitude):
            if number <= frequency_spectral_roll_off:
                sum_spectral_centroid_roll_off = sum_spectral_centroid_roll_off + (Amplitude[number] * Frequency[number])
        spectral_centroid_roll_off = sum_spectral_centroid_roll_off / sum(Amplitude)

# Dynamic
        mean = sum(Amplitude) / len(Amplitude)
        dynamic = max(Amplitude) / mean

        amplitude_spectral_roll_off = []
        for number, amplitude in enumerate(Amplitude):
            if number <= frequency_spectral_roll_off:
                amplitude_spectral_roll_off.insert(number, Amplitude[number])

#Harmonic
        Tops_Amplitude = []
        Tops_Number_Frequency = []
        Tops_Frequency = []
        for number, amplitude in enumerate(Amplitude):
            if number > 0 and number < len(Amplitude) - 1:
                if amplitude > Amplitude[number - 1] and amplitude > Amplitude[number + 1]:
                    Tops_Amplitude.append(amplitude)
                    Tops_Number_Frequency.append(number)

        for number, amplitude in enumerate(Tops_Amplitude):
            if number > 0 and number < len(Tops_Amplitude) - 1:
                if amplitude < -(((- Tops_Amplitude[number - 1] - Tops_Amplitude[number + 1]) / 2) + ((- Tops_Amplitude[number - 1] - Tops_Amplitude[number + 1]) * 0.1 * 0.5)):
                    Tops_Amplitude.remove(amplitude)
                    Tops_Number_Frequency.pop(number)

        for num, index in enumerate(Tops_Number_Frequency):
            for number, frequency in enumerate(Frequency):
                if index == number:
                    Tops_Frequency.append(frequency)

        Harmonic_List = []
        Harmonic_List_Left = []
        Harmonic_List_Right = []

        for number, amplitude in enumerate(Amplitude):
            for num, amp in enumerate(Tops_Amplitude):
                if Tops_Amplitude[num] == amplitude:
                    if Amplitude[number - 1] < amplitude and number > 0:
                        Left_Save_Amplitude_Harmonic = number - 1
                        if Amplitude[number - 2] < Amplitude[number - 1] and number > 1:
                            Left_Save_Amplitude_Harmonic = number - 2
                            if Amplitude[number - 3] < Amplitude[number - 2] and number > 2:
                                Left_Save_Amplitude_Harmonic = number - 3
                                if Amplitude[number - 4] < Amplitude[number - 3] and number > 3:
                                    Left_Save_Amplitude_Harmonic = number - 4
                    if Amplitude[number + 1] < amplitude and number < len(Amplitude)-4:
                        Right_Save_Amplitude_Harmonic = number + 1
                        if Amplitude[number + 2] < Amplitude[number + 1] and number < len(Amplitude) - 1:
                            Right_Save_Amplitude_Harmonic = number + 2
                            if Amplitude[number + 3] < Amplitude[number + 2] and number < len(Amplitude) - 2:
                                Right_Save_Amplitude_Harmonic = number + 3
                                if Amplitude[number + 4] < Amplitude[number + 3] and number < len(Amplitude) - 3:
                                    Right_Save_Amplitude_Harmonic = number + 4

                    Harmonic_List.append(Left_Save_Amplitude_Harmonic)
                    Harmonic_List_Left.append(Left_Save_Amplitude_Harmonic)
                    Harmonic_List.append(Right_Save_Amplitude_Harmonic)
                    Harmonic_List_Right.append(Right_Save_Amplitude_Harmonic)

        Harmonic_List_Amplitude = []
        Harmonic_List_Frequency = []

        for num, index in enumerate(Harmonic_List_Left):
            for number, amplitude in enumerate(Amplitude):
                if number >= Harmonic_List_Left[num] and number <= Harmonic_List_Right[num]:
                    Harmonic_List_Amplitude.append(amplitude)
        for num, index in enumerate(Harmonic_List_Left):
            for number, frequency in enumerate(Frequency):
                if number >= Harmonic_List_Left[num] and number <= Harmonic_List_Right[num]:
                    Harmonic_List_Frequency.append(frequency)

        maksima_freq = []
        maksima_amp = []
        for number, index in enumerate(Harmonic_List_Left):
            widmo = []
            freq = []
            for num, amplitude in enumerate(Amplitude):
                if num < index:
                    widmo.append(Amplitude[index])
                if num >= Harmonic_List_Left[number] and num <= Harmonic_List_Right[number]:
                    widmo.append(amplitude)

            for num, frequency in enumerate(Frequency):
                if num < index:
                    freq.append(Frequency[num])
                if num >= Harmonic_List_Left[number] and num <= Harmonic_List_Right[number]:
                    freq.append(frequency)

        # Ustalenie progu amplitudy powyżej progu + 5 dB nie są brane pod uwagę
            if Amplitude[Harmonic_List_Left[number]] > Amplitude[Harmonic_List_Right[number]]:
                prog = Amplitude[Harmonic_List_Left[number]] + 3
            elif Amplitude[Harmonic_List_Left[number]] < Amplitude[Harmonic_List_Right[number]]:
                prog = Amplitude[Harmonic_List_Right[number]] + 3
            ponad = (widmo >= prog).astype(np.int)
            pochodna = np.diff(ponad)
            poczatki = np.where(pochodna == 1)[0] + 1
            konce_lista = np.where(pochodna == -1)[0] + 1
            konce = []
            if len(konce_lista) > 1:
                konce.append(konce_lista[-1])
            elif len(konce_lista) == 1:
                konce.append(konce_lista[0])

            for poczatek, koniec in zip(poczatki, konce):
                p = np.argmax(widmo[poczatek:koniec]) + poczatek

                a, b, c = widmo[p - 1:p + 2]
                k = 0.5 * (a - c) / (a - 2 * b + c)

                maksima_freq.append((p + k) * fs_rate / number_of_samples_in_frame)
                maksima_amp.append(Amplitude[p])
        Harmonic_Number = len(maksima_amp)

# Euclides distance
        Euclides_distance = []
        for number, value in enumerate(maksima_amp):
            if number + 1 < len(maksima_amp):
                Euclides_distance.insert(number, math.sqrt(math.pow(maksima_amp[number] - maksima_amp[number + 1], 2) + math.pow(maksima_freq[number + 1] - maksima_freq[number], 2)))
        if len(Euclides_distance) != 0:
            Average_Euclides_distance = sum(Euclides_distance)/len(Euclides_distance)
        elif len(Euclides_distance) == 0:
            Average_Euclides_distance  = 0

# Frequency of max amplitude
        if maksima_amp != []:
            for number, amplitude in enumerate(maksima_amp):
                if amplitude == max(maksima_amp):
                    number_of_max_amplitude = number
            frequency_of_max_amplitude = maksima_freq[number_of_max_amplitude]
        elif maksima_amp == []:
            for n, a in enumerate(Amplitude):
                if a == max(Amplitude):
                    frequency_of_max_amplitude = Frequency[n]

        List.List.writing_to_lists(frequency_of_max_amplitude,frequency_data[frequency_spectral_roll_off],spectral_roll_off_amp,
                                   zero_crossing_rate_counter,spectral_centroid_roll_off,dynamic, Harmonic_Number, Average_Euclides_distance,
                                   number_of_frame,number_of_samples_in_frame,base_choice,number_of_files,number_of_file,user_choice,
                                   lista_1,lista_2,lista_3,lista_4,lista_5,lista_6,lista_7,lista_8,lista_9,lista_10)