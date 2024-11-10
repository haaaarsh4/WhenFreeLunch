import subprocess
from getpass import getpass

f = open("TempPassword.txt", "w")

dict = {"General Batman" : "4e63be1122d51e7cc915512588a06e9bd1ea60cbe59ba3b40dce00cde2dac23", 
        "Colonel Spiderman" : "1e7cf8c7a52ad61ca65e9403ebef462bcf4c85c0a9b01c1726ace07f9b14ecac", 
        "President Trump  " : "ec4b5a41fbac55548db79a0d2db9abab37c60026adc6636e3f9c0a64411c7f42"}

# passwords: AlfredisCute, TonyDead， IMissBiden

### Login Page

print("-------- MARS INTEL AGENCY LOGIN SYSTEM --------")
print("------------------------------------------------ ")
username = input("Enter Username: ")
while (username not in dict.keys()):
    print("INVALID USERNAME, AGAIN")
    username = input("Enter Username: ")
password = getpass("Enter Password: ")

f.write(password)
f.close()

command = "./hash TempPassword.txt"
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
hashed_pass = process.communicate()[0]
hashed_pass = (hashed_pass.decode("utf-8"))

isBoss = False
count = 0
while (hashed_pass != dict[username] and count < 3):
    password = getpass("Wrong Password, re-enter Password: ")

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