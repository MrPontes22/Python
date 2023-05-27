import requests
API_KEY = "1590e6cde31694e4b0ea6c7bb8a079fe"
cidade = "rio de janeiro"
LINK = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(LINK)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ºC")