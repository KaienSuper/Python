profiles_dict = {}
def setup_profile(name, vacation_dates):
    profiles_dict[name] = vacation_dates

def print_application_for_leave(name):
    print(f"Заявление на отпуск в период {profiles_dict[name]}. {name}")

def print_holiday_money_claim(money, name):
    print(f"Прошу выплатить {money} отпускных денег. {name}")

def print_attorney_letter(name_vice, name):
    print(f"На время отпуска в период {profiles_dict[name]} \n моим заместителем назначается {name_vice}")

setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave("Иван Петров")
print_application_for_leave("Иван Петров")
print_holiday_money_claim("15 тысяч пиастров", "Иван Петров")
print_attorney_letter("Василий Васильев", "Иван Петров")
