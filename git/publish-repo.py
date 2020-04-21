#############################################################################
# script to push a git repository to the remote repo                        #
# author: Nathan Snelson                                                    #
# date: 18/04/2020                                                          #
#############################################################################
#boolean check for import success
flag = False

#try to import required modules
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

#if imports successful continue
if flag is False:    
    a = input("Enter the repository location: ")
    
    try:
        os.chdir(a)
    except OSError:
        print(colored("Couldn't locate directory","red"))
    else:
        print(colored("Directory {} found, proceeding".format(a),"green"))

        b = input("Is this repo ready to be published?(Y/N) ")
        if b == "Y":
            r = git.Repo

            print("The following folders will be pushed:")
            d = os.listdir()
            for item in d:
                print(colored("- {}".format(item),"blue"))
                        
            os.system('ls')
            
            c = input("Proceed with push?(Y/N) ")
            if c == "Y":
                m = input("Enter a commit message: ")
                if m != None:
                    cmd = "git add ."
                    os.system(cmd)
                    
                else:
                    r.commit("New Commit!")                       
        else:
            print(colored("Push has been cancelled","red"))