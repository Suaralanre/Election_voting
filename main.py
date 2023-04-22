#! usr/bin/env python3

import pyinputplus as pyip
import cv2 as cv
import requests, time, webbrowser, csv

# create a csv file to collect the vote count
# with open("votes.csv", "w+") as f:



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


def user_choice() -> int:
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
        user_prompt = pyip.inputMenu(["Accreditation", "Cast Vote", "Upload Result", "View Result"],
                                     prompt="Please pick the corresponding number"
                                     "from the following options: ", 
                                     numbered=True)

        print_pause(f"Just to confirm, Are you sure you"
                    "want to proceed with {user_option[user_choice]}?")
        
        bool_ans = pyip.inputYesNo(prompt="Answer yes(y) or no(n)",)
        if bool_ans == 'no':
            continue
        break
    return user_prompt


def validate_voter(user_input: int) -> None:
    ''' validates if the user's voter card is valid 
    or not'''
    registered_card = ["123456789", "987654321", "456789123"]
    if user_input not in registered_card:
        raise ValueError("Your voter's card is not registered")


def accreditation() -> None:
    '''verifies the new/existing voter'''
    verified_list = []
    card_nos = pyip.inputCustom(validate_voter, 
                     prompt="Please enter your voter's" 
                     "card number: ")
    try:
        if card_nos not in verified_list:
            verified_list.append(card_nos)
    except:
        print("You've already been verified")


def cast_vote() -> int:
    ''' takes the user's vote'''
    print_pause("Carefully choose the corresponding number for your"
                "party of choice.")
    user_vote = pyip.inputInt(
    prompt="1. Action Democratic Party (ADP)\n"
            "2. African Democratic Congress (ADC)\n"
            "3. African Democratic Party (ADP)\n"
            "4. All Grassroots Alliance (AGA)\n"
            "5. All Progressives Congress (APC)\n"
            "6. All Progressives Grand Alliance (APGA)\n"
            "7. Democratic People's Party (DPP)\n"
            "8. Labour Party (LP)\n"
            "9. Peoples Democratic Party (PDP)\n"
            "10. Progressive Peoples Alliance (PPA)\n"
            "11. Young Progressives Party (YPP)",
    max=11, min=1
    )
    
def 