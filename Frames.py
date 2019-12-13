from __future__ import print_function
import Parameters
#import pyglet
#import os
class Frames():

    def frames_division(data, number_of_samples, fs_rate, base_choice, number_of_files, number_of_file, user_choice):

        list_1 = []
        list_2 = []
        list_3 = []
        list_4 = []
        list_5 = []
        list_6 = []
        list_7 = []
        list_8 = []
        list_9 = []
        list_10 = []

        frame_begin = [0]
        for number, frame in enumerate(frame_begin):
            if frame_begin[number] <= number_of_samples:
                frame_begin.insert(number + 1, frame_begin[number] + 2000)

        frame_end = [2048]
        for number, frame in enumerate(frame_end):
            if frame_end[number] <= number_of_samples:
                frame_end.insert(number + 1, frame_end[number] + 2000)

        if frame_end[-1] > number_of_samples:
            frame_end.pop(-1)
            frame_end.append(number_of_samples)

        for number_of_frame, frame in enumerate(frame_begin):
            if frame_begin[number_of_frame] <= number_of_samples:
                part_of_data = data[frame_begin[number_of_frame]: frame_end[number_of_frame]]
                number_of_samples_in_frame = len(part_of_data)

                # print("######################################################################################################################")
                # print(number_of_samples)
                # print("Frame: ", number_of_frame + 1, ",", "frame_begin:", frame_begin[number_of_frame], ",", "frame_end:", frame_end[number_of_frame], ",", "Part of data: ", part_of_data)
                # print("i: ", number_of_frame)

                # Percent
                percent = (100 * number_of_frame) / len(frame_begin)
                print("Parameterization progress:", round(percent, 2), "%")
                #os.system("cls")

                Parameters.Parameters.parameterization(data, part_of_data, fs_rate, number_of_samples_in_frame, number_of_frame,
                                                       base_choice, number_of_files, number_of_file, user_choice,
                                                       list_1, list_2, list_3, list_4, list_5,
                                                       list_6, list_7, list_8, list_9, list_10)
