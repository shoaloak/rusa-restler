""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_api_v1_private_employees_post_id = dependencies.DynamicVariable("_api_v1_private_employees_post_id")

_api_v1_articles_post_id = dependencies.DynamicVariable("_api_v1_articles_post_id")

def parse_apiv1privateemployeespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_api_v1_private_employees_post_id", temp_7262)


def parse_apiv1articlespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8173 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_api_v1_articles_post_id", temp_8173)

req_collection = requests.RequestCollection([])
# Endpoint: /api/v1/private/employees/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("private"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_private_employees_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/private/employees/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/private/employees/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("private"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_private_employees_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/private/employees/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/private/employees/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("private"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_private_employees_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/private/employees/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/articles/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("articles"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_articles_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/articles/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/articles/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("articles"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_articles_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/articles/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/articles/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("articles"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_api_v1_articles_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/articles/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/private/employees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("private"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/private/employees"
)
req_collection.add_request(request)

# Endpoint: /api/v1/private/employees, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("private"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_apiv1privateemployeespost,
            'dependencies':
            [
                _api_v1_private_employees_post_id.writer()
            ]
        }

    },

],
requestId="/api/v1/private/employees"
)
req_collection.add_request(request)

# Endpoint: /api/v1/articles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("articles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/articles"
)
req_collection.add_request(request)

# Endpoint: /api/v1/articles, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("articles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_apiv1articlespost,
            'dependencies':
            [
                _api_v1_articles_post_id.writer()
            ]
        }

    },

],
requestId="/api/v1/articles"
)
req_collection.add_request(request)
