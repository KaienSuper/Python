month_ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
            "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
month_en = ["januar", "february", "march", "april", "may", "june", "jule",
            "august", "september", "october", "november", "december"]
def month_name(count, language):
    if language == "ru":
        return month_ru[count - 1]
    elif language == "en":
        return month_en[count - 1]
print(month_name(3, "en"))
print(month_name(3, "ru"))