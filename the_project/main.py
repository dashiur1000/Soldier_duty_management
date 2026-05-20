import the_project.data
from utils import is_valid_choice, find_soldier_by_id


data_file = the_project.data.soldiers_list


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
            "Here is a menu for selecting an action\n"
            "Adding a new soldier type 1\n"
            "Removing a soldier type 2\n"
            "Viewing the list of soldiers type 3\n"
            "Adding a duty to a soldier type 4\n"
            "Update and mark duty status type 5\n"
            "Printing soldier duty type 6")

def get_user_choice(message) -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש

    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    choice = input(f"Enter your choice ({message}): ")
    return choice



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
    new_soldier = get_user_choice("id_number")
    new_soldier = is_valid_choice(new_soldier, "7 numbers")
    if find_soldier_by_id(new_soldier):
        new_soldier_name = get_user_choice("name")
        data_file.append({"id": new_soldier,
        "name": new_soldier_name,
        "duties": [{"name": "guard duty",
                "day": "sunday",
                "status": "completed"},
            {"name": "kitchen duty",
                "day": "wednesday",
                "status": "pending"}]})





def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    remove_soldier = get_user_choice("id_number")
    if is_valid_choice(remove_soldier, "7 numbers"):
        if find_soldier_by_id(remove_soldier):
            remove_soldier_name = get_user_choice("name")
            for names in data_file:
                if data_file["name"] == remove_soldier_name:
                    data_file.remove(names)
                    print("The soldier was successfully deleted!")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    pass


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
    return exit()


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    show_menu()
    choice = int(get_user_choice("number"))
    if is_valid_choice(choice, "1-6_range"):
        if choice == 1:
            handle_add_soldier()
        elif choice == 2:
            handle_remove_soldier()
        elif choice == 3:
            handle_view_soldiers()
        elif choice == 4:
            handle_add_duty()
        elif choice == 5:
            handle_update_duty_status()
        else:
            handle_view_soldier_duties()
    else:
        exit_from_program()



if __name__ == "__main__":
    main()