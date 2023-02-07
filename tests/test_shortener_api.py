import pytest

def test_encode_endpoint_encodes_url_and_returns_201(client):
	response = client.post(
		'/encode', json={'url': 'https://very.long/url/to/shorten'}
	)
	assert response.status_code == 201
	assert response.headers['content-type'] == 'application/json' 
	encoded_url = response.json["url"]
	assert len(encoded_url.split("/")[-1]) == 7
	assert "https://short.en" in encoded_url

def test_encode_enpoint_returns_400_if_data_not_okay(client):
	response = client.post(
		'/encode', json={}
	)
	assert response.status_code == 400
	response = client.post(
		'/encode', json={"wrong": "data"}
	)
	assert response.status_code == 400

def test_decode_endpoint_decodes_url_and_returns_200(client):
	original_url = 'http://anoth.er/too/long/url/to/shorten'
	response = client.post(
		'/encode', json={'url': original_url}
	)
	encoded_url = response.json['url']
	response = client.post(
		'/decode', json={'url': encoded_url}
	)
	assert response.status_code == 200
	assert response.headers['content-type'] == 'application/json'
	assert response.json['url'] == original_url

def test_decode_endpoint_returns_400_if_data_not_okay(client):
	response = client.post(
		'/decode', json={}
	)
	assert response.status_code == 400
	response = client.post (
		'/decode', json={'wrong': 'data'}
	)
	assert response.status_code == 400

def test_decode_endpoint_returns_404_if_url_not_found(client):
	response = client.post(
		'/decode', json={'url': 'https://stran.ge/url'}
	)
	assert response.status_code == 400
	response = client.post(
		'/decode', json={'url': 'https://short.en/H23j21y'}
	)