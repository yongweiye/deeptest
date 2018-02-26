# -* coding:utf-8 *-
__author__ = 'nancy'

import urllib.request
import csv
import codecs

if __name__ == "__main__":
    print("urllib抓取豆瓣eg：搜索Python")

    url = "https://api.douban.com/v2/book/search?q=python"
    response  = urllib.request.urlopen(url)

    # trans bytes to string
    ebook_str = response.read().decode()

    # trans string to dict
    ebook_dict = eval(ebook_str)

    print(type(ebook_dict))
    print(ebook_dict)

    count = ebook_dict["count"]
    total = ebook_dict["total"]

    with codecs.open('httpbook.csv', 'w', 'utf-8') as csvfile:
        writer = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["book", "authot", "des", "publ", "price"])

        for book in ebook_dict["books"]:
            writer.writerow([book["title"],
                ",".join(book["author"]),
                book["summary"],
                book["publisher"],
                book["price"]])

        # 从第二页开始，获取其他书籍信息
        '''
        for start in range(1, int(total/count)+1):
            url =  "https://api.douban.com/v2/book/search?q=python&start=%d" % start
            try:
                resp = urllib.request.urlopen(url)
            except:
                print("封ip啦")
                break

            ebook_str = resp.read().decode()
            ebook_dict = eval(ebook_str)

            for book in ebook_dict["books"]:
                writer.writerow([book["title"],
                    ",".join(book["author"],
                    book["summary"]),
                    book["publisher"],
                    book["price"]])
        '''