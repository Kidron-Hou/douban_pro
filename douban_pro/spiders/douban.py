import scrapy

from douban_pro.items import DoubanProItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath('//*[@id="content"]/div/div/ol/li')
        for movie in movie_list:
            item = DoubanProItem()
            item['serial_number'] = movie_list.index(movie)+1
            item['movie_name'] = movie.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            intro_content = movie.xpath('./div/div[2]/div[2]/p[1]/text()').extract()
            norm_content = [intro.strip() for intro in intro_content]

            item['introduce'] = ''.join(norm_content)
            item['star'] = movie.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['evaluate'] = movie.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            item['describe'] = movie.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()

            yield item

