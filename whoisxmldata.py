try:
   from urllib.request import urlopen, Request
except ImportError:
   from urllib2 import urlopen, Request

from json import dumps
import json
from datetime import datetime

terms = ["arriver"]
key = "at_vJzTpzSlCboaKedpbLCjM5nJUPeo3"
mode = "purchase"
data = {"includeSearchTerms": terms, "apiKey": key, "mode": mode, "sinceDate": "2022-11-18"}
url = "https://brand-alert.whoisxmlapi.com/api/v2"

req = Request(url)
#print(urlopen(req,data).read())
test  = str(datetime.now())
print(test)
time = {"_time": test}
response = json.loads(urlopen(req, dumps(data).encode("utf-8")).read().decode("utf8"))
#response.append(time)
print({**time,**response})
#print(response)
