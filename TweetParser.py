from playwright.sync_api import sync_playwright
from parsel import Selector
import time
import threading


def parse_tweets(tweets: str):
    selector = Selector(text=tweets)

    tweets = selector.xpath(
        '//div/div/article')

    results = []
    for i, tweet in enumerate(tweets):
        # using data-testid attribute we can get tweet details:
        found = {
            "text": "".join(tweet.xpath(".//*[@data-testid='tweetText']//text()").getall()),
            "name": tweet.xpath(
                ".//div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span//text()").get(),
            "username": tweet.xpath(
                ".//div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a/div/span//text()").get(),
            "avatar": tweet.xpath(
                ".//div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/a/div[3]/div/div[2]/div/img/@src").get(),
            "handle": tweet.xpath(".//*[@data-testid='User-Names']/div[2]//text()").get(),
            "datetime": tweet.xpath(".//time/@datetime").get(),
            "verified": bool(tweet.xpath(".//svg[@data-testid='icon-verified']")),
            "url": tweet.xpath(".//time/../@href").get(),
            "image": tweet.xpath(".//*[@data-testid='tweetPhoto']/img/@src").get(),
            "video": tweet.xpath(".//video/@src").get(),
            "video_thumb": tweet.xpath(".//video/@poster").get(),
            "likes": tweet.xpath(".//*[@data-testid='like']//text()").get(),
            "retweets": tweet.xpath(".//*[@data-testid='retweet']//text()").get(),
            "replies": tweet.xpath(".//*[@data-testid='reply']//text()").get(),
            "views": (tweet.xpath(".//*[contains(@aria-label,'Views')]").re("(\d+) Views") or [None])[0],
            # "links": tweet.xpath(".//a[contains(text(),'http')]/@href"),
            "tweetLink": tweet.xpath(".//div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a/@href").get(),
        }

        # main tweet (not a reply):
        if i == 0:
            found["views"] = tweet.xpath('.//span[contains(text(),"Views")]/../preceding-sibling::div//text()').get()
            found["retweets"] = tweet.xpath('.//a[contains(@href,"retweets")]//text()').get()
            found["quote_tweets"] = tweet.xpath('.//a[contains(@href,"retweets/with_comments")]//text()').get()
            found["likes"] = tweet.xpath('.//a[contains(@href,"likes")]//text()').get()
        results.append({k: v for k, v in found.items() if v is not None})

    return results


def get_user_tweets(username: str, tweet_list: list, index: int):
    with sync_playwright() as p:
        URL = f"https://twitter.com/{username}"
        N_TWEETS = 5

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url=URL)

        time.sleep(1)

        tweets = ""
        for i in range(N_TWEETS):
            page.keyboard.down("PageDown")
            time.sleep(0.2)
            tweet = page.locator(
                f'xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{i+1}]')
            tweets += tweet.inner_html() + "\n\n"

        tweet_list[index] = tweets


def get_multiple_users_tweets(usernames: list, save_html: bool = False):
    t = ""
    with sync_playwright() as p:
        for username in usernames:
            URL = f"https://twitter.com/{username}"
            N_TWEETS = 5

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url=URL)

            time.sleep(1)

            tweets = ""
            for i in range(N_TWEETS):
                page.keyboard.down("PageDown")
                time.sleep(0.2)
                tweet = page.locator(
                    f'xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{i+1}]')
                tweets += tweet.inner_html() + "\n\n"
            t += tweets

        if save_html:
            with open('tweets.html', 'w', encoding="utf-8") as file:
                file.write(t)

        return t


def get_multiple_users_tweets_async(usernames: list, save_html: bool = False):
    max_n_threads = 5
    threads = []
    tweet_list = [None] * len(usernames)

    for i in range(0, len(usernames), max_n_threads):
        for j in range(i, min(i+max_n_threads, len(usernames))):
            print(f"Getting tweets for {usernames[j]} using thread {j}")
            thread = threading.Thread(target=get_user_tweets, args=(usernames[j], tweet_list, j))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            print(f"Thread {thread.name} finished")

    time.sleep(1)

    t = ""
    for tweet in tweet_list:
        t += tweet

    if save_html:
        with open('tweets.html', 'w', encoding="utf-8") as file:
            file.write(t)

    return t
