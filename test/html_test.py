from jinja2 import Template
from datetime import datetime

def date_formatter(date: str):
    input_format = "%Y-%m-%dT%H:%M:%S.000Z"
    output_format = "%H:%M %d.%m.%Y"
    datetime_obj = datetime.strptime(date, input_format)
    return datetime_obj.strftime(output_format)


def render_tweets_html(tweets:list):
    for tweet in tweets:
        if "datetime" in tweet:
            tweet["datetime"] = date_formatter(tweet["datetime"])

    template_str = open("template.html", "r", encoding="utf-8").read()

    template = Template(template_str)
    rendered_html = template.render(tweets=tweets)
    return rendered_html


# Example data
tweets = [
{'text': '', 'name': 'jupyter_meowbooks.ipynb', 'username': '@untitled01ipynb', 'datetime': '2023-06-04T21:39:05.000Z', 'verified': False, 'url': '/untitled01ipynb/status/1665473272413138944', 'image': 'https://pbs.twimg.com/media/FxzzG6zWIAA6-hT?format=jpg&name=small', 'replies': '2'},

{'text': 'AI is taking over', 'name': 'AK', 'username': '@_akhaliq', 'datetime': '2023-06-04T15:12:55.000Z', 'verified': True, 'url': '/_akhaliq/status/1665376088594214917', 'video': 'https://video.twimg.com/ext_tw_video/1665375924206878720/pu/vid/406x720/TGUYq7SIlXQzP6tZ.mp4?tag=12', 'video_thumb': 'https://pbs.twimg.com/ext_tw_video_thumb/1665375924206878720/pu/img/gUo2J7DyD5CkWMnO.jpg', 'likes': '4,380', 'retweets': '519', 'replies': '105', 'views': '563713'},

{'text': 'SEVGİLİ KARDEŞLERİM\n\nFastapi öğrenin. Evet sana söylüyorum 4. sınıfa giden mezun olmak üzere olan genç. Evet sana söylüyorum AI çalışmak isteyen kardeşim. Fastapi öğrenin. Django diye bi şey varmış diyen junior, sen de fastapi öğren\n\nFASTAPI ÖĞRENMEYEN KİMSE KALMASIN ARTIK', 'name': 'ege ', 'username': '@mrboyoz_', 'datetime': '2023-06-04T14:29:08.000Z', 'verified': False, 'url': '/mrboyoz_/status/1665365069553709056', 'likes': '435', 'retweets': '38', 'replies': '14', 'views': '52991'},

{'text': 'Avrupa Türklere kapıyı tamamen kapattı demek için baya dangalak olmak lazım.', 'name': 'midorikocak', 'username': '@midorikocak', 'datetime': '2023-06-03T06:21:54.000Z', 'verified': False, 'url': '/midorikocak/status/1664880067577610240', 'likes': '28', 'retweets': '1', 'replies': '2', 'views': '4464'},

{'text': 'turkiyenin yillik kaybettigi kapasiteden bahseden belki alakasiz ama bir bakkal hesabi yapalim tek bir sirket uzerinden\n- ASML\'nin calisanlarinin ~%2.5\'i turk\n- ASML\'nin "net" geliri 5.6B euro\n- Turk sayisina oranladigimizda yillik 138 milyon euro', 'name': 'ege ', 'username': '@mrboyoz_', 'datetime': '2023-06-01T19:02:10.000Z', 'verified': False, 'url': '/mrboyoz_/status/1664346618240311335', 'image': 'https://pbs.twimg.com/media/FxjunU0WIA8K9tt?format=jpg&name=small', 'likes': '31', 'retweets': '8', 'replies': '6', 'views': '4594'},

{'text': 'Hosting @RobertKennedyJr’s upcoming Space', 'name': 'Elon Musk', 'username': '@elonmusk', 'datetime': '2023-06-04T14:40:50.000Z', 'verified': True, 'url': '/elonmusk/status/1665368017125900288', 'likes': '53.3K', 'retweets': '9,735', 'replies': '5,103', 'views': '7753789'},

{'text': 'A number of political shows and podcasts have announced their intention to upload on Twitter alongside, or even in place of, Youtube. This new move by Youtube may be intended to stem the bleeding. \n\nSource: \n\n https://axios.com/2023/06/02/us-election-fraud-youtube-policy…', 'name': 'T(w)itter Daily News \uea00', 'username': '@TitterDaily', 'datetime': '2023-06-04T11:58:17.000Z', 'verified': True, 'url': '/TitterDaily/status/1665327109324013568', 'likes': '7,169', 'retweets': '1,202', 'replies': '634', 'views': '2512203'},      

{'text': 'Falcon 9 launches 22 @Starlink satellites to orbit from Florida', 'name': 'SpaceX', 'username': '@SpaceX', 'datetime': '2023-06-04T13:36:07.000Z', 'verified': True, 'url': '/SpaceX/status/1665351728412372992', 'image': 'https://pbs.twimg.com/media/FxyER7YaMAEm7iD?format=jpg&name=small', 'likes': '15.5K', 'retweets': '1,991', 'replies': '668', 'views': '2408925'},

{'text': 'Falcon 9’s first stage has landed on the Just Read the Instructions droneship', 'name': 'SpaceX', 'username': '@SpaceX', 'datetime': '2023-06-04T12:29:57.000Z', 'verified': True, 'url': '/SpaceX/status/1665335077562384395', 'video': 'https://video.twimg.com/amplify_video/1665334878630731778/vid/1280x720/1qijMN6K4Gk1fsir.mp4?tag=14', 'video_thumb': 'https://pbs.twimg.com/amplify_video_thumb/1665334878630731778/img/SxphJcgYWm-XYI7D.jpg', 'likes': '16.2K', 'retweets': '1,963', 'replies': '658', 'views': '2723914'},

{'text': '', 'name': 'Elon Musk', 'username': '@elonmusk', 'datetime': '2023-06-04T05:02:33.000Z', 'verified': True, 'url': '/elonmusk/status/1665222486915522564', 'image': 'https://pbs.twimg.com/media/FxwPBq4XoAAzF6p?format=jpg&name=small', 'likes': '104.5K', 'retweets': '10.4K', 'replies': '11K', 'views': '21479774'},
]

html = render_tweets_html(tweets)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
