from datetime import date





def current_date():
    today = str(date.today())
    print(len(today))
    return today


print(current_date())
