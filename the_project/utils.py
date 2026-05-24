def find_soldier_by_id(soldier_id: int, data, is_true = True) -> dict | None:
    """
    מחפשת חייל לפי id ומחזירה אותו.

    סוג: פונקציית עזר (Helper Function)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        dict | None: מילון של החייל אם נמצא, None אם לא נמצא

    זורקת: כלום - מחזירה None במקרה שלא נמצא

    למה הפונקציה קיימת:
    פונקציה זו משמשת הרבה מקומות במערכת (DRY).
    במקום לחזור על לולאת חיפוש בכל פונקציה,
    יש פונקציה אחת שעושה את זה.
    מחזירה None במקום לזרוק exception - מאפשרת גמישות.
    """
    for item in data:
        if item["id"] != int(soldier_id):
            continue
        return item


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    מחפשת תורנות לפי שם ברשימת תורנויות.

    סוג: פונקציית עזר (Helper Function)

    מקבלת:
        duties (list): רשימת תורנויות
        duty_name (str): שם התורנות לחיפוש

    מחזירה:
        dict | None: מילון של התורנות אם נמצאה, None אם לא נמצאה

    זורקת: כלום - מחזירה None במקרה שלא נמצא

    למה הפונקציה קיימת:
    פונקציה זו משמשת במספר מקומות (הוספת תורנות, עדכון סטטוס).
    הפרדה של לוגיקת החיפוש למקום אחד.
    מחזירה None במקום לזרוק exception - מאפשרת גמישות.
    """
    for item in duties:
        if duty_name in item:
            return item
    return None


def is_valid_status(status: str) -> bool:
    """
    בודקת אם סטטוס הוא חוקי.

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        status (str): הסטטוס לבדיקה

    מחזירה:
        bool: True אם הסטטוס חוקי (pending/completed/missed)
              False אם לא חוקי

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של סטטוס משמשת במספר מקומות.
    במקום לחזור על הבדיקה, יש פונקציה אחת.
    גם מקל על שינוי הסטטוסים החוקיים בעתיד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    if status in ["pending", "completed", "missed"]:
        return True
    raise ValueError("ValueError")


def is_valid_name(name: str) -> bool:
    """
    בודקת אם שם הוא תקין (לא ריק).

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        name (str): השם לבדיקה

    מחזירה:
        bool: True אם השם תקין (לא ריק)
              False אם ריק

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של שם משמשת במספר מקומות.
    הפרדה של לוגיקת הבדיקה למקום אחד.
    בעתיד אפשר להוסיף בדיקות נוספות (אורך מינימלי, תווים חוקיים).
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    name = name.lower()
    name_without_space = name.replace(" ", "")
    if len(name) >= 2 and name_without_space.isalpha():
        return True
    return False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    בודקת אם לחייל יש תורנות עם שם מסוים.

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        soldier (dict): מילון של חייל
        duty_name (str): שם התורנות לבדיקה

    מחזירה:
        bool: True אם התורנות קיימת לחייל
              False אם לא קיימת

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקה זו משמשת בהוספת תורנות (למנוע כפילויות).
    הפרדה של הלוגיקה למקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    for key, value in soldier.items():
        if value == duty_name:
            return True
    return False


def is_valid_day(day: str) -> bool:
    """
    בודקת אם יום הוא חוקי (לא שישי או שבת).

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        day (str): היום לבדיקה

    מחזירה:
        bool: True אם היום חוקי (sunday-thursday)
              False אם לא חוקי או אסור (friday/saturday או ערך לא תקין)

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של יום משמשת בהוספת תורנות.
    הפרדה של לוגיקת הבדיקה למקום אחד.
    בעתיד אפשר לשנות את הימים החוקיים במקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    if day in ["sunday", "monday", "tuesday", "wednesday", "thursday"]:
        return True
    raise ValueError("ValueError")


def is_valid_choice(choice, test_type):
    """
    פונקצייה הבודקת אם מה שהמשתמש הזין תואם למה שהתבקש

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
    מה שהמשתמש הזין
    הסוג המשתמש התבקש להזין

    מחזירה:
        bool: True אם הערך חוקי
              False אם לא חוקי או אסור (או ערך לא תקין)

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של הזנת המשתמש.
    הפרדה של לוגיקת הבדיקה למקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    try:
        if test_type == "1-6_range":
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return True
            print("ValueError")

        elif test_type == "7 numbers":
            if int(len(choice)) == 7 and choice.isdigit():
                return True
            print("ValueError")

        elif test_type == "name":
            choice = choice.lower()
            name_without_space = choice.replace(" ", "")
            if len(choice) >= 2 and name_without_space.isalpha():
                return True
            raise ValueError("ValueError")

        elif test_type == "yes or no":
            if choice in ["yes", "no"]:
                return True
            raise ValueError("ValueError")

    except ValueError as e:
        print(e)
        return False

    return False