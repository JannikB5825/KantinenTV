import fetcher
with open ("text.txt", "w", encoding = "utf-8") as f:   
    for x in fetcher.ArticleFetcher.fetchIntra():
        for y in x:
            f.write(y+"\n")