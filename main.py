import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Функция для отправки уведомлений в гугл таблицу
def send_notification_to_google_sheet(action, details):
    scope = ['https://docs.google.com/spreadsheets/d/1EkjiAV17mZI3pjcKEXp-KbPwxs6_TenQJhkBymMWvRY/edit?usp=sharing']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open('Actions Log').sheet1
    worksheet.append_row([action, details])

from api import patch_report_season
# Функция для взаимодействия с первым API файлом
def list_change():
    response = patch_report_season()
    if response.status_code == 200:
        send_notification_to_google_sheet('Изменен список отряда ', 'Success')
    else:
        send_notification_to_google_sheet('Ошибка редактирования', 'Error')

# Функция для взаимодействия со вторым API файлом
'''def api_action2():
    response = requests.get('http://api2.com')
    if response.status_code == 200:
        send_notification_to_google_sheet('API Action 2', 'Success')
    else:
        send_notification_to_google_sheet('API Action 2', 'Error')
'''
# Основной блок программы
if __name__ == '__main__':
    # Вызываем функции для взаимодействия с API
    list_change()
    #api_action2()