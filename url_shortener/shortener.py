import hashlib

class URL_Shortener:
	"""
	The URL_Shortener is used to encode long urls
	to shortened ones in the form of baseurl/{code}
	and stores a mapping for later decoding.

	"""
	def __init__(self, base_url: str):
		self.base_url = base_url
		self.urls = {}

	def encode_url(self, original_url: str) -> str:
		""" 
		Encodeds url to short url 
		
		"""
		md5hash = hashlib.md5(original_url.encode()).hexdigest()
		base62_code = base62_encode(int(md5hash, 16))[:7]
		self.urls[base62_code] = original_url
		encoded_url = f"{self.base_url}/{base62_code}"
		return encoded_url

	def decode_url(self, encoded_url: str) -> str:
		"""
		Decodeds short url back to original

		"""
		base62_code = encoded_url.split("/")[-1]
		try:
			decoded_url = self.urls[base62_code]
		except KeyError as exc:
			raise ValueError("Cant decode provided URL: no entry present!") from exc

		return decoded_url

def base62_encode(num: int) -> str:
	"""
	Encodes integer to base62 format
	"""
	characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	encoded = ""
	base = 62
	while num:
		num, res = divmod(num, base)
		encoded = characters[res] + encoded
	return encoded
