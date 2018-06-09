def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode()
    except:
        return ''

def union(list1, list2):
    for e in list2:
        if e not in list1:
            list1.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1: end_quote]

        return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            if url[:4] == 'http' or url[:3] == 'www':
                links.append(url)
            page = page[endpos:]
        else:
            return links

def crawl_web(seed, max_depth = 1000):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0

    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()

        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
            print(page)

        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1

    return crawled


seed =('https://xkcd.com/353/')
#seed =('https://yandex.ru')

print(crawl_web(seed, 3))

