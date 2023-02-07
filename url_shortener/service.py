from flask import Blueprint, request
from . import shortener, config

url_shortener = shortener.URL_Shortener(config.SERVER_NAME)

bp = Blueprint('service', __name__)

@bp.route('/encode', methods=['POST'])
def encode():
	"""
	Encoding endpoint returning hort URL to given URL
	"""
	try:
		url = request.get_json()['url']
	except KeyError:
		return 'Invalid data', 400

	encoded_url = url_shortener.encode_url(url)

	return {'url': encoded_url}, 201

@bp.route('/decode', methods=['POST'])
def decode():
	"""
	Decoding endpoint rreturning original URL given short URL
	"""
	try:
		encoded_url = request.get_json()['url']
	except KeyError:
		return 'Invalid data', 400

	try:
		decoded_url = url_shortener.decode_url(encoded_url)
	except ValueError:
		return 'Url not found', 400

	return {'url': decoded_url}
