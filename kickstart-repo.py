import subprocess
import os
import git

path = os.getcwd()
arr = os.listdir()

a = input("Enter your new repo name: ")

if a in arr:
    print("File found with the same name!")
elif a is None:
    print("No directory specified")
else:
    print("Proceeding")
    
    try:
        os.mkdir(a)
    except OSError:
        print ("Creation of the directory %s failed" % a)
    else:
        print ("Successfully created the directory %s " % a)
    
    os.chdir(a)
    newDir = os.getcwd()
    print(newDir)

    b = input("How many folders are required: ")
    i = 1
    while True:        
        #print(i)
        i = i + 1
        try:
            c = input("Provide a name: ")         
            os.mkdir(c)
            print(c)
        except OSError:
            print("Creation of the folder %s failed" % c)
        else:
            print("Successfully created the directory %s " % c)        
        if(i > int(b)):                
            repo = git.Repo.init(a)
            print(repo.git.status())
            break