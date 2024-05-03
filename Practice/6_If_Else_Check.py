login = input('login: ')
password = input('Password: ')

if len(login) >=6 and len (password) >=8:
    #Делаю проверку на хотя бы 1 символ заглавный
    has_uper = any(char.isupper() for char in password)
    #Делаю проверку на хотя бы 1 цифру
    has_digit = any(char.isdigit() for char in password)

    if has_uper and has_digit:
        print('Вход выполнен')
    else:
        print('Ошибка: должна быть одна заглавная и хотя бы одна цифра')
else: 
    print ('Ошибка: логин должен быть не менее 6 символов, а пароль не менее 8.')