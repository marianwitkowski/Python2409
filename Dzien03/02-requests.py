
# Pobieranie danych z internetu
import requests
from requests.auth import HTTPBasicAuth

# GET
response = requests.get("https://api.github.com/",
                        verify=False, # weryfikacja certu SSL
                        allow_redirects=True, # automatycznie przekierowania
                        timeout=(10, 45) #10sek na połączenie, 45sek na odbiór danych
                        )
print(response.text)

# https://api.github.com/search/repositories?q=request+language:python&
response = requests.get("https://api.github.com/search/repositories",
                        params={
                            "q" : "request+language:python"
                        },
                        verify=False, # weryfikacja certu SSL
                        allow_redirects=True, # automatycznie przekierowania
                        timeout=(10, 45) #10sek na połączenie, 45sek na odbiór danych
                        )
print(response.status_code)

# POST
response = requests.post("http://httpbin.org/post", data={
    "key1" : "value1", "key2" : "value2"
}, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "App-ID" : "Python Course 2409"
}, proxies={
   # "http" : "http://192.168.0.1:3128",
   # "https" : "http://192.168.0.1:3128",
})
print(response.text)

# https://api.ambra.com.pl/j3GsmoZgcL/260/CQ02.png
url = "https://api.ambra.com.pl/j3GsmoZgcL/260/CQ02.png"
response = requests.get(url,
                        auth=HTTPBasicAuth("","") )

file_name = url.split("/")[-1]
with open(file_name, "wb") as fd:
    fd.write(response.content)

# UPLOAD plików
with open("CQ02.png", "rb") as fd:
    upload_files = {
        "CQO2.png" : fd
    }
    response = requests.post("http://httpbin.org/post", files=upload_files)
    print(response.text)