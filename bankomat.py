from datetime import datetime

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage Uzbek>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


user_info = {
    "first_name": "Sardorbek", "last_name": "Sarmanov",
    "card_password": 7777, "card_balance": 77777777,
    "card_number":9860130128304743,
    "phone_number": "", "status": False}
data_atm = {"balance": 400000}


def uzbek_balance_display():
    a = input(f"""
    Sizning balansingiz {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanishni istaysizmi?
        1. Ha
        2. Yo'q
            >>> """)

    if a == "1":
        return uzbek_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return uzbek_balance_display()


def uzbek_balance_check():
    print("Bizni tanlaganiz uchun tashakkur")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()


def uzbek_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. Ekranda ko'rish
        2. Chekda ko'rish
            >>> """)
    if services == "1":
        return uzbek_balance_display()

    elif services == "2":
        return uzbek_balance_check()


def check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Kartadan yechiladigan summa {m}
                            1. Davom etish
                            2. Bekor qilish
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("Tabriklayman amaliyot muvaffaqiyatli yakunlandi")
            return uzbek_services()

        elif tasdiq == "2":
            print(" Kechirasiz xizmat bekor qilindi")
            return uzbek_services()

        else:
            print("Xatolik !!!")
            return uzbek_service_money()

    else:
        print("Xatolik!!!")
        return main()


def uzbek_service_money():
    money = input("""
        Iltomos summani tanlang !!! :
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summa
            0. Orqaga
                >>> """)

    if money == "1":
        return check_balance(50000)

    elif money == "2":
        return check_balance(100000)

    elif money == "3":
        return check_balance(300000)

    elif money == "4":
        return check_balance(400000)

    elif money == "6":
        money = input("""Iltimos summani kiriting: """)
        return check_balance(int(money))

    elif money == "0":
        return uzbek_services()

    else:
        print("Xatolik !!!")
        return uzbek_service_money


def uz_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Telefon raqamingizni kiriting: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return uzbek_services()
        else:
            print('Xatolik')
            return uz_sms_on()
    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return uzbek_services()


def uz_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return uzbek_services()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulanmagan")
        return uzbek_services()


def uzbek_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. SMS Xabarnomani ulash
        2. SMS Xabarnomani o'chirish
            >>> """)
    if service == "1":
        return uz_sms_on()

    elif service == "2":
        return uz_sms_off()


