import requests
url="https://www.sabah.com.tr/"
response=requests.get(url)
print(response)
#200 işlem başarılı
#400 sayfa bulumadı
#500 server hatası 
print(response.status_code)
#gönderilen isteğe karşılık gelen kod
print(response.text)
