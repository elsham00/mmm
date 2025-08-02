import time 
print("кош келиниз ойунга, сизде 2 эшик бар кайсынысын тандайсыз(1 ак, 2кара)")
("эки эшиктин биросун танда:")
time.sleep(1)
print("--1 ак")
time.sleep(1)
print("--2 кара")
user = input("1 же 2")
if user == '2':
    time.sleep(2)

    print(" сиз эшикти ачтыз ")
    print("сизде 3 тандо бар")
    print("/1 кылыч:")
    print("/2 бычак: ")
    print("/3 эт")
    user2 = input("1же, же2, 3бу:")
    if user2 =='1':
        print("колуна кылыч алды:")
    elif user2 == "2":
        print("колуна бычак алды:")
    elif user2 == '3':
        time.sleep(3)
        print(" сиз эти алдыныз:")
        print("сизде 4 жаныбар бар")
        print("1 Арыстан")
        print("2 Жолборс:")
        print("3 Балык:")
        print("4 Буркут:")
        user3 = input("1би, 2же, 3ко: ")
        if user3("1"):
            print("арстандан олдун")
        
        elif user3("2"):
            print("Жолборс сизди олтурду")

        elif user3("3"):
            print("балык сиз отуз")

        elif user3("4"):
            print("этинизди жедирип койдус бирок отус")
            print("сизде 2 тандо бар")
            user4 =input("1 карышкыр, 2 кракадил")
            if user4 ("1"):
              print("сизде эт жок: ")
        elif user4 ("2"):
            print("этин жок чыгып кете бер")

        

        
