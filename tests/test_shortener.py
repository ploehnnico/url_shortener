import pytest
from url_shortener.shortener import URL_Shortener

def make_shortener_and_urls():
	original_url = "https://very.very/long/url/to/shorten"
	base_url = "https://short.en"
	url_shortener = URL_Shortener(base_url)
	return url_shortener, original_url, base_url

def test_url_is_encode_to_base_url_and_7_digit_code():
	url_shortener, original_url, base_url = make_shortener_and_urls()
	encoded_url = url_shortener.encode_url(original_url)
	code = encoded_url.split("/")[-1]
	assert base_url in encoded_url
	assert len(code) == 7

def test_encoded_url_can_be_decoded_to_original_url():
	url_shortener, original_url, _ = make_shortener_and_urls()
	encoded_url = url_shortener.encode_url(original_url)
	decoded_url = url_shortener.decode_url(encoded_url)
	assert decoded_url == original_url

def test_unknown_url_and_unknwon_code_cant_be_decoded():
	url_shortener, _, base_url = make_shortener_and_urls()
	unknown_url = "https://un.known/url"
	url_with_unknown_code = f"{base_url}/1234567"
	with pytest.raises(Exception) as e_info:
		decoded_url = url_shortener.decode_url(unknown_url)
	with pytest.raises(Exception) as e_info:
		decoded_url = url_shortener.decode_url(url_with_unknown_code)

def test_same_long_url_is_always_encoded_to_same_url():
	url_shortener, original_url, _ = make_shortener_and_urls()
	encoded_url_1 = url_shortener.encode_url(original_url)
	encoded_url_2 = url_shortener.encode_url(original_url)
	assert encoded_url_1 == encoded_url_2

