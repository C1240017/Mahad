def main():
    name_list=[]
    print("Choose (1-5):")
    while True:
        print("1) Add Name.")
        print("2) Modify Name.")
        print("3) Remove Name.")
        print("4) View Name.")
        print("5) Exit.")

        choice=input("enter your choice (1-5):")

        if choice == "1":
            name=input("enter a name:")
            name_list.append(name)
            print(name_list)
            print()

        elif choice == "2":
            nam_in_list=input("enter a name in list:")
            if nam_in_list in name_list:
                index=name_list.index(nam_in_list)
                new_name=input("enter a new name:")
                name_list[index]=new_name
                print(name_list)
            else:
                print("not found.")
            print()
            
        elif choice == "3":
            remove_name=input("enter name you want to remove:")
            if remove_name in name_list:
                name_list.remove(remove_name)
                print(name_list)
            else:
                print("not found.")
            print()
            
        elif choice == "4":
            name_list.sort()
            for name in name_list:
                print(name)
            print()
            
        elif choice == "5":
            print("Thank you.")
            break
        else:
            print("Invalid choice. pleas enter a number between (1-5)")
main()