#Exploring Python's OS Module
#Task 1: Directory Inspector:
#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.
#Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# #Handle exceptions for invalid paths or inaccessible directories.
# List and print all files and subdirectories in the given path

import os


def add_directory():
    path2= input("What is the name of new directory? ")
  
    exist = os.path.exists(path2)
    if exist == False:
        os.makedirs((path2), exist_ok =True)
        print("Created a new directory")
    else: 
        print("Directory already exist")

def add_file():
    #adds to dir
    #with open('docs/readme.txt', 'w') as f:
    file_new=input("What is the name of the file you would like to add: ")
    try:
        dir_file =input("What directory would you like to add it to: ")
        file_dir =os.path.exists(dir_file)
  
        f = open(os.path.join((dir_file), file_new), 'w')
        print_dir=os.listdir(dir_file)
        print("Files", file_new ," has been added to: " ,dir_file)
    except FileNotFoundError:
        print("Directory does not exist")
    
  
 
    
   
       

def print_directory():
    try:
        dir_file =input("What directory would you view all folders: ")
        file_dir =os.path.exists(dir_file)
  
      
        print_dir=os.listdir(dir_file)
        print("Files", print_dir ," are in: " ,dir_file)
    except FileNotFoundError:
        print("Directory does not exist")
    

  



def main():
    while True:
    
        print("\nAdding Directory and files")
        print("1. Add new directory: ")
        print("2. Add new file: ")
        print("3. Display a directory and its files: ")
        print("4. Exit")
    
        choice=input("Plesae make a selection: ")
        if choice =="1":
            add_directory()
        elif choice =="2":
            add_file()
        elif choice =="3":
            print_directory()
        elif choice =="4":
            print("Goodbye")
            break
        else:
            print("Please make a valid selection 1-4")
        
main()
        
        