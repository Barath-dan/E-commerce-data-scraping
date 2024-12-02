from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

laptop_dict={
    'name':[],
    'processor':[],
    'ram':[],
    'os':[],
    'ssd':[],
    'price':[],
    'link':[],
}

driver=webdriver.Chrome()
processor=""
ram = ""
os = ""
ssd = ""
name=""
link=""
price=""
page=1
while True:
    print('*******************************')
    print(f'Page No {page}')
    print('*******************************')
    url=f'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.processor_brand%255B%255D%3DIntel&p%5B%5D=facets.processor_brand%255B%255D%3DApple&p%5B%5D=facets.operating_system%255B%255D%3DWindows%2B10&p%5B%5D=facets.operating_system%255B%255D%3DMac%2BOS&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi3&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi7&p%5B%5D=facets.processor%255B%255D%3DM1%2BMax&p%5B%5D=facets.processor%255B%255D%3DM1%2BPro&p%5B%5D=facets.processor%255B%255D%3DM2&p%5B%5D=facets.processor%255B%255D%3DM2%2BMax&p%5B%5D=facets.processor%255B%255D%3DM3&p%5B%5D=facets.processor%255B%255D%3DM3%2BPro&p%5B%5D=facets.processor%255B%255D%3DM3%2BMax&p%5B%5D=facets.processor%255B%255D%3DM4&p%5B%5D=facets.processor%255B%255D%3DM4%2BMax&p%5B%5D=facets.processor%255B%255D%3DM4%2BPro&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B7%2BOcta%2BCore&page={page}'
    time.sleep(10)
    driver.get(url)
    page_html=driver.page_source
    soup=BeautifulSoup(page_html,'html.parser')
    container=soup.find('div',class_='DOjaWF')
    Laptops=container.find_all('div',class_='yKfJKb')
#name #processor #ram #os #ssd
    for Laptop in Laptops:
        name=Laptop.find('div',class_='KzDlHZ').get_text(strip=True).split('-')[0]
        print(name)
        laptop_dict['name'].append(name)
        features=Laptop.find_all('li',class_='J+igdf')
        for feature in features:
            feature_text=feature.get_text(strip=True)
            if "Processor" in feature_text:
                processor=feature_text
                laptop_dict['processor'].append(processor)
            elif "RAM" in feature_text:
                ram=' '.join(feature_text.split()[:-1])
                laptop_dict['ram'].append(ram)
            elif "Operating System" in feature_text:
                os=' '.join(feature_text.split()[:-2])
                laptop_dict['os'].append(os)
            elif "SSD" in feature_text:
                ssd=' '.join(feature_text.split()[:-1])
                laptop_dict['ssd'].append(ssd)
        print(processor)
        print(ram)
        print(os)
        print(ssd)
        price_div=Laptop.find('div',class_='Nx9bqj')
        price=price_div.get_text(strip=True) if price_div else 'Price info not available'
        laptop_dict['price'].append(price)
        print(price)
        link='https://www.flipkart.com'+soup.find('a',class_='CGtC98')['href']
        laptop_dict['link'].append(link)
        print(link)
    pagination_div = driver.find_element(By.CLASS_NAME, '_1G0WLw')
    last_page = pagination_div.find_element(By.TAG_NAME, 'span').text
    last_page_number = int(last_page.split()[-1])

    if page >= last_page_number:
        print("Last page reached. Exiting...")
        break
    else:
        page+=1
driver.quit()

