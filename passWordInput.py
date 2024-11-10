import subprocess
from getpass import getpass
from pathlib import Path
from random import shuffle


#RSA Section
p = 447106507
q = 5940619
n = p*q


dict = {"General Batman" : "4e63be1122d51e7cc915512588a06e9bd1ea60cbe59ba3b40dce00cde2dac23",
        "Colonel Spiderman" : "1e7cf8c7a52ad61ca65e9403ebef462bcf4c85c0a9b01c1726ace07f9b14ecac", 
        "President Trump  " : "ec4b5a41fbac55548db79a0d2db9abab37c60026adc6636e3f9c0a64411c7f42"}



# passwords: AlfredisCute, TonyDead， IMissBiden

def failLoginLog():
    "todo"

def login():
    ### Login Page

    print("-------- MARS INTEL AGENCY LOGIN SYSTEM --------")
    print("--------        NUKE LAUNCH SYSTEM      --------")
    print("------------------------------------------------")
    username = input("Enter Username: ")
    while (username not in dict.keys()):
        print("INVALID USERNAME, AGAIN")
        username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    f = open("TempPassword.txt", "w")
    f.write(password)
    f.close()

    command = "./hash TempPassword.txt"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    hashed_pass = process.communicate()[0]
    hashed_pass = (hashed_pass.decode("utf-8"))

    isBoss = False
    count = 0
    while (count < 3):
        if(hashed_pass == dict[username]):
            isBoss = True
            break
        password = getpass("Wrong Password, re-enter Password: ")

        f = open("TempPassword.txt", "w")
        f.write(password)
        f.close()

        command = "./hash TempPassword.txt"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        hashed_pass = process.communicate()[0]
        hashed_pass = (hashed_pass.decode("utf-8"))
        
        count+=1

    print("------------------------------------------------ ")
    print(f"LOGIN SUCCESSFUL, WELCOME {username}")
    print("------------------------------------------------ ")
    return (isBoss, username)


def displayFileName():
    files = []
    folder_path = Path('classified')
    for file in folder_path.iterdir():
        if file.is_file() and str(file)[len('classified')+1] != '.' :
            files.append(str(file))
    shuffle(files)
    for count, fileName in enumerate(files):
        print(count, fileName)
    return (count, files)

def select3Files(topNum: int, files: list[str]):
    selected_nums = []
    selected_files = []
    for i in range(3):
        num = (int)(input(f"select file {i}: "))
        while (num>topNum or num<0):
            num = (int)(input(f"file out of range, select file again {i}: "))
        selected_nums.append(num)
        selected_files.append(files[num])
    return (selected_files)

def Hash3Files(files: list[str]):
    hashed_file_path = "hashed_file.txt"

    print(f"\n{files}\n")
    for i in range(3):
        filePath = files[i]
        hash_command = f"./hash {filePath}"
        hash_process = subprocess.Popen(hash_command, stdout=subprocess.PIPE, shell=True)
        hashed_content = hash_process.communicate()[0]
        hashed_content = (hashed_content.decode("utf-8"))
        print(f"hashed_content: {hashed_content}")
        if(i == 0):
            with open(hashed_file_path, "w") as hash_file:
                hash_file.write(hashed_content)
        else:
            with open(hashed_file_path, "a") as hash_file:
                hash_file.write(hashed_content)


def main():
    (isBoss, username) = login()
    if(isBoss):
    
    #right one
        choice = (int)(input("check log[0]\nsend nuke piece[1]\nChoice: "))
        if(choice == 0):
            log_choice = (int)(input("fail log[0]\nlogin log[1]\nChoice: "))
            if(log_choice==0):
                logName = "failLogin.txt"
            else:
                logName = "loginLog.txt"

            subprocess.run(['cat', f'logs/{logName}'])
        else:
            displayResult = displayFileName()
            selected_files = select3Files(displayResult[0], displayResult[1])
            Hash3Files(selected_files)

    else:
        #decoy 
        choice = (int)(input("check log[0]\nsend nuke piece[1]\nChoice: "))
        if(choice == 0):
            print("Log Empty")
        else:
            displayResult = displayFileName()
            selected_files = select3Files(displayResult[0], displayResult[1])
            print("NUKE PIECE SENT SUCCESSFULLY")

main()