# Тестирование функционала сервиса *Stellar Burgers*

## Описание проекта

Cервиса _Stellar Burgers_ - это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

Адрес сервиса: https://stellarburgers.nomoreparties.site

Описание реализованных для проверки сервиса тестов:

В файле test_registration.py содержатся скрипты для проверки регистрации:

| № | Название теста                         | Описание теста                                                                       |
|--:|:---------------------------------------|:-------------------------------------------------------------------------------------|
| 1 | **test_user_registration**             | Тест проверяет, что регистрация пользователя при корректных данных произошла успешно |
| 2 | **test_password_exception_length_1_5** | Тест проверяет, что при вводе пароля меньше 6 символов при регистрации выйдет ошибка |
| 3 | **test_password_exception_length_0**   | Тест проверяет, что с пустым паролем зарегистрироваться невозможно                   |

В файле test_enter.py содержатся скрипты для проверки входа в систему

| № | Название теста                                 | Описание теста                                                      |
|--:|:-----------------------------------------------|:--------------------------------------------------------------------|
| 1 | **test_user_login_enter_account**              | Тест проверяет вход по кнопке «Войти в аккаунт» на главной странице |
| 2 | **test_user_login_enter_personal_account**     | Тест проверяет вход через кнопку «Личный кабинет»                   |
| 3 | **test_user_login_enter_form_registration**    | Тест проверяет вход через кнопку на форме регистрации               |
| 4 | **test_user_login_enter_form_forgot_password** | Тест проверяет вход через кнопку в форме восстановления пароля      |


В файле test_personal_account.py содержатся скрипты для перехода в личный кабинет и переход из личного кабинета

| № | Название теста                                  | Описание теста                                                       |
|--:|:------------------------------------------------|:---------------------------------------------------------------------|
| 1 | **test_user_click_personal_account**            | Тест проверяет переход по клику на «Личный кабинет»                  |
| 2 | **test_user_click_builder_in_personal_account** | Тест проверяет переход по клику на «Конструктор» из личного кабинета |
| 3 | **test_user_logo_click**                        | Тест проверяет на логотип Stellar Burgers из личного кабинета        |


В файле test_logout.py содержится скрипт проверки выхода по кнопке "Выход"

| № | Название теста                       | Описание теста                                            |
|--:|:-------------------------------------|:----------------------------------------------------------|
| 1 | **test_user_enter_personal_account** | Тест проверяет выхода по кнопке "Выход" в личном кабинете |**

В файле test_change_ingridients.py содержатся скрипты проверки работы к разделам «Булки», «Соусы», «Начинки».

| № | Название теста              | Описание теста                             |
|--:|:----------------------------|:-------------------------------------------|
| 1 | **test_user_click_bulka**   | Тест проверяет переход к разделу "Булки"   |
| 2 | **test_user_click_souse**   | Тест проверяет переход к разделу "Соусы"   |
| 3 | **test_user_click_filling** | Тест проверяет переход к разделу "Начинки" |

В файле conftest.py созданы фикстуры для подключения к сервису и генерации логина, пароля и e-mail

В файле data.py содержатся данные для проведения теста.
