import TweetParser as tp
import PageCreator as pc


def get_and_parse_tweets(usernames: list):
    tweets = tp.get_multiple_users_tweets_async(usernames=usernames, save_html=False)
    parsed_tweets = tp.parse_tweets(tweets=tweets)

    return parsed_tweets


def main():
    # usernames = ["beratfromearth", "elonmusk"]
    # usernames = ["beratfromearth"]
    usernames = ["beratfromearth", "joisino_en", "jayzpio", "dair_ai",
                 "LangChainAI", "TheBlokeAI", "sama", "huggingface"]

    usernames = list(set(usernames))

    parsed_tweets = get_and_parse_tweets(usernames=usernames)
    file = pc.render_and_save_html(tweets=parsed_tweets)


if __name__ == "__main__":
    main()
