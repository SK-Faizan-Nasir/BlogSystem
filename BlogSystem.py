'''
Admin - login/logout, publish, deleting
User - login/logout, publish
'''
import os,fnmatch
aid = "Anil"
apassword = 123

userid = "Farman"
upassword = 123

print("\t\t\t\t\t Welcome To Anil's Blog System\n")
def admin():
    while(True):
        print("\n\t\t\t\t\t Press '1' for Login"
              "\n\t\t\t\t\t Press '2' to get back to main menu")
        admin_main_choice = int(input("\t\t\t\t\t Please enter your choice"))
        if admin_main_choice==1:
            adminid = input("\n\t\t\t\t\t Enter your ID").capitalize()
            if aid==adminid:
                adminpass = int(input("\n\t\t\t\t\t Enter your PassCode"))
                if apassword==adminpass:
                    print(aid," Login sucessful")
                    while(True):
                        print("\n\t\t\t\t\t Press '1' to publish a blog"
                              "\n\t\t\t\t\t Press '2' to delete a blog"
                              "\n\t\t\t\t\t Press '3' to read a blog"
                              "\n\t\t\t\t\t Press '4' to logout")
                        fchoice = int(input("Please enter your choice"))
                        if fchoice==1:
                            name = input("Title of the blog with extension").capitalize()
                            f = open(name,'w')
                            print("The file has been create please fill in the contents")
                            content = input()
                            f.write(content)
                            f.close()
                        elif fchoice==2:
                            print("Enter the name of the blog that you want to delete with extension")
                            delete_name = input().capitalize()
                            if os.path.exists(delete_name):
                                os.remove(delete_name)
                                print("The file ",delete_name," has been deleted")
                            else:
                                print("File does not exists")
                        elif fchoice == 3:
                            read_choice = input("Please enter the file name to be read along with the extension").capitalize()
                            if os.path.exists(read_choice):
                                f = open(read_choice,'r')
                                print(f.read())
                            else:
                                print("File does not exists")
                        elif fchoice == 4:
                            break
                        else:
                            print("Please select item from the menu")
                else:
                    print("\n\t\t\t\t\t Wrong password")
            else:
                print("\n\t\t\t\t\t Wrong ID Please try again")
        elif admin_main_choice == 2:
            print("You have successfully logged out")
            break
        else:
            print("Wrong Choice")


def user():
    while (True):
        print("\n\t\t\t\t\t Press '1' for Login"
              "\n\t\t\t\t\t Press '2' to get back to main menu")
        user_main_choice = int(input("\t\t\t\t\t Please enter your choice"))
        if user_main_choice == 1:
            uid = input("\n\t\t\t\t\t Enter your ID").capitalize()
            if uid == userid:
                userpass = int(input("\n\t\t\t\t\t Enter your PassCode"))
                if upassword == userpass:
                    print("Login sucessful")
                while (True):
                    print("\n\t\t\t\t\t Press '1' to publish a blog"
                          "\n\t\t\t\t\t Press '2' to delete a blog"
                          "\n\t\t\t\t\t Press '3' to read a blog"
                          "\n\t\t\t\t\t Press '4' to logout")
                    fchoice = int(input("Please enter your choice"))
                    if fchoice == 1:
                        name = input("Title of the blog with extension").capitalize()
                        f = open(name, 'w')
                        print("The file has been create please fill in the contents")
                        content = input()
                        f.write(content)
                        f.close()
                    elif fchoice == 2:
                        print("Enter the name of the blog that you want to delete with extension")
                        delete_name = input().capitalize()
                        if os.path.exists(delete_name):
                            os.remove(delete_name)
                            print("The file ", delete_name, " has been deleted")
                        else:
                            print("File does not exists")
                    elif fchoice == 3:
                        read_choice = input(
                            "Please enter the file name to be read along with the extension").capitalize()
                        if os.path.exists(read_choice):
                            f = open(read_choice, 'r')
                            print(f.read())
                        else:
                            print("File does not exists")
                    elif fchoice == 4:
                        break
                    else:
                        print("Please select item from the menu")
                else:
                    print("\n\t\t\t\t\t Wrong password")
            else:
                print("\n\t\t\t\t\t Wrong ID Please try again")
        elif user_main_choice == 2:
            break
        else:
            print("Wrong Choice")


while(True):
    print("\n\t\t\t\t\tPress '1' for the admin section"
          "\n\t\t\t\t\tPress '2' for the user section"
          "\n\t\t\t\t\tPress '3' to quit the app")

    main_choice = int(input("\n\t\t\t\t\t Enter your choice"))
    if main_choice==1:
        admin()
    elif main_choice==2:
        user()
    elif main_choice==3:
        print("Thanks for using the app")
        break
    else:
        print("Please select an option from the menu")