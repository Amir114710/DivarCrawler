import scrapy

url = 'https://divar.ir/v/-/{token}'

token_file = open('/Users/Amir/OneDrive/دسکتاپ/bird_divar/tokens.txt' , 'r' , encoding='utf-8')

tokens = token_file.read().split(',')
token_file.close()

class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self , reponse):

        address = reponse.css('div div.kt-page-title__subtitle--responsive-sized::text').extract()

        price = reponse.css('div p.kt-unexpandable-row__value::text').extract_first()

        title = reponse.css('div div.kt-page-title__title--responsive-sized::text').extract()

        image = reponse.css('div div.kt-offset-1').extract()

        discription = reponse.css('div p.kt-description-row__text--primary::text').extract()
                
        phone = reponse.css('div div.copy-row__content').extract()


        yield {
            'Title' : title , 
            'Image' : image ,
            'Discription' : discription ,
            'Phone' : phone ,
            'Address' : address , 
            'Price' : price
        }