def uzbek_service_add_money():
    print("ADD")
    money = input("Iltimos summani kiriting: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return uzbek_services()
    else:
        print("Error")
        return uzbek_service_money()


def uzbek_services():
    print("Service Page")
    services = input("""
        Xizmat turini tanglang:
            1. Balanceni ko'rish
            2. Naqt pul yechish
            3. SMS Xabarnoma
            4. Kartani to'ldirish
            0. Back
                >>> """)

    if services == "1":
        return uzbek_service_balance()

    elif services == "2":
        return uzbek_service_money()

    elif services == "3":
        return uzbek_service_sms()

    elif services == "4":
        return uzbek_service_add_money()

    elif services == "0":
        print("Siz bizni tanlab to'g'ri ish tutdingiz!")
        return main()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()


def uzbek():
    print("<<<<<<<<<<<<<<Uzbek Lenguage>>>>>>>>>>>>>>>>")
    password = int(input("Pin codeni kiriting: "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("Pin codeni kiriting: "))
        n -= 1

    if user_info["card_password"] == password:
        return uzbek_services()

    print("Kechirasiz sizning Kartangiz bloklandi")
    return main()




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage English>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def english_balance_display():
    a = input(f"""
    Your balance  {user_info["card_balance"]} sum
    Do you want to use another service
        1. Yes
        2. No
            >>> """)

    if a == "1":
        return english_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return english_balance_display()


def english_balance_check():
    print("You did the right thing by choosing us !!!")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()


def english_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. View on screen
        2. Check out
            >>> """)
    if services == "1":
        return english_balance_display()

    elif services == "2":
        return english_balance_check()


def english_check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Amount debited from the card {m}
                            1. Continue
                            2. Cancellation
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("The operation was completed  successfully ")
            return english_services()

        elif tasdiq == "2":
            print("Service canceled")
            return english_services()

        else:
            print("Error")
            return english_service_money()

    else:
        print("Error!!!")
        return main()


def english_service_money():
    money = input("""
        Select an amount:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Another amount
            0. Back
                >>> """)

    if money == "1":
        return english_check_balance(50000)

    elif money == "2":
        return english_check_balance(100000)

    elif money == "3":
        return english_check_balance(300000)

    elif money == "4":
        return english_check_balance(400000)

    elif money == "6":
        money = input("""Please enter the amount !!!: """)
        return english_check_balance(int(money))

    elif money == "0":
        return english_services()

    else:
        print("Error")
        return english_service_money


def eng_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Enter your phone number: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return english_services()
        else:
            print('Please error')
            return eng_sms_on()
    else:
        print("SMS notification is already connected to this number")
        return english_services()


def eng_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return english_services()

    else:
        print("There is no SMS notification already connected to this number")
        return english_services()


def english_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. Connect SMS Notification
        2. Delete SMS Notification
            >>> """)
    if service == "1":
        return eng_sms_on()

    elif service == "2":
        return eng_sms_off()


def english_service_add_money():
    print("ADD")
    money = input("Please enter the amount !!!: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return english_services()
    else:
        print("Error")
        return english_service_money()


def english_services():
    print("Service Page")
    services = input("""
        Please select a service type !!!:
            1. Check balance
            2. Would you like to withdraw cash?
            3. SMS notification
            4. Filling the card
            0. Back
                >>> """)

    if services == "1":
        return english_service_balance()

    elif services == "2":
        return english_service_money()

    elif services == "3":
        return english_service_sms()

    elif services == "4":
        return english_service_add_money()

    elif services == "0":
        print("You did the right thing by choosing us !!!")
        return main()

    else:
        print("This type of service does not exist")
        return english_services()


def english():
    print("<<<<<<<<<<<<<<English Lenguage>>>>>>>>>>>>>>>>")
    password = int(input("Please enter pin code !!! : "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("Please enter pin code !!! : "))
        n -= 1

    if user_info["card_password"] == password:
        return english_services()

    print("Sorry, your account has been blocked")
    return main()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Russian>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def russian_balance_display():
    a = input(f"""
    Ваш баланс {user_info["card_balance"]} сум
    Хотите воспользоваться другой услугой?
        1. ДА
        2. НЕТ
            >>> """)

    if a == "1":
        return russian_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return russian_balance_display()


def russian_balance_check():
    print("Вы правильно сделали, что выбрали нас!!!")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()


def russian_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. Просмотр на экране
        2. Посмотреть на чеке
            >>> """)
    if services == "1":
        return russian_balance_display()

    elif services == "2":
        return russian_balance_check()


def ru_check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Сумма списанная с карты {m}
                            1. Продолжение
                            2. Отмена
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("Операция завершилась успешно")
            return russian_services()

        elif tasdiq == "2":
            print("Услуга отменена")
            return russian_services()

        else:
            print("Ошибка!!!")
            return russian_service_money()

    else:
        print("Ошибка!!!")
        return main()


def russian_service_money():
    money = input("""
        Выберите сумму:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Другая сумма
            0. Назад
                >>> """)

    if money == "1":
        return ru_check_balance(50000)

    elif money == "2":
        return ru_check_balance(100000)

    elif money == "3":
        return ru_check_balance(300000)

    elif money == "4":
        return ru_check_balance(400000)

    elif money == "6":
        money = input("""Введите сумму: """)
        return ru_check_balance(int(money))

    elif money == "0":
        return russian_services()

    else:
        print("Error")
        return russian_service_money


def ru_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Введите свой номер телефона: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return russian_services()
        else:
            print('Ошибка !!!')
            return ru_sms_on()
    else:
        print("СМС-уведомление уже подключено к этому номеру")
        return russian_services()


def ru_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return russian_services()

    else:
        print("На этот номер уже не подключено SMS-уведомление")
        return russian_services()


def russian_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. Подключите СМС-уведомление
        2. Удалить SMS-уведомление
            >>> """)
    if service == "1":
        return ru_sms_on()

    elif service == "2":
        return ru_sms_off()


def russian_service_add_money():
    print("ADD")
    money = input("Введите сумму: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return russian_services()
    else:
        print("Error")
        return russian_service_money()


def russian_services():
    print("Service Page")
    services = input("""
        Выберите тип услуги::
            1. Посмотреть баланс
            2. Вывести денег
            3. SMS-уведомление
            4. Заполнение карты
            0. назад
                >>> """)

    if services == "1":
        return russian_service_balance()

    elif services == "2":
        return russian_service_money()

    elif services == "3":
        return russian_service_sms()

    elif services == "4":
        return russian_service_add_money()

    elif services == "0":
        print("Вы правильно сделали, что выбрали нас!!!")
        return main()

    else:
        print("К сожалению, такого типа услуг не существует")
        return russian_services()


def russian():
    print("<<<<<<<<<<<<<<Russian Lenguage>>>>>>>>>>>>>>>>")
    password = int(input("Пожалуйста, введите свой пин-код: "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("Пожалуйста, введите свой пин-код: "))
        n -= 1

    if user_info["card_password"] == password:
        return russian_services()

    print("Извините, ваша карта заблокирована")
    return main()




def main():
    lenguage = input("""
        Tilni tanglang:
            1. Uzbek
            2. English
            3. Russian
                >>> """)

    if lenguage == "1":
        return uzbek()

    elif lenguage == "2":
        return english()

    elif lenguage == "3":
        return russian()


    else:
        print("Bunday til mavjud emas")
        return main()



if __name__ == "__main__":
    main()
