# Link to GitHub:
# https://github.com/dashiur1000/Soldier_duty_management

import the_project.data
from utils import is_valid_choice, find_soldier_by_id
from soldier_manager import get_all_soldiers, add_soldier, remove_soldier


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
            if find_soldier_by_id(int(remove_soldier_id), data_file):
                remove_soldier(int(remove_soldier_id), data_file)
                print("The soldier was successfully deleted!")
                exit_from_program()


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
    pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def exit_from_program():
    print("Do you want to log out?")
    choice = get_user_choice("yes or no")
    is_valid_choice(choice, "yes or no")
    if choice == "yes":
        print("You are logged out!")
        exit()
    else:
        return is_true


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