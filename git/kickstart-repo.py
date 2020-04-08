#############################################################################
# script to initialise a git repository and assign it a number of folders   #
# author: Nathan Snelson                                                    #
# date: 08/04/2020                                                          #
#############################################################################
#boolean check for import success
flag = False

#try to import key modules
try:
    import os
except ImportError:
    print("os module not installed")
    flag = True
try:
    import git
except ImportError:
    print("gitpython module not installed")   
    flag = True

#if imports successful continue
if flag is False:
    #get current directory
    path = os.getcwd()
    
    #get contents of directory
    arr = os.listdir()

    #prompt to get repo name
    a = input("Enter your new repo name: ")

    #where input already exists in directory throw error
    if a in arr:
        print("File found with the same name!")
    elif a == "":
        print("No directory specified")
    else:
        print("Proceeding")

        #create directory, throw error if unsuccessful
        try:
            #when directory created initialise it as a git repository
            os.mkdir(a)            
            repo = git.Repo.init(a)
        except OSError:
            print("Creation of the directory {} failed".format(a))
        else:
            print("Successfully created the directory {}".format(a))
        
        #change directory to the newly created repository
        os.chdir(a)
        newDir = os.getcwd()        

        #prompt to get number of folders
        b = input("How many folders are required: ")
        i = 1

        #create folders
        while True:            
            try:
                #prompt to get the name of each folder
                c = input("Provide a name for folder {}: ".format(i))         
                os.mkdir(c)
                i = i + 1
            except OSError:
                print("Creation of the folder {} failed".format(i))
            else:
                print("Successfully created the directory {}".format(c))
            if(i > int(b)):
                #once all folders created print git status
                print(repo.git.status())
                break