import http.client

conn = http.client.HTTPSConnection("quote-api4.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "725fb326c3mshba753d38a59d3f5p137210jsn4a78d70c995f",
    'x-rapidapi-host': "quote-api4.p.rapidapi.com"
}

conn.request("GET", "/quote?topic=inspirational", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
