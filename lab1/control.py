import help_function as H
import menu
import commands
import help_function




def Controll():
    func = help_function.Functions()
    check = menu.My_Menu()
    if (check == '1'):
        func.print_table()
        Controll()
    elif (check == '2'):
        func.insert_film()
        Controll()
    elif (check == '3'):
        func.execute_str(commands.str_between)
        Controll()
    elif (check == '4'):
        func.execute_str(commands.str_prod_from)
        Controll()
    elif (check == '5'):
        func.update_award()
        Controll()
    elif (check == '6'):
        func.delete_film()
        Controll()
    elif (check == '7'):
        findword = input("findword: \n")
        func.search1(findword)
        Controll()
    elif (check == '8'):
        print("Type your function for execute:")
        func.execute_str(input())
        Controll()
    elif (check == '0'):
        check = input("Do you want exit from program Y/N ?")
        check.lower
        if (check == "n"):
            Controll()
    else:
        Controll()

if __name__ == '__main__':
    Controll()