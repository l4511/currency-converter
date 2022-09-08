import json
import requests
from config import keys


class APIExceptions(Exception):
	pass


class Convertor:
	@staticmethod
	def get_price(amount, base, quote):
		try:
			base_ticker = keys[base.lower()]
		except KeyError:
			raise APIExceptions(f'Валюта {base} не найдена!')
		try:
			quote_ticker = keys[quote.lower()]
		except KeyError:
			raise APIExceptions(f'Валюта {quote} не найдена!')
		if base == quote:
			raise APIExceptions(f'Невозможно перевести одинаковые валюты {quote}!')
		try:
			amount = float(amount)
		except ValueError:
			raise APIExceptions(f' Не удалось обработать количество {amount}!')

		r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
		total_base = json.loads(r.content)[keys[quote]]
		text = f'Цена {amount} {base}  в {quote}  : {amount * total_base}'

		return text
