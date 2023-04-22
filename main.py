#! usr/bin/env python3

import pyinputplus as pyip
import cv2 as cv
import requests, time, webbrowser


def print_pause(*args, pause: int=2) -> None:
    '''prints the string slowly based on the 
    time set. Default is 2 secs'''
    print(*args)
    time.sleep(pause)

def intro_msg() -> str:
    ''' prints the introductory message '''

    print_pause("************************************************************************\ ") 
    print_pause("@@@@@@@@@@@@@@@@@@@@ copyright of Mr_Cyber 2023 @@@@@@@@@@@@@@@@@@@@@@@@/") 
    print_pause("************************************************************************\ ") 
    print_pause("************************************************************************/") 
    print_pause(" _         _    ___         ______           ______     ______    ___")
    print_pause("| \       / | |     \     /         \     / |       \  |        |      \ ")
    print_pause("|  \     /  | |  D   )   /           \   /  |   D    | |        |   O   )")
    print_pause("|   \ _ /   | |     /   /             \ /   | _____ /  |______  |      /")
    print_pause("|     O     | |    / __ \              |    |       \  |        |     /")
    print_pause("|    ___    | |  _ \     \             |    |   D    | |        |  __ \ ")
    print_pause("| _ |   | _ | |_| |_\     \ ______     |    | ______ / |______  |_|  |_\ ")
    print_pause("************************************************************************")
    print_pause("@@@@@@@@@@@@@ github link = https://github.com/Mr-cyber200 @@@@@@@@@@@@@") 
    print_pause("LinkendIn link = https://www.linkedin.com/in/nwarienne-michael-378b5a183") 
    print_pause("************************************************************************") 

    print_pause("Wecome to my voting app")


def user_prompt() -> int:
    ''' returns the user option '''

    # user_option = {
    #     1: "Accreditation",
    #     2: "Cast Vote",
    #     3: "Upload Result",
    #     4: "View Result",
    # }
    # print_pause("Please pick the corresponding number"
    #             "from the following options")
    # for key, value in user_option.items():
    #     print_pause(key, ":", value)

    while True:
        user_choice = pyip.inputMenu(["Accreditation", "Cast Vote", "Upload Result", "View Result"],
                                     prompt="Please pick the corresponding number"
                                     "from the following options: ", 
                                     numbered=True)

        print_pause(f"Just to confirm, Are you sure you"
                    "want to proceed with {user_option[user_choice]}?")
        
        bool_ans = pyip.inputYesNo(prompt="Answer yes(y) or no(n)",)
        if bool_ans == 'no':
            continue
        break
    return user_choice


def validate_voter() -> bool:
    ''' validates if the user's voter card is valid 
    or not'''

# def accreditation():
    