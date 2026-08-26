from playwright.sync_api import expect, Page
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

VALID_ORDER_DATA = {
    "name": "Иван",
    "surname": "Петров",
    "address": "ул. Ленина, 1",
    "metro_station": "Сокольники",
    "phone": "+79991234567",
    "date": "01.01.2026",
    "rental_period": "сутки",
    "color": "чёрный жемчуг"
}


class OrderPage:
    def __init__(self, page: Page):
        self.page = page
        
        # TODO: напишите локаторы для всех элементов на странице
        # Используйте приоритет: role → text → CSS → XPath
        
        # Первый шаг (Для кого самокат)
        # self.name_input = 
        # self.surname_input = 
        # self.address_input = 
        # self.metro_input = 
        # self.phone_input = 
        # self.next_button = 
        
        # Второй шаг (Про аренду)
        # self.date_input = 
        # self.rental_dropdown = 
        # self.color_checkbox_black = 
        # self.color_checkbox_grey = 
        # self.comment_input = 
        # self.order_button = 
        
        # Модальное окно
        # self.yes_button = 
        # self.success_header = 

    def fill_first_step(self, name, surname, address, metro_station, phone):
        """Заполняет поля первого шага"""
        # TODO: реализуйте заполнение всех полей первого шага
        # Обратите внимание: поле метро требует выбора из выпадающего списка
        pass

    def fill_second_step(self, date, rental_period, color="чёрный жемчуг", comment=""):
        """Заполняет поля второго шага и подтверждает заказ"""
        # TODO: реализуйте заполнение всех полей второго шага
        # 1. Ввести дату и закрыть календарь (Enter)
        # 2. Выбрать срок аренды из дропдауна
        # 3. Выбрать цвет самоката
        # 4. Нажать "Заказать"
        # 5. Подтвердить в модальном окне
        pass


def test_successful_order(page: Page):
    """
    TODO: Позитивный сценарий — успешное оформление заказа
    
    1. Открыть страницу заказа
    2. Заполнить все поля корректно
    3. Отправить заказ
    4. Проверить сообщение об успехе
    """
    pass


def test_empty_required_field_name(page: Page):
    """
    TODO: Негативный сценарий — пустое обязательное поле (Имя)
    
    1. Открыть страницу заказа
    2. Заполнить все поля, кроме имени
    3. Нажать "Далее"
    4. Проверить ошибку "Введите корректное имя"
    """
    pass


def test_invalid_phone_format(page: Page):
    """
    TODO: Негативный сценарий — неверный формат телефона
    
    1. Открыть страницу заказа
    2. Заполнить все поля, но ввести телефон в неверном формате
    3. Нажать "Далее"
    4. Проверить ошибку "Введите корректный номер"
    """
    pass