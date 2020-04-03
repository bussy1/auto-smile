import requests
import time

TOKEN = '' 


def check_token(token): # проверяем токен
	try:
		response = requests.post('https://api.vk.com/method/users.setCovidStatus?' \
		'api_id=7362610'\
		'&method=users.setCovidStatus&format=json&' \
		'v=5.103' \
		'&status_id=1' + \
		'&access_token=' + str(token) + \
		'&request_id=5')

		print('Проверка токена..')
		data = response.json()
		if data['response']: # проверяем появится ли ошибка
			pass

		return True

	except:
		return False	


def requests_smile(token):
	try:
		if check_token(token) == True:
			print('Токен верный..')

			print('Скрипт запущен')
			while True:
				for item in range(1, 7):
					response = requests.post('https://api.vk.com/method/users.setCovidStatus?' \
						'api_id=7362610'\
						'&method=users.setCovidStatus&format=json&' \
						'v=5.103' \
						'&status_id=' + str(item) + \
						'&access_token=' + str(TOKEN) + \
						'&request_id=5')
				time.sleep(0.1)
		else:
			print('Токен введен неверно')

	except Exception as error:
		print(f'[ОШИБКА] {error}')



if __name__ == '__main__':
	requests_smile(TOKEN)
