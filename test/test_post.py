import requests
from requests.structures import CaseInsensitiveDict

id_number = 555
content = "The world is yours"
priority = 1

url = f"http://localhost:8000/add_task?id_number={id_number}&content={content}&priority={priority}"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NDAsInVzZXJuYW1lIjoidGVzdGRpZWdvIiwicGFzc3dvcmQiOiIkMmIkMTIkYm1NUzk1TS5UUGhQQThCTXMxR2FCdXRLZlQzY0MxWUtFc3hKUlZwR3ZMdXg4d1NKVG1ESk8iLCJib2FyZCI6eyJ0YXNrcyI6e30sImNvbHVtbnMiOnsiY29sdW1uLTEiOnsiaWQiOiJjb2x1bW4tMSIsInRpdGxlIjoiVG8gZG8iLCJ0YXNrSWRzIjpbXX0sImNvbHVtbi0yIjp7ImlkIjoiY29sdW1uLTIiLCJ0aXRsZSI6IkRvbmUiLCJ0YXNrSWRzIjpbXX0sImNvbHVtbi0zIjp7ImlkIjoiY29sdW1uLTMiLCJ0aXRsZSI6IkluIHByb2dyZXNzIiwidGFza0lkcyI6W119fSwiY29sdW1uT3JkZXIiOlsiY29sdW1uLTEiLCJjb2x1bW4tMiIsImNvbHVtbi0zIl19fQ.T4Nr8NnS5m6gHsp2QTGyIaDhv1QzG4YhkjInDaVqX5E"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

print(url)

resp = requests.post(url, headers=headers)
print(resp)