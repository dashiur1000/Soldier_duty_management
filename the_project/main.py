# Link to GitHub:
# https://github.com/dashiur1000/Soldier_duty_management

import the_project.data
from utils import is_valid_choice, find_soldier_by_id, is_valid_day, is_valid_status, is_valid_name
from soldier_manager import get_all_soldiers, add_soldier, remove_soldier
from duty_manager import get_soldier_duties, add_duty_to_soldier,update_duty_status


data_file = the_project.data.soldiers_list
is_true = True


def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.

    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)

    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("==========================================\n"
        "Welcome to the unit's central duty system!\n"
            "==========================================\n"
            "  Here is a menu for selecting an action:\n"
            "Adding a new soldier type..............(1)\n"
            "Removing a soldier type................(2)\n"
            "Viewing the list of soldiers type......(3)\n"
            "Adding a duty to a soldier type........(4)\n"
            "Update and mark duty status type.......(5)\n"
            "Printing soldier duty type.............(6)")

def get_user_choice(message) -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש

    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    choice = input(f"Enter your {message}: ")
    return str(choice)



def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    new_soldier_id = get_user_choice("id_number")
    if is_valid_choice(new_soldier_id, "7 numbers"):
        if find_soldier_by_id(int(new_soldier_id), data_file) == None:
            new_soldier_name = get_user_choice("name")
            if is_valid_choice(new_soldier_name, "name"):
                add_soldier(int(new_soldier_id), new_soldier_name, data_file)
                print(data_file)
                exit_from_program()
    return None





def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    remove_soldier_id = get_user_choice("id_number")
    if is_valid_choice(remove_soldier_id, "7 numbers"):
        remove_soldier_name = get_user_choice("name")
        if is_valid_choice(remove_soldier_name, "name"):
            if is_valid_name(remove_soldier_name):
                if find_soldier_by_id(int(remove_soldier_id), data_file):
                    remove_soldier(int(remove_soldier_id), data_file)
                    print("The soldier was successfully deleted!")
                    exit_from_program()
                else:
                    raise ValueError("ValueError! id not found!")
            else:
                raise ValueError("ValueError! this name is not valid!")
        else:
            raise ValueError("ValueError! this name is not valid!")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    get_all_soldiers(data_file)
    exit_from_program()


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = get_user_choice("id_number")
        if is_valid_choice(soldier_id, "7 numbers"):
            if find_soldier_by_id(int(soldier_id), data_file):
                duty_name = get_user_choice("duty_name")
                if is_valid_choice(duty_name, "name"):
                    day = get_user_choice("day")
                    if is_valid_choice(day, "name"):
                        if is_valid_day(day):
                            add_duty_to_soldier(int(soldier_id), duty_name, day, data_file)
                            print("Soldier duty has been successfully added!")
    except ValueError as e:
        print(e)




def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = get_user_choice("id_number")
        if is_valid_choice(soldier_id, "7 numbers"):
            if find_soldier_by_id(int(soldier_id), data_file):
                duty_name = get_user_choice("duty_name")
                if is_valid_choice(duty_name, "name"):
                    day = get_user_choice("day")
                    if is_valid_choice(day, "name"):
                        if is_valid_day(day):
                            new_status = get_user_choice("new status")
                            if is_valid_status(new_status):
                                update_duty_status(int(soldier_id), duty_name, new_status, data_file)
                                print("Duty status has been updated successfully!")

    except:
        raise ValueError("ValueError! try again!")




def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    id_soldier = get_user_choice("id_number")
    if is_valid_choice(id_soldier, "7 numbers"):
        print(get_soldier_duties(int(id_soldier), data_file))
        exit_from_program()





def exit_from_program():
    print("Do you want to log out?")
    a = True
    while a == True:
        choice = get_user_choice("yes or no")
        if is_valid_choice(choice, "yes or no"):
            if choice == "yes":
                print("You are logged out!")
                exit()
            else:
                a = False
                return is_true
        a = True




def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while is_true == True:
        show_menu()
        choice = (get_user_choice("number"))
        if is_valid_choice(choice, "1-6_range"):
            if choice == "1":
                handle_add_soldier()
            elif choice == "2":
                handle_remove_soldier()
            elif choice == "3":
                handle_view_soldiers()
            elif choice == "4":
                handle_add_duty()
            elif choice == "5":
                handle_update_duty_status()
            else:
                handle_view_soldier_duties()


if __name__ == "__main__":
    main()