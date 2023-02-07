# Shortlink
Shortlink is a simple URL shortening service written in Python.
It provides the functionality to encode a long URL into a short URL such as https://short.link/E8nq13l and back.

## Installing

Clone repository and install using pip:
```bash
$ git clone https://github.com/ploehnnico/url_shortener.git
$ cd url_shortener
$ pip3 install -e .
```
## Usage
To bring up the api server:
```bash
$ flask --app url_shortener run
```

The two api endpoints are available on localhost:5000 at /encode and /decode.

## Encode a URL
The encoding endoint is used to encode a given url to a shortened URL:

```http
POST /encode HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: xy
{
  "url": "url to shorten"
}
```

Example using curl:
```bash
curl -X POST -i -H "Content-Type: application/json" -d '{"url": "https://very.very/long/url"}' http://localhost:5000/encode
```

### Response
```
  HTTP/1.1 201 CREATED
  Server: Werkzeug/2.2.2 Python/3.11.0
  Date: Tue, 07 Feb 2023 14:31:36 GMT
  Content-Type: application/json
  Content-Length: 35
  Connection: close
  {"url":"https://short.en/7UzG1CM"}
```  
## Decode a URL
The decode endoint is used to convert a short URL back to its original URL:

```http
POST /decode /HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: xy
{
  "url": "short url to decode"
}
```

Using curl:
```bash
curl -X POST -i -H "Content-Type: application/json" -d '{"url": "https://short.en/7UzG1CM"}' http://localhost:5000/decode
```
### Response
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.0
Date: Tue, 07 Feb 2023 14:44:15 GMT
Content-Type: application/json
Content-Length: 37
Connection: close
{"url":"https://very.very/long/url"}
```

## Testing the application
The project contains unit tests for the shortening functionality and api tests for both apis.
To run the tests:
```bash
cd this-repository
pytest
```
