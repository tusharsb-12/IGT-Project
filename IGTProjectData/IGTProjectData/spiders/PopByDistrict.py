import scrapy


class PopulationOfDistrict(scrapy.Spider):
    name = "districtPop"

    def start_requests(self):
        urls = [
            "https://www.citypopulation.de/en/india/admin/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = 'DistrictPop'
        filename = f'{page}.txt'
        x_list1 = response.css('table')[0]
        x_list = x_list1.css('thead th a::text').getall()
        x_list[2] += '1'
        x_list[3] += '2'
        x_list[4] += '3' 
        y_list = x_list1.css('tbody')
        z_list = []
        for yl in y_list :
            xyz = yl.css(f'tr')
            for j in xyz :
                z = {}
                ab,b = j.css(f'td a span::text').getall(),j.css(f'td::text').getall()
                for a in ab :
                    z[x_list[0]] = a
                    c = 0
                    for i in x_list[1:] :
                        z[i] = b[c]
                        c += 1
                    yield z
            
        #     z_list.append([])
        # with open(filename, 'wb') as f:
        #     f.write(str(x_list).encode())
        #     f.write(str(z_list).encode())
