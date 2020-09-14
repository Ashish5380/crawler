import re
import ast
import scrapy
#from dateutil.parser import parse

from ecommerce_crawler.onedirect_common.config.review_urls import ReviewUrls
from ecommerce_crawler.onedirect_common.utils.logger import logger
from ecommerce_crawler.amazon_crawler.items import AmazonReviewItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = ReviewUrls().read_all_urls()

    def parse(self, response, **kwargs):
        item = AmazonReviewItem()

        logger.info('A response from %s just arrived!', response.url)

        data = response.css('#cm_cr-review_list')

        logger.info("Data fetched from amazon page :: {0}".format(data))

        star_rating = data.css('.review-rating')

        comments = response.xpath('//span[@class="a-size-base review-text review-text-content"]/span/text()').extract()

        author = data.css('.a-profile-name')

        posted_date = data.css('.review-date')

        comment_headers = data.css('.review-title')

        review_link = data.css('.a-link-normal::attr(href)').getall()

        user_profile = data.css('.a-profile::attr(href)').getall()

        verified_user = data.css('.review-format-strip')

        for attr in zip(star_rating, comments, author, posted_date, comment_headers, review_link, user_profile,
                        verified_user):
            item["star_rating"] = attr[0].xpath('.//text()').extract()
            item["rating_text"] = attr[1]
            item["author"] = attr[2].xpath('.//text()').extract()

            item["review_header"] = attr[4].xpath('.//span/text()').extract()
            item["review_link"] = 'amazon.in' + attr[5]
            item["user_profile"] = 'amazon.in' + attr[6]
            item["verified_user"] = attr[7].xpath('.//text()').extract()
            date = attr[3].xpath('.//text()').extract()
            dt = re.sub("Reviewed in India on ", "", str(date))
            dt = ast.literal_eval(dt)
            # print(" DT" + dt)
            da = parse(dt[0])
            item["posted_dates"] = da.strftime('%Y-%m-%d %H:%M:%S')
            yield item

        next_page = response.css('.a-last a ::attr(href)').extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
