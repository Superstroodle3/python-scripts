#############################################################################
# script to clear temp files on windows                                     #
# author: Nathan Snelson                                                    #
# date: 21/04/2020                                                          #
#############################################################################
#boolean check for import success
flag = False

#try to import required modules
try:
    import os
except ImportError:
    print("os module not installed")
    flag = True

try:
    import shutil
except ImportError:
    print("shutil module not installed")
    flag = True

#if imports successful continue
if flag is False:
    #build path for temp
    homedir = os.path.expanduser("~")
    a = os.path.join(homedir,'AppData','Local','Temp')

    #change directory to temp
    try:
        os.chdir(a)
    except OSError:
        print("Couldn't locate directory {}".format(a))
    else:
        b = os.getcwd()
        print("Directory found!")

        #delete files/ directories within temp
        for filename in os.listdir(b):
            file_path = os.path.join(b, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))