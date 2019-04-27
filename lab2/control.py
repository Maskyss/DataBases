import menu
from db.queries import Database
import input_entity as in_en


db = Database()



def Controll():

    check = menu.My_Menu()
    if (check == '1'):
        in_en.get_all(in_en.get_entity(), db)
        Controll()
    elif (check == '2'):
        in_en.input_film(db)
        Controll()
    elif (check == '3'):
        in_en.update_film(db)
        Controll()
    elif (check == '4'):
        in_en.get_all(1, db)
        inp=input("what film delete input id: \n")
        db.delete_film(inp)
        Controll()
    elif (check == '5'):
        findword = input("findword in films title | producer: \n")
        req = db.search(findword)
        print(req)
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