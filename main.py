#! usr/bin/env python3

import pyinputplus as pyip
import cv2 as cv
import pandas as pd
import requests, time, webbrowser, csv, os



def print_pause(*args, pause: int=0) -> None:
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

    print_pause("Wecome to my voting app\n")
    return


def user_choice() -> int:
    ''' returns the user option '''

    while True:
        user_prompt = pyip.inputMenu(["Accreditation", "Cast Vote", "Upload Image", "View Result\n"],
                                     prompt="Please pick the corresponding number"
                                     " from the following options: \n", 
                                     numbered=True)

        print_pause("Just to confirm, Are you sure you"
                    f" want to proceed with {user_prompt}?")
        
        bool_ans = pyip.inputYesNo(prompt="Answer yes(y) or no(n): \n",)
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
    return


def accreditation() -> None:
    '''
    func when user_choice = Accreditation

    verifies the new/existing voter'''

    verified_list = []
    card_nos = pyip.inputCustom(validate_voter, 
                     prompt="Please enter your voter's" 
                     " card number: ")
    try:
        if card_nos not in verified_list:
            verified_list.append(card_nos)
            print("You are now verified")
    except:
        print("You've already been verified")
    return


def cast_vote() -> int:
    ''' 
    func when user_choice = Cast Vote
    
    takes the user's vote'''

    print_pause("Carefully choose the corresponding number for your"
                " party of choice.")
    
    print_pause("1. Action Democratic Party (ADP)\n"
            "2. African Democratic Congress (ADC)\n"
            "3. African Democratic Party (ADP)\n"
            "4. All Grassroots Alliance (AGA)\n"
            "5. All Progressives Congress (APC)\n"
            "6. All Progressives Grand Alliance (APGA)\n"
            "7. Democratic People's Party (DPP)\n"
            "8. Labour Party (LP)\n"
            "9. Peoples Democratic Party (PDP)\n"
            "10. Progressive Peoples Alliance (PPA)\n"
            "11. Young Progressives Party (YPP)\n"
            )
    user_vote = pyip.inputNum(prompt=
                              "\nEnter your party's number here: ",
                              max=11, min=1)
    return user_vote

    
def record_vote() -> None:
    '''records the user's vote in the flat file'''

    vote_num = cast_vote()
    df = pd.read_csv("votes.csv", index_col="serial")
    df.loc[vote_num, "count"]+=1
    df.to_csv("votes.csv", index=True, sep=",")    
    print_pause("\nYour vote has been recorded successfully")
    return


def upload_image() -> str:
    '''
    func when user_choice = Upload Image
    '''
    camera = cv.VideoCapture(0)
    return_value, image = camera.read()
    cv.imwrite('result.jpg', image)
    del(camera)
    img = cv.imread('result.jpg')
    cv.imshow('Captured Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    url = 'https://github.com/Mr-cyber200/python-script'
    files = {'file': open('result.jpg', 'rb')}
    r = requests.post(url, files=files)
    print_pause(r.text)
    print_pause("Image captured and uploaded to portal")
    return

def view_result() -> None:
    '''func when user_choice = View Result '''

    print("Redirecting you to the result page...")
    webbrowser.open("https://www.inecelectionresults.ng/elections/types")
    return


def create_csv() -> None:
    '''
    creates a csv file to collect the vote count
    '''
    with open("votes.csv", "w") as f:
        pol_party = ["ADP","ADC","AfDP","AGA","APC","APGA", "DPP",
        "LP","PDP","PPA","YPP"]
        write_obj = csv.DictWriter(f, ["serial", "party", "count"])
        write_obj.writeheader()

        for index, party in enumerate(pol_party, start=1):
            write_obj.writerow({"serial": index, "party": party, "count": 0})
    return

def main() -> None:
    '''main function for the script'''
    intro_msg()
    voter_choice = user_choice()
    if voter_choice == "Accreditation":
        accreditation()
    elif voter_choice == "Cast Vote":
        record_vote()
    elif voter_choice == "Upload Image":
        upload_image()
    elif voter_choice == "View Result":
        view_result()
    return


if __name__ == "__main__":
    if not os.path.exists("votes.csv"):
        create_csv()
    main()
    

