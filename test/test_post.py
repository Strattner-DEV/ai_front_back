import requests
from requests.structures import CaseInsensitiveDict

id_number = 555
content = "The world is yours"
priority = 1

url = f"http://localhost:8000/add_task?id_number={id_number}&content={content}&priority={priority}"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsInVzZXJuYW1lIjoidGVzdDciLCJwYXNzd29yZCI6IiQyYiQxMiQ3SkovVnBMSGFUVjJqN1FwbHJsRkouV2JFY2tlUFRycjZYLkVFV3k5QTVyMXNFazZpMFRxYSIsImJvYXJkIjp7InRhc2tzIjp7fSwiY29sdW1ucyI6eyJjb2x1bW4tMSI6eyJpZCI6ImNvbHVtbi0xIiwidGl0bGUiOiJUbyBkbyIsInRhc2tJZHMiOltdfSwiY29sdW1uLTIiOnsiaWQiOiJjb2x1bW4tMiIsInRpdGxlIjoiRG9uZSIsInRhc2tJZHMiOltdfSwiY29sdW1uLTMiOnsiaWQiOiJjb2x1bW4tMyIsInRpdGxlIjoiSW4gcHJvZ3Jlc3MiLCJ0YXNrSWRzIjpbXX19LCJjb2x1bW5PcmRlciI6WyJjb2x1bW4tMSIsImNvbHVtbi0yIiwiY29sdW1uLTMiXX19.9AY6cLIggbldwuiSLAZj_1RY8TiuCNCjZKZ1Lp_fwR8"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

print(url)

resp = requests.post(url, headers=headers)
print(resp)