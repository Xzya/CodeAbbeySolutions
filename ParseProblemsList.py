
import urllib

url = "http://www.codeabbey.com/index/task_list"

req = urllib.request.urlopen(url)
html = req.read()

