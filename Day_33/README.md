Today we will learn about the **API's**

**Application Programming Interface**

An API is a set of Commands, functions, protocols, and objects that programmers can use to create softwares or interact with an external system.

***Restraunt menu*** is an analogy for API, where restraunt decide what we can order and what not.

**API Endpoint**: The location where data is stored (URL)

**API Request** : Asking our question

```python
import requests
# this library requests need to be used for fetchning data from http,
# mostly used to fetch data from API

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# <Response [200]>

Below are few sample Response Codes:
1XX : Hold On
2XX : Here you go
3XX : Go Away (Access Problem)
4XX : You Screwed up (Like a wrong link/url etc)
5XX : Server Screwed up

#More here :
https://www.webfx.com/web-development/glossary/http-status-codes/
```

**REST API** (Representational State Transfer) is an architectural style for building web services, which defines a set of constraints to be used when creating web services. REST APIs are used to communicate between a client and server to perform operations over HTTP.

**FastAPI**, on the other hand, is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It uses the ASGI (Asynchronous Server Gateway Interface) server which allows for great concurrency and performance. FastAPI provides several features out-of-the-box, such as automatic data validation, automatic generation of API documentation, and support for asynchronous programming.

In short, REST API is a set of constraints for creating web services, whereas FastAPI is a Python framework for building high-performance web APIs that adheres to the RESTful principles.

The requests module is a third-party library in Python that allows you to send HTTP/1.1 requests using Python code. It is used for making HTTP requests to a server and retrieving the response. You can use it to fetch data from an API, access web pages, download files, and more. The requests module provides a simple way to interact with websites and web services, and it handles many of the details for you, like encoding and decoding data and handling redirects.
