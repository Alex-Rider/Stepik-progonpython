import requests
"""
r = requests.get("http://example.com")
print(r.text)
"""

"""url = "http://example.com"
par = {"key1": "value1", "key2": "value2", "key_n": "value_n"}
r = requests.get(url, params=par)
print(r.url)
print(r.headers)
print(type(r.headers))
"""

"""url = "http://httpbin.org/cookies"
cookies = {"cookies_are": "working"}
r = requests.get(url, cookies=cookies)
print(r.text)

print(r.cookies["example_cookie_name"])"""

"""url = "https://stepic.org/media/attachments/course67/3.6.2/121.txt"
r = requests.get(url)
n = r.text.count("\n")
print(r.text)
print(n)"""

# prefix = "https://stepic.org/media/attachments/course67/3.6.3/"
# url = input()
# while flag != "We":
#     print("!!!", prefix + url, "!!!")
#     r = requests.get(prefix + url)
#     url = r.text.split()[-1]
#     print("!!! Next URL is", prefix + url, "!!!")
# res_file = open("url_res.txt","w")
# print(r.text, file=res_file)


import requests
url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
while name[:2] != 'We':
    name = requests.get(url + name).text
    print(name)
