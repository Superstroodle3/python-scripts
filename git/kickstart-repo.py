#############################################################################
# script to initialise a git repository and assign it a number of folders   #
# author: Nathan Snelson                                                    #
# date: 09/04/2020                                                          #
#############################################################################
#boolean check for import success
flag = False

#try to import key modules
try:
    from colorama import init
except ImportError:
    print("colorama module not installed")
    flag = True
try:
    from termcolor import colored
except ImportError:
    print("termcolor module not installed")
    flag = True
try:
    import os
except ImportError:
    print(colored("os module not installed","red"))
    flag = True
try:
    import git
except ImportError:
    print(colored("gitpython module not installed","red"))
    flag = True

#initialise print colours
init()

#function to create folders
def createFolder(name):
    try:      
        os.mkdir(name)
    except OSError:
        print(colored("Creation of {} failed".format(name),"red"))
    else:
        print(colored("Successfully created {}".format(name),"green"))

#if imports successful continue
if flag is False:
    #get current directory    
    c = input("Enter the directory the new repo will be created in: ")

    try:
        os.chdir(c)
    except OSError:
        print(colored("Directory doesn't exist!","red"))
    else:
        print(colored("Successfully found directory","green"))
        #get contents of chosen directory
        arr = os.listdir()

        #prompt to get repo name
        a = input("Enter your new repo name: ")

        #where input already exists in directory throw error
        if a in arr:
            print(colored("File found with the same name!","red"))
        elif a == "":
            print(colored("No directory specified","yellow"))
        else:
            print(colored("Proceeding","green"))

            #create directory, throw error if unsuccessful
            try:
                #when directory created initialise it as a git repository
                os.mkdir(a)            
                repo = git.Repo.init(a)
            except OSError:
                print(colored("Creation of {} failed".format(a),"red"))
            else:
                print(colored("Successfully created {}".format(a),"green"))
            
            #change directory to the newly created repository
            os.chdir(a)
            newDir = os.getcwd()        

            #prompt to get number of folders
            b = input("How many folders are required: ")
            i = 1

            #create folders
            while True:                        
                #prompt to get the name of each folder
                c = input("Provide a name for folder {}: ".format(i))
                #pass name into function
                createFolder(c)                
                i = i + 1
                if(i > int(b)):
                    #once all folders created print git status
                    print(repo.git.status())
                    break