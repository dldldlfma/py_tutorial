from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint

def keyword_preprocessing(word):
    """
    검색 keyword를 google 검색 URL과 붙이기 위해 적합한 형태로 전환합니다. 
    띄어쓰기를 +로 바꾸는 정도 입니다. 
    """
    change_word = list(word)
    for i in range(len(change_word)):
        if(change_word[i]==' '):
            change_word[i]='+'
    change_word = ''.join(change_word)
    return change_word

def single_keyword_search(keyword):

    """
    구글에 keyword 검색결과를 html로 받아온뒤에 그 안에 일반 게시물 분류에 속하는
    class='r' 부분만 모아서 return해주는 함수 입니다.  

    Args:
       Keyword (String) : 구글에 검색할 Keyword
    
    Returns:
       title_list (bs4.element.ResultSet) : 구글 검색에서 확인된 일반게시물(class='r')들의 모음
    """
    URL = 'https://www.google.com/search?q=' +keyword_preprocessing(keyword)

    driver = webdriver.Chrome("C:/Users/ksg/py_tutorial/chromedriver.exe")
    driver.implicitly_wait(1)

    driver.get(URL)
    driver.implicitly_wait(2)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    title_list = soup.find_all(name='div',attrs={'class':'r'})
    return title_list

def google_contents_rank(keyword_list, channel_list):
    """
    구글에서 keyword로 검색했을때 channel_list속 채널에서 몇개의 데이터가 검출되었는지를 확인할 수 있는 코드 입니다. 
    """
    for keyword in keyword_list:
    title_list = single_keyword_search(keyword)
    for i,val in enumerate(title_list):
        for channel in channel_list:
            title=str(val).split("\"")[3]
            if(title[0:len(channel)]==channel):
                print(keyword,end=" : ")
                print(i,end=" => ")
                print(val.text[0:40])
    print("")
