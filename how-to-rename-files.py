# import os module
import os
import string

# define rename files function


def file_rename():
    # get files
    file_list = os.listdir("D:/python-workouts/prank")
    # print(file_list)
    save_path = os.getcwd()
    print("Current drive is: " + save_path)
    os.chdir("d:\python-workouts\prank")
    new_path = os.getcwd()
    # rename files
    print("New path is: " + new_path)

    for file_name in file_list:
        #remove_digits = str.maketrans('','','0123456789')
        # file_name.translate(remove_digits)
        # os.rename(file_name, file_name.translate(
        #  {ord(k): None for k in '0123456789'}))
        # print(file_name)

        removed_digits = ''.join(
            file_name for file_name in file_list if not file_name.isdigit())
        os.rename(file_name, removed_digits)
        os.chdir(new_path)


# call/initiate function
file_rename()
