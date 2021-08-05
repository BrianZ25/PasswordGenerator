import random
import string

try:
    passwordFile = open("PasswordList.txt", "r+")
    if passwordFile.readlines() == "Password List:":
        passwordFile.close();
    else:
        passwordFile.write("Password List:")
        passwordFile.close();
except:
    createFile = open("PasswordList.txt", "w")
    createFile.write("")
    createFile.close()
    print("File was not found before hand, but a new file has been created. Close and relaunch the program.")

passwordFile = open("PasswordList.txt", "a");

length = input("How many characters is the password? ");

try:
    i = int(length);
    applicationName = input("What is this application for? ");
    passwordFile.write("\n"+applicationName+" - ");
    specialChar = input("Do you want to include special characters into your password? Respond with either yes or no ");
    if (specialChar == "yes"):
        for letters in range(0,i):
            passwordFile.write(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation));
    elif (specialChar == "no"):
        for letters in range(0,i):
            passwordFile.write(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits));
    else:
        print("Remember to respond specifically with \"yes\" or \"no\"");
except:
    print("Error has occurred, please make sure that an integer was entered");

print("Password has been generated and logged to the text file");
passwordFile.close;


