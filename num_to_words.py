def convert_hundreds(num):
    ones = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    tens = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    hundreds = ["", "یکصد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
    teens = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]

    if num == 0:
        return ""
    
    word = ""
    
    if num >= 100:
        word += hundreds[num // 100]
        num %= 100
        if num > 0:
            word += " و "

    if 10 <= num < 20:
        word += teens[num - 10]
    elif num >= 20:
        word += tens[num // 10]
        if num % 10 != 0:
            word += " و " + ones[num % 10]
    else:
        word += ones[num]
    
    return word.strip()

def convert_to_letters(num):
    if num == 0:
        return "صفر"

    if num < 1000:
        return convert_hundreds(num)

    # Add suffixes for thousands, millions, billions, etc.
    units = ["", " هزار", " میلیون", " میلیارد", " تریلیون"]
    
    words = []
    unit_index = 0

    while num > 0:
        if num % 1000 != 0:
            words.append(convert_hundreds(num % 1000) + units[unit_index])
        num //= 1000
        unit_index += 1

    # Join parts with " و " (and)
    return " و ".join(reversed(words)).strip()

print(convert_to_letters(999999))