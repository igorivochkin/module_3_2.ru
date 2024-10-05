# module_3_2.ru

def ad_ver(addres_):
    for i in range(len(addres_)):
        if addres_[i] == '@':
            if (addres_[len(addres_)-4:] == '.com'
                    or addres_[len(addres_)-4:] == '.net'
                    or addres_[len(addres_)-3:] == '.ru'):
                return True
            else:
                return False

def send_email(message, recipient,*, sender="university.help@gmail.com"):
    if ad_ver(recipient) == False or ad_ver(sender) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
