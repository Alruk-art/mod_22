import pytest


def python_string_slicer(str):
   if len(str) < 50 or "python" in str:
       return str
   else:
       return str[0:50]

def generate_id(val):
   return "params: {0}".format(str(val))

@pytest.fixture(scope="function", params=[
   ("Короткая строка", "Короткая строка"),
   ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
    , "Длинная строка, не то чтобы прям очень длинная, но"),
   ("Короткая строка со словом python", "Короткая строка со словом python"),
   ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
    , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python")
],  ids=generate_id)

def param_fun_generated(request):
   return request.param

def test_python_string_slicer_generated(param_fun_generated):
   (input, expected_output) = param_fun_generated
   result = python_string_slicer(input)
   print ("\n Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
   assert result == expected_output

@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 11])
def test_multiply_params(x, y):
   print("x: {0}, y: {1}".format(x, y))
   assert True


@pytest.mark.parametrize ("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
@pytest.mark.parametrize ("y", [100, 1000], ids=["3 digit", "4 digit"])
def test_multiply_params(x, y):
    print ("x: {0}, y: {1}".format (x, y))
    assert True

def ids_x(val):
   return "x=({0})".format(str(val))
def ids_y(val):
   return "y=({0})".format(str(val))

@pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
@pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
def test_multiply_params(x, y):
   print("x: {0}, y: {1}".format(x, y))
   assert True


""" Задача про треугольники"""

def triangle(a,b):
    if a+b>5:
        result = True
    else:
        result = False
    return result

def ids_a(val):
   return "a=({0})".format(str(val))
def ids_b(val):
   return "b=({0})".format(str(val))

@pytest.mark.parametrize("a", [-1 , 0, 1], ids=ids_a)
@pytest.mark.parametrize("b", [4, 5, 6], ids=ids_b)

def test_sum_params(a, b):
    result = triangle(a,b)
    print("\n a: {0}, b: {1} a+b=".format(a, b), a+b, result)
    assert  True

def check(s,n):
    if n<=0 :
        result = False

    else:
        result = len(s) / n
    return result

@pytest.mark.parametrize('s',['', 'ddmnsdn'])
@pytest.mark.parametrize('n', [0, 3])

def test_check_s(s,n):
    result = check(s,n)
    print ('\n result=', result)

