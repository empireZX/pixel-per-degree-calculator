import requests
from bs4 import BeautifulSoup
headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
for start_num in range(0,250,25):
    URL=f"https://search.jd.com/Search?keyword=%E9%BC%A0%E6%A0%87&enc=utf-8&wq=%E9%BC%A0%E6%A0%87&pvid=504c42530e9f49bd87a0cf5327006c5b"
    response= requests.get(URL,headers=headers)
   # print(response.status_code)
    content=response.text
    soup = BeautifulSoup(content,"html.parser")
    all_mouses=soup.findAll("em")
    for mouse in all_mouses:
        print(mouse.string)
    #    mouse_string=mouse.string
    #    if"/"not in title_string:
    #       print(mouse_string)