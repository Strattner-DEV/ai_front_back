import requests
from requests.structures import CaseInsensitiveDict

id_number = 745646
content = "The world is yours"
priority = 1

url = f"http://127.0.0.1:8000/add_task?id_number={id_number}&content={content}&priority={priority}"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjcsInVzZXJuYW1lIjoidGVzdDMiLCJwYXNzd29yZCI6IiQyYiQxMiRJemxBQUtlSjdSTDk4M0pJaVNzL1YubGJOTW02MVFDbXJjdzRpMzZFOFlvUnY3QmdDQmlMNiIsImJvYXJkIjp7InRhc2tzIjp7InRhc2stMSI6eyJpZCI6InRhc2stMSIsImNvbnRlbnQiOiJ1eWlvdXkiLCJwcmlvcml0eSI6MH19LCJjb2x1bW5zIjp7ImNvbHVtbi00MzA5MzYiOnsiaWQiOiJjb2x1bW4tNDMwOTM2IiwidGl0bGUiOiJ0ZXN0IiwidGFza0lkcyI6WyJ0YXNrLTEiXX19LCJjb2x1bW5PcmRlciI6WyJjb2x1bW4tNDMwOTM2Il19fQ.3p33UL2AEc3k-k1ilwGyqQm2-Bch27WP1J3r6CzF0zA"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

print(url)

resp = requests.post(url, headers=headers)
print(resp)