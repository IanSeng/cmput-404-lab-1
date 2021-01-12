import pkg_resources
import requests

# google URL 
googleURL = 'https://google.com'
# github URL 
githubURL = 'https://raw.githubusercontent.com/IanSeng/cmput-404-lab-1/main/script.py'
# github output file name 
githubFileName = 'githubOutput.txt'

# Print package requests
print(pkg_resources.get_distribution("requests").version)

# Get and print Google home page
googleResp= requests.get(googleURL)
print(googleResp)

# Get and print script text
githubResp = requests.get(githubURL)
print(githubResp.text)