import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
count_redirects = len(response.history)

print(f"Количество редиректов: {count_redirects}")
print(f"Итоговый URL : {response.url}")