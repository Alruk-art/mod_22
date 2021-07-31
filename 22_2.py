import pytest
@pytest.fixture(autouse=True)
def ket_api_key():
   """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

   # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
   status, pytest.key = pf.get_api_key(valid_email, valid_password)

   # Сверяем полученные данные с нашими ожиданиями
   assert status == 200
   assert 'key' in pytest.key

   yield

   # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
   assert pytest.status == 200


@pytest.mark.parametrize("filter", ['', 'my_pets'], ids= ['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
   """ Проверяем, что запрос всех питомцев возвращает не пустой список.
   Для этого сначала получаем api-ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
   запрашиваем список всех питомцев и проверяем, что список не пустой.
   Доступное значение параметра filter - 'my_pets' либо '' """

   pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

   assert len(result['pets']) > 0

def generate_string(n):
   return "x" * n

@pytest.mark.parametrize("filter",
                        [''
                            , 'my_pets'
                            , generate_string(255)
                            , generate_string(1001)]
   , ids= ['empty string', 'only my pets', '255 symbols', 'more than 1000 symbols'])

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.mark.parametrize("filter",
                        [''
                            , 'my_pets'
                            , generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , 123
                         ]
   , ids=['empty string'
          , 'only my pets'
          , '255 symbols'
          , 'more than 1000 symbols'
          , 'russian'
          , 'RUSSIAN'
          , 'chinese'
          , 'specials'
          , 'digit'])
def test_get_all_pets_with_valid_key(filter):

def generate_string(num):
   return "x" * num


def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.fixture(autouse=True)
def ket_api_key():
   # """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

   # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
   status, pytest.key = pf.get_api_key(valid_email, valid_password)

   # Сверяем полученные данные с нашими ожиданиями
   assert status == 200
   assert 'key' in pytest.key

   yield


@pytest.mark.parametrize("filter",
                        [
                            generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , 123
                        ],
                        ids =
                        [
                            '255 symbols'
                            , 'more than 1000 symbols'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                            , 'specials'
                            , 'digit'
                        ])
def test_get_all_pets_with_negative_filter(filter):
   pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

   # Проверяем статус ответа
   assert pytest.status == 400


@pytest.mark.parametrize("filter",
                        ['', 'my_pets'],
                        ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
   pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

   # Проверяем статус ответа
   assert pytest.status == 200
   assert len(result['pets']) > 0
   
ef add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
   """
   Метод
   отправляет (постит)
   на
   сервер
   данные
   о
   добавляемом
   питомце
   и
   возвращает
   статус
   запроса
   и
   результат
   в
   формате
   JSON
   с
   данными
   добавленного
   питомца
   """

   data = MultipartEncoder(
       fields={
           'name': name,
           'animal_type': animal_type,
           'age': age
       })
   headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

   res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
   status = res.status_code
   result = ""
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   print(result)
   return status, result


Теперь возьмем наш тест test_add_new_pet_with_valid_data и создадим по аналогии другой тест. Назовем его test_add_new_pet_simple и параметризуем по принципу, описанному выше. Единственное, что бросается в глаза — это то, что мы пытаемся передать число в виде строки, но это не проблема, так как form-data тип данных не может принимать числовые данные в принципе, у нас просто не остаётся других вариантов:

@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
def test_add_new_pet_simple(name, animal_type='двортерьер',
                           age='4'):
   """
   Проверяем, что
   можно
   добавить
   питомца
   с
   различными
   данными
   """

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '':
       assert pytest.status == 400
   else:
	 assert pytest.status == 200
       assert result['name'] == name
       assert result['age'] == age
       assert result['animal_type'] == animal_type

@pytest.mark.parametrize("name"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
def test_add_new_pet_simple(name, animal_type,
                           age='4'):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Добавили проверку animal_type
   if name == '' or animal_type == '':
       assert pytest.status == 400
   else:
       assert pytest.status == 200
       assert result['name'] == name
       assert result['age'] == age
       assert result['animal_type'] == animal_type
