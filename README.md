# Shortlink
Shortlink is a simple URL shortening service written in Python.
It provides the functionality to encode a long URL into a short URL such as https://short.link/E8nq13l and back.

# Installing

Clone repository and install using pip:
```bash
$ git clone https://www.github.com/this-repository-url
$ cd this-repository
$ pip3 install -e .
```
# Usage
To bring up the api server:
```bash
$ flask --app url_shortener run

```

The two api endpoints are available on localhost:5000 at /encode and /decode.

# Encode a URL
The encoding endoint is used to encode a given url to a shortened URL:

```http
POST /encode
```

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
  {"url":"https://short.en/7UzG1CM"}```
