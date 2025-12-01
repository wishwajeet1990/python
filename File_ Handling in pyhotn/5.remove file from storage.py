import os as cmd
file = open(r"D:\Python\Codding\File_ Handling\ my_file_4.txt","w")
file.close()
if cmd.path.exists(r"D:\Python\Codding\File_ Handling\ my_file_4.txt"):
    print("File Exists")
    print("Do you want to remove the file please enter your choice 'y' or 'n")
    rep = input()
    if rep == "y" or rep == "Y":
        cmd.remove(r"D:\Python\Codding\File_ Handling\ my_file_4.txt")
        print("After removal of File do you want to check the file exists or not please enter your choice 'y' or 'n")
        rep = input()
        if rep == "y" or rep == "Y":
            if cmd.path.exists(r"D:\Python\Codding\File_ Handling\ my_file_4.txt"):
                print("File Exists")
            else:
                print("File not Found")
        else:
            print("You Didn't Try to check the file existence ")
    else:
        print("File not Removed")
else:
    print("File not Found")
print("End OF Programme")