from playwright.sync_api import expect


def test_successful_order(page):
    '''
    TODO:
    1. Открыть форму заказа
    2. Заполнить все поля корректно
    3. Отправить заказ
    4. Проверить сообщение об успехе
    '''
    pass


def test_empty_required_field(page):
    '''
    TODO:
    1. Открыть форму заказа
    2. Оставить обязательное поле пустым
    3. Отправить форму
    4. Проверить ошибку валидации
    '''
    pass


def test_invalid_phone_format(page):
    '''
    TODO:
    1. Открыть форму заказа
    2. Ввести телефон в неверном формате
    3. Отправить форму
    4. Проверить ошибку валидации
    '''
    pass
