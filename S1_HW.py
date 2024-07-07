import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
category = input('Введите категорию (cafe, fitness, etc.): ')
params = {
"client_id": client_id,
"client_secret": client_secret,
"near": city,
"query": category,
'fields': 'name,location,rating'
}

headers = {
"Accept": "application/json",
"Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text) # Парсим JSON-ответ в словарь Python
    venues = data["results"] # Получаем список мест из данных ответа
    if len(venues) != 0:
        for venue in venues:# Проходимся по каждому месту в списке
            print("\n")
            print("Категория: ", category)
            print("Название:", venue["name"])
            print("Адрес:", venue.get('location').get('address'))
            print("Рейтинг:", venue.get('rating'))
    else:
        print("Категория не найдена!")
        

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)


