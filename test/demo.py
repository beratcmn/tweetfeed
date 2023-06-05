from playwright.sync_api import sync_playwright
from parsel import Selector


def parse_tweets(tweets: str):
    selector = Selector(text=tweets)

    tweets = selector.xpath(
        '//div/div/article')

    results = []
    for i, tweet in enumerate(tweets):
        # using data-testid attribute we can get tweet details:
        found = {
            "text": "".join(tweet.xpath(".//*[@data-testid='tweetText']//text()").getall()),
            "username": tweet.xpath(".//*[@data-testid='User-Names']/div[1]//text()").get(),
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
        }
        # main tweet (not a reply):
        if i == 0:
            found["views"] = tweet.xpath('.//span[contains(text(),"Views")]/../preceding-sibling::div//text()').get()
            found["retweets"] = tweet.xpath('.//a[contains(@href,"retweets")]//text()').get()
            found["quote_tweets"] = tweet.xpath('.//a[contains(@href,"retweets/with_comments")]//text()').get()
            found["likes"] = tweet.xpath('.//a[contains(@href,"likes")]//text()').get()
        results.append({k: v for k, v in found.items() if v is not None})

    return results


def get_user_tweets(username: str):
    with sync_playwright() as p:
        URL = f"https://twitter.com/{username}"
        N_TWEETS = 5

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url=URL)

        tweets = ""
        for i in range(N_TWEETS):
            page.keyboard.down("PageDown")
            tweet = page.locator(
                f'xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{i+1}]')
            tweets += tweet.inner_html() + "\n\n"

        # with open('tweets.html', 'w', encoding="utf-8") as file:
            # file.write(tweets)

        return tweets


def get_multiple_users_tweets(usernames: list):
    t = ""
    with sync_playwright() as p:
        for username in usernames:
            URL = f"https://twitter.com/{username}"
            N_TWEETS = 5

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url=URL)

            tweets = ""
            for i in range(N_TWEETS):
                page.keyboard.down("PageDown")
                tweet = page.locator(
                    f'xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{i+1}]')
                tweets += tweet.inner_html() + "\n\n"
            t += tweets
        return t


if __name__ == "__main__":
    # tweets = get_user_tweets(username="beratfromearth")
    tweets = get_multiple_users_tweets(usernames=["beratfromearth", "elonmusk"])
    parsed_tweets = parse_tweets(tweets=tweets)

    for tweet in parsed_tweets:
        print(tweet)
        print()
