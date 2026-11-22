import requests
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ["GET", "POST", "PUT", "DELETE"]

# 1. http-запросы без параметра method
print("1. http-запросы без параметра method")
for method in methods:
    response = requests.request(method, url)
    print(f"{method} : {response.text}")
print()


# 2. http-запрос не из списка [POST, GET, PUT, DELETE]
print("2. http-запрос не из списка [POST, GET, PUT, DELETE]")
response_head = requests.head(url)
print(f"HEAD: status code - {response_head.status_code}\n")


# 3. http-запросы c правильным параметром method
print("3. http-запросы c правильным параметром method")
for method in methods:
    if method == "GET":
        response = requests.request(method, url, params={"method": method})
        print(f"{method} : {response.text}")
    else:
        response = requests.request(method, url, data={"method": method})
        print(f"{method} : {response.text}")
print()


# 4. Цикл перебора всех возможных сочетаний реальных типов запроса и значений параметра method
print("4. Цикл перебора всех возможных сочетаний реальных типов запроса и значений параметра method")
flag = False
for req_method in methods:
    print(f"Тип запроса: {req_method}")
    for param_method in methods:
        if req_method == "GET":
            response = requests.request(req_method, url, params={"method": param_method})
        else:
            response = requests.request(req_method, url, data={"method": param_method})

        if (req_method == param_method) and (response.text != '{"success":"!"}'):
            print(f"\t Аномалия при значении параметра method = {param_method} : {response.text}")
            flag = True
        if (req_method != param_method) and (response.text != "Wrong method provided"):
            print(f"\t Аномалия при значении параметра method = {param_method} : {response.text}")
            flag = True

    if not flag:
        print(f"\t Аномалий не найдено")
    else:
        flag = False
