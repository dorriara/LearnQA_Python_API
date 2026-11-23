import requests
import time
url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
parsed_response = response.json()
token = parsed_response["token"]
wait_seconds = parsed_response["seconds"]

print("Check the job status:")
response_with_token = requests.get(url, params={"token": token})
parsed_response_with_token = response_with_token.json()

if "error" in parsed_response_with_token:
    print(f'\t{parsed_response_with_token["error"]}')
    exit()

if parsed_response_with_token["status"] == "Job is NOT ready":
    print(f'\t{parsed_response_with_token["status"]}')
    print(f"Wait {wait_seconds} seconds and check again:")
    time.sleep(wait_seconds)
    response_with_token = requests.get(url, params={"token": token})
    parsed_response_with_token = response_with_token.json()

if (parsed_response_with_token["status"] == "Job is ready") and ("result" in parsed_response_with_token):
    print(f'\t{parsed_response_with_token["status"]}')
    print(f'\tresult = {parsed_response_with_token["result"]}')
else:
    print("\tSomething wrong")
