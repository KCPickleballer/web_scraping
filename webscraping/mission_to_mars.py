from splinter import Browser
from bs4 import BeautifulSoup

import pandas as pd
import requests

def nasaMarsNews():
    #url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    results = soup.find_all('div', class_="image_and_description_container")

    elements = soup.find_all('div', class_=['rollover_description_inner', 'content_title'])
    news_p= []
    news_title = []
    i = 0
    j = 0
    k = 0
    for el in elements:
        try:
            if i % 2 == 0:
                    news_p.append(el.get_text())
                  #  print(f'i = {i} news_p = {news_p[j]}')
                    j += 1
            else:
                    #news_title.append(el.get_text())
                    news_title.append(el.find('a').text)

                   # print(f'i = {i} news_title = {news_title[k]}')
                    k += 1
            
        except AttributeError as e:
                print(e)
            
        i += 1
    marsNews = { 'NewsTitle': news_title,
                 'NewsParagraph': news_p }
    print(marsNews)             

    #return marsNews
    return (news_title[0], news_p[0])

def weatherTweet():
    url = 'https://twitter.com/MarsWxReport?lang=en'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find('div', class_="js-tweet-text-container")
    #print(results.prettify())

    marsWthr= results.find('p').text

    #print(marsWthr)
    return (marsWthr)

def marsFacts():

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ['Fact_desc', 'Fact_value']
    print(df)

    df = df.set_index('Fact_desc')
    print("test")
    print(df)


    html_table = df.to_html()

    html_table_str = html_table.replace('\n', '')

    

    return (html_table_str)


def marsHemis():

    try:
        executable_path = {'executable_path': 'chromedriver.exe'}
        print("pt1")
        browser = Browser('chrome', **executable_path, headless=False)
        print("pt2")

        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'    
        browser.visit(url)
        print("pt3")

        html = browser.html
        print("pt4")
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        print("pt5")
    # Retrieve all elements that contain book information
    #articles = soup.find_all('article', class_='product_pod')
    #print(soup.prettify)

        slop = soup.find_all('div', class_='collapsible results')
        print(slop.prettify())
    except:
            

        hem1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
        hem1Title = 'Cerberus Hemisphere Enhanced'

        hem2 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
        hem2Title = 'Schiaparelli Hemisphere Enhanced'

        hem3 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
        hem3Title = 'Syrtis Major Hemisphere Enhanced'

        hem4 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
        hem4Title = 'Valles Marineris Hemisphere Enhanced'

        #hem1TitleLngth =  hem1Title.len()
        #print(hem1TitleLngth)

    hemisphere_image_urlsList = [
        {'title': hem1Title,    'img_url': hem1},
        {'title': hem2Title,    'img_url': hem2},
        {'title': hem3Title,    'img_url': hem3},
        {'title': hem4Title,    'img_url': hem4}
    ] 

    hemList = [hem1, hem2, hem3, hem4]
    titleList = [hem1Title, hem2Title, hem3Title, hem4Title ]
    
   # return (hemisphere_image_urlsList)
    return (hemList, titleList)

def morrisTest():
    executable_path = {'executable_path': 'chromedriver.exe'}
    print(0)
    browser = Browser('chrome')
    print(1)
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    print(2)
    browser.get(hemisphere_url)
    # # hemisphere_html = browser.html
    # # hemisphere_soup = bs(hemisphere_html, 'html.parser')
    # # links = hemisphere_soup.find_all('a', class_='product-item')

    # # hemi_names = []
    # # for link in links:
    # #     if link.text:
    # #             hemi_names.append(link.text) 

    # # hemi_img = []
    # # for i in range(1, 9, 2):
    # #     browser.visit(hemisphere_url)
    # #     hemisphere_html = browser.html
    # #     hemisphere_soup = bs(hemisphere_html, 'html.parser')
    # #     detail_links = browser.find_by_css('a.product-item')
    # #     detail_links[i].click()
    # #     browser.find_link_by_text('Sample').first.click()
    # #     browser.windows.current = browser.windows[-1]
    # #     hemi_img_html = browser.html
    # #     browser.windows.current = browser.windows[0]
    # #     browser.windows[-1].close()
    # #     hemi_img_soup = bs(hemi_img_html, 'html.parser')
    # #     hemi_img_path = hemi_img_soup.find('img')['src']
    # #     hemi_img.append(hemi_img_path)

    # # hemisphere_dicts = []
    # # for i in range(4):
    # #     hemisphere_dict = {}
    # #     hemisphere_dict['title'] = hemi_names[i]
    # #     hemisphere_dict['url'] = hemi_img[i]
    # #     hemisphere_dicts.append(hemisphere_dict)  

    return()  
def featuredImg():
    url =' https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    #soup = BeautifulSoup(response.text, 'lxml')
    #print(soup.prettify())

    results = soup.find('a', id="full_image")['data-fancybox-href']

    featuredImg = url + '/' + results

    print(featuredImg)



featuredImg()
hemiTup = marsHemis()
print(hemiTup)
#print(nasaMarsNews())
marsNewsTuple = nasaMarsNews()
# print(f' title : {marsNewsTuple[0]}, news_para: {marsNewsTuple[1]}')
ars_weather = weatherTweet()
 marFacts_html_tbl_str = marsFacts()
#print(marFacts_html_tbl_str)
#hemisphere_image_urls = marsHemis()
# hemi_dicts = 
#morrisTest()
# print(hemi_dicts)
mars_info = { "mars_weather": mars_weather,
          "mars_news_title": marsNewsTuple[0],
          "mars_news_para": marsNewsTuple[1],
          "marsFacts_table":  marFacts_html_tbl_str
     }
# print("mars_info: ")
# print(mars_info)

