# requires
# pip install requests

# communication

"""
Serialization:
to store and exchange data, we want to agree on a format that is easy
to write in and to read back.

On the web 2 formats are very popular:
- HTML (a subset of XML)
data is represented as a tree of opening and closing tags
enclosing the children of each element
"""
sample_html = """
<html>
    <head>
        <title>Hello title</title>
    </head>
    <body>
        <h1>I'm a header!</h1>
        <p class="fancy">I'm a paragraph</p>
    </body>
</html>
"""
# XML can be parsed using the standard library
# https://docs.python.org/3/library/xml.etree.elementtree.html
# or more conveniently using beautifulsoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# standard library example
import xml.etree.ElementTree as ET

# root = ET.parse(fname).getroot()
html = ET.fromstring(sample_html)
body = html[1]
for child in body:
    print(child)
    print("tag:", child.tag)  # h1 ; p
    print("attr:", child.attrib)  # {} ; {"class": "fancy"}

"""
- JSON (JavaScript Object Notation)
This format looks a lot like Python dictionaries, lists and literals.
Strings have to be double quoted, and no trailing comma is allowed.
With dictionaries, we have additional semantics due to the distinct keys.
The same data could be represented in JSON like this:
(for teaching purposes, not standard)
"""
sample_json = """
{
    "head": [{"type": "title", "text": "Hello title"}],
    "body": [
        {"type": "h1", "text": "I'm a title!"},
        {"type": "p", "class": "fancy", "text": "I'm a paragraph"}
    ]
}
"""
import json

# json.load(open(fname))
sample_dict = json.loads(sample_json)
print(sample_dict)

"""
other common formats include
- CSV / TSV for tabular data (spreadsheets)
- protobuf, used with gRPC, stricter communication channels between servers
- image formats (PNG, JPEG)

often this data is compressed using gzip or brotli
"""

"""
Client-Server interaction

On the web, machine use an IP address to send and receive data packets
Your web browser will first talk to a DNS to convert a domain name (wikipedia.org)
to an IP address (208.80.154.224)  # https://who.is/dns/wikipedia.org

The client then sends a request to this address,
the server processes it and generates a response 
(the webpage, or JavaScript in case of SPA (React & others))

    client      ||      server

send request              |
      |        --->       |
      |             receive request
    still            ... work ...
   waiting          generate response
      |               send response
      |        <---       |
receive response          |
decode & process          |
"""
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if resp.ok:
    print("---")
    print(resp.json())  # a dict
else:
    print("oh no!")

"""
More info:

The interface the server provides (how to request it & what answer to expect)
is called an API. API are commonly

- RESTful: oriented around resources and collections
        these APIs use semantics of HTTP methods (GET, PUT, POST, DELETE)
    GET /todos    -> list todos
    GET /todos/1  -> get todo w/ id=1
    PUT /todos/1 {"text": "hey"} -> update todo 1, set text to "hey"
    DELETE /todos/1 -> delete resource

- RPC (remote procedure call): arbitrary logic executed by the server
    POST nasa.gov/api/start_colonization {"planet": "Mars"}
"""
