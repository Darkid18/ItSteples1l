import  requests
from bs4 import BeautifulSoup
# response = requests.post("https://httpbin.org/get", data = "test data", headers = ("h1" "Test title"))
# print(response.content)

res_palse_list = []
responce = requests.get("https://coinmarketcap.com/")
responce_text = responce.text
responce_parse = responce_text.split("<span>")

for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_palse_list.append(parse_elem_2)

bitcoin_rate = res_palse_list[0]
print("Bitcoin rate now :     ",bitcoin_rate)



response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    s_list = soup.find_all("a", {"href":"/currencies/bitcoin/#markets"})
    res = s_list[0].find("<span>")
    print(s_list)
else:
    print("Error")