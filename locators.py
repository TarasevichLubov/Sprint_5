# Страница - https://stellarburgers.nomoreparties.site/
account = ".//a[@href='/account']"  # кнопка "Личный кабинет"
button_enter_account = ".//button[text()='Войти в аккаунт']"
button_order = ".//button[text()='Оформить заказ']"
page_brad = ".//span[text()='Булки']/parent::div"
page_souse = ".//span[text()='Соусы']/parent::div"
page_filling = ".//span[text()='Начинки']/parent::div"

# Страница - https://stellarburgers.nomoreparties.site/login
button_registration = ".//button[text()='Зарегистрироваться']"  # ссылка "Зарегистрироваться"
field_email = ".//label[text()='Email']/following-sibling::input"  # поле "Email"
field_password = ".//label[text()='Пароль']/following-sibling::input"  # поле "Пароль"
but_enter = ".//button[text()='Войти']"  # кнопка "Войти"

# Страница - https://stellarburgers.nomoreparties.site/register
field_reg_login = ".//label[text()='Имя']/following-sibling::input"  # поле "Логин"
field_reg_email = ".//label[text()='Email']/following-sibling::input"  # поле "Email"
field_reg_password = ".//label[text()='Пароль']/following-sibling::input"  # поле "Пароль"
error_message_password_less_6 = ".//label[text()='Пароль']/following::p[contains(@class, 'input__error')]"  # сообщение об ошибке
href_enter = ".//a[@href='/login']"

# Страница - https://stellarburgers.nomoreparties.site/account/profile
button_builder = ".//p[text()='Конструктор']/following::a[@href=\'/\']"  # кнопка "Конструктор"
button_exit = ".//button[text()='Выход']"  # кнопка "Выход"
logo = ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href=\'/\']"  # логотип "Stellar Burgers"

# Страница - https://stellarburgers.nomoreparties.site/forgot-password
login_href = ".//a[@href='/login']"  # ссылка зарегистрироваться
