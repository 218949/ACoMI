from __future__ import print_function
import scipy.io.wavfile as wavfile
import wave
#import pyglet
import Frames
#import os
from playsound import playsound


class Read_file():

    def read(file_choice, base_choice, number_of_files, number_of_file, user_choice):

        print(sep="\n")
        read = "Instruments/" + base_choice + "/" + file_choice
        print("Path of file:", read)

        if number_of_files == 1:
            print("Left:", number_of_files, "file")

        elif number_of_files > 1:
            print("Left:", number_of_files - number_of_file, "files")

        fs_rate, data = wavfile.read(read)
        sample = wave.open(read)
        liczba_kanalow = len(data.shape)
        # print("Liczba kanałów: ", liczba_kanalow)
        signal_parameters = sample.getparams()
        print("Parameters of file:", signal_parameters, "\n")
        number_of_samples = sample.getnframes()
        # print("liczba ramek: ", liczba_ramek)

        playsound(read)

        lenght = len(data.shape)
        data = data.astype(float)
        if lenght == 2:
            data = data.sum(axis=1) / 2

        Frames.Frames.frames_division(data, number_of_samples, fs_rate, base_choice, number_of_files, number_of_file, user_choice)

