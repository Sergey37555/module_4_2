def test_function():        
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()   # здесь ничего не возвращает

inner_function()       # здесь появляется ошибка

test_function()        # здесь срабатывает ("Я в области видимости функции test_function")