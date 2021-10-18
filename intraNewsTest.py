import fetcher

with open("news.csv", "a") as a:
    for x in fetcher.ArticleFetcher.fetch():
        for y in x:
            a.write(y + "   ")
        a.write("\n")