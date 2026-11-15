#lesson-1 Ex.3
print("Hello from Sofya")

#lesson-1 Ex.4
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)