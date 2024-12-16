import os
def shutdown () :
    choice = input("If you want to shutdown you computer than type 'Yes' and if you don't want to shut your computer than type 'No': ")
    if choice == 'Yes' :
        print("Your computer is shuting down in 3 seconds...")
        os.system("shutdown /s /t 3")
    elif choice == 'No' :
        print("It seems like you don't want to shutdown your computer so we are not shuting down your computer...")
    else :
        print("Invalid input")
shutdown()