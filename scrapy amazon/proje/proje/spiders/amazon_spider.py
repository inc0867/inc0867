import scrapy


class amazonSpider(scrapy.Spider):

    name = "amazon"
    i = 0
    dosya = open("veri.txt","a+",encoding="utf-8")
    start_urls = [
        "https://www.amazon.com.tr/s?k=monster+notebook&crid=1UF7QUQD9DPF1&sprefix=%2Caps%2C122&ref=nb_sb_ss_recent_1_0_recent"
    ]



    def parse(self, response):
        modeladı = response.css("div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style span::text").extract()
        fiyat = response.css("div.a-row.a-size-base.a-color-base span.a-price-whole::text").extract()

        while self.i < len(modeladı):
            self.dosya.write("***********************************************")
            self.dosya.write("\n")
            self.dosya.write(modeladı[self.i])
            self.dosya.write("\n")
            self.dosya.write(fiyat[self.i])
            self.dosya.write("\n")
        
            self.i += 1



        next_url = response.css("a.s-pagination-item.s-pagination-button.s-pagination-separator::attr(href)").extract_first()

        if next_url is not None:
            yield scrapy.Request(url="https://www.amazon.com.tr" + next_url ,callback= self.parse)

        else:
            self.dosya.close()