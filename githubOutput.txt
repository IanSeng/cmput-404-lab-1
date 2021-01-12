import pkg_resources
import requests

print(pkg_resources.get_distribution("requests").version)

r = requests.get('https://google.com')
print(r.text)