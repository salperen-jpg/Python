#importing new libraries 
import requests
from  bs4 import BeautifulSoup
import time

#Main function
def main():
    url='https://www.n11.com/arama?q=hyperx+flight'
    #Request for website.
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    #Getting related html tag from web page.
    productLink=soup.body.select('div.pro > a')
    #List for product links.
    productLinks=[link['href'] for link in productLink]
    print(productLinks)

    prices=list()
    for i in range(len(productLinks)):
        try:
            r2=requests.get(productLinks[i])
        except :
            print('We did not access this Url.')
        r2=requests.get(productLinks[i])
        web=BeautifulSoup(r2.content)
        productAttr=web.find('div',attrs={'class':'feaItem'}).find('span').text
        productLabel=web.find('a',attrs={'class':'data'}).find('span').text
        productName=web.find('div',attrs={'class':'nameHolder'}).find('h1').string.strip()
        productOlPrice=web.find('del',attrs={'class':'oldPrice'}).string
        if productOlPrice==None :
            productOlPrice=web.find('div',attrs={'class':'newPrice'}).find('ins').text
        productPrice=web.find('div',attrs={'class':'newPrice'}).find('ins').text
        print('Product ' + str(i+1))
        print('{}\n{}\n{}\n{}'.format(productName,productAttr,productLabel,productPrice))
        print('*'*100)
        
        price=productPrice[:-3] # To convert all price to integer value.
        prices.append(price)
    
    
    print('The best price is finding ,please wait......')
    time.sleep(5)
        
        
    minPrice=min(prices)

    a=prices.index(minPrice)
    #print(a)

    productSuggestion(a,productLink)


#Finding lowest price.
def productSuggestion(b,productLinks):
   adviceUrl=productLinks[b]['href']
   advice_r=requests.get(adviceUrl)
   advice_soup=BeautifulSoup(advice_r.content,'lxml')
   advice_title=advice_soup.title.text
   productAttr=advice_soup.find('div',attrs={'class':'feaItem'}).find('span').text
   productLabel=advice_soup.find('a',attrs={'class':'data'}).find('span').text
   productOlPrice=advice_soup.find('del',attrs={'class':'oldPrice'}).string
   if productOlPrice==None :
        productOlPrice=advice_soup.find('div',attrs={'class':'newPrice'}).find('ins').text
   productPrice=advice_soup.find('div',attrs={'class':'newPrice'}).find('ins').text
   print('-'*100)
   print('{}\n{}\n{}\n{}'.format(advice_title,productAttr,productLabel,productPrice))

    


main()




    