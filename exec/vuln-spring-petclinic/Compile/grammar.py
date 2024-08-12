""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_owners_post_id = dependencies.DynamicVariable("_owners_post_id")

_owners__ownerId__pets_post_type_id = dependencies.DynamicVariable("_owners__ownerId__pets_post_type_id")

_pettypes_post_id = dependencies.DynamicVariable("_pettypes_post_id")

_pets_post_type_id = dependencies.DynamicVariable("_pets_post_type_id")

_visits_post_id = dependencies.DynamicVariable("_visits_post_id")

_specialties_post_id = dependencies.DynamicVariable("_specialties_post_id")

_vets_post_specialties_0_id = dependencies.DynamicVariable("_vets_post_specialties_0_id")

def parse_ownerspost(data, **kwargs):
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
        dependencies.set_variable("_owners_post_id", temp_7262)


def parse_ownersownerIdpetspost(data, **kwargs):
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
            temp_8173 = str(data["type"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_owners__ownerId__pets_post_type_id", temp_8173)


def parse_pettypespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

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
            temp_7680 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_pettypes_post_id", temp_7680)


def parse_petspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5581 = None

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
            temp_5581 = str(data["type"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_pets_post_type_id", temp_5581)


def parse_visitspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

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
            temp_2060 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_visits_post_id", temp_2060)


def parse_specialtiespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

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
            temp_5588 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_specialties_post_id", temp_5588)


def parse_vetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

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
            temp_9060 = str(data["specialties"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_vets_post_specialties_0_id", temp_9060)

req_collection = requests.RequestCollection([])
# Endpoint: /oops, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oops"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/oops"
)
req_collection.add_request(request)

# Endpoint: /owners, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["George"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Franklin"]),
    primitives.restler_static_string(""",
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["110 W. Liberty St."]),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Madison"]),
    primitives.restler_static_string(""",
    "telephone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["6085551023"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_ownerspost,
            'dependencies':
            [
                _owners_post_id.writer()
            ]
        }

    },

],
requestId="/owners"
)
req_collection.add_request(request)

# Endpoint: /owners, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("lastName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Davis"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["George"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Franklin"]),
    primitives.restler_static_string(""",
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["110 W. Liberty St."]),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Madison"]),
    primitives.restler_static_string(""",
    "telephone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["6085551023"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}/pets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Leo"]),
    primitives.restler_static_string(""",
    "birthDate":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2010-09-07"]),
    primitives.restler_static_string(""",
    "type":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_ownersownerIdpetspost,
            'dependencies':
            [
                _owners__ownerId__pets_post_type_id.writer()
            ]
        }

    },

],
requestId="/owners/{ownerId}/pets"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}/pets/{petId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners__ownerId__pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}/pets/{petId}"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}/pets/{petId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners__ownerId__pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Leo"]),
    primitives.restler_static_string(""",
    "birthDate":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2010-09-07"]),
    primitives.restler_static_string(""",
    "type":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}/pets/{petId}"
)
req_collection.add_request(request)

# Endpoint: /owners/{ownerId}/pets/{petId}/visits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_owners__ownerId__pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2013-01-01"]),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["rabies shot"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/owners/{ownerId}/pets/{petId}/visits"
)
req_collection.add_request(request)

# Endpoint: /pettypes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pettypes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pettypes"
)
req_collection.add_request(request)

# Endpoint: /pettypes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pettypes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_pettypespost,
            'dependencies':
            [
                _pettypes_post_id.writer()
            ]
        }

    },

],
requestId="/pettypes"
)
req_collection.add_request(request)

# Endpoint: /pettypes/{petTypeId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pettypes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pettypes_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pettypes/{petTypeId}"
)
req_collection.add_request(request)

# Endpoint: /pettypes/{petTypeId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pettypes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pettypes_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pettypes/{petTypeId}"
)
req_collection.add_request(request)

# Endpoint: /pettypes/{petTypeId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pettypes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pettypes_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pettypes/{petTypeId}"
)
req_collection.add_request(request)

# Endpoint: /pets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pets"
)
req_collection.add_request(request)

# Endpoint: /pets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Leo"]),
    primitives.restler_static_string(""",
    "birthDate":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2010-09-07"]),
    primitives.restler_static_string(""",
    "type":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_petspost,
            'dependencies':
            [
                _pets_post_type_id.writer()
            ]
        }

    },

],
requestId="/pets"
)
req_collection.add_request(request)

# Endpoint: /pets/{petId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pets/{petId}"
)
req_collection.add_request(request)

# Endpoint: /pets/{petId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Leo"]),
    primitives.restler_static_string(""",
    "birthDate":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2010-09-07"]),
    primitives.restler_static_string(""",
    "type":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["cat"]),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/pets/{petId}"
)
req_collection.add_request(request)

# Endpoint: /pets/{petId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pets_post_type_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pets/{petId}"
)
req_collection.add_request(request)

# Endpoint: /visits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/visits"
)
req_collection.add_request(request)

# Endpoint: /visits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2013-01-01"]),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["rabies shot"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_visitspost,
            'dependencies':
            [
                _visits_post_id.writer()
            ]
        }

    },

],
requestId="/visits"
)
req_collection.add_request(request)

# Endpoint: /visits/{visitId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_visits_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/visits/{visitId}"
)
req_collection.add_request(request)

# Endpoint: /visits/{visitId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_visits_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "date":"""),
    primitives.restler_fuzzable_date("2019-06-26", quoted=True, examples=["2013-01-01"]),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["rabies shot"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/visits/{visitId}"
)
req_collection.add_request(request)

# Endpoint: /visits/{visitId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visits"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_visits_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/visits/{visitId}"
)
req_collection.add_request(request)

# Endpoint: /specialties, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("specialties"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/specialties"
)
req_collection.add_request(request)

# Endpoint: /specialties, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("specialties"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["radiology"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_specialtiespost,
            'dependencies':
            [
                _specialties_post_id.writer()
            ]
        }

    },

],
requestId="/specialties"
)
req_collection.add_request(request)

# Endpoint: /specialties/{specialtyId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("specialties"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_specialties_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/specialties/{specialtyId}"
)
req_collection.add_request(request)

# Endpoint: /specialties/{specialtyId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("specialties"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_specialties_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["radiology"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/specialties/{specialtyId}"
)
req_collection.add_request(request)

# Endpoint: /specialties/{specialtyId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("specialties"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_specialties_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/specialties/{specialtyId}"
)
req_collection.add_request(request)

# Endpoint: /vets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/vets"
)
req_collection.add_request(request)

# Endpoint: /vets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["James"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Carter"]),
    primitives.restler_static_string(""",
    "specialties":
    [
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["radiology"]),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_vetspost,
            'dependencies':
            [
                _vets_post_specialties_0_id.writer()
            ]
        }

    },

],
requestId="/vets"
)
req_collection.add_request(request)

# Endpoint: /vets/{vetId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_vets_post_specialties_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/vets/{vetId}"
)
req_collection.add_request(request)

# Endpoint: /vets/{vetId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_vets_post_specialties_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["James"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Carter"]),
    primitives.restler_static_string(""",
    "specialties":
    [
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["radiology"]),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/vets/{vetId}"
)
req_collection.add_request(request)

# Endpoint: /vets/{vetId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_vets_post_specialties_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/vets/{vetId}"
)
req_collection.add_request(request)

# Endpoint: /users, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/petclinic/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:9966\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john.doe"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["1234abc"]),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(""",
    "roles":
    [
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["admin"]),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/users"
)
req_collection.add_request(request)
