def render_tweets_html(tweets):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>Tweetfeed</title>
    </head>
    <body>
      <h1 class="">Tweets</h1>
    '''

    for tweet in tweets:
        html += '''
        <div class="tweet">
          <h1>{}</h1>
          <h2>{}</h2>
          <p>Posted on {}</p>
          <p>Verified: {}</p>
        '''.format(tweet['name'], tweet['username'], tweet['datetime'], tweet['verified'])

        if 'text' in tweet:
            html += '<p>{}</p>'.format(tweet['text'])

        if 'image' in tweet:
            html += '<img src="{}" alt="Tweet Image">'.format(tweet['image'])

        if 'video' in tweet:
            html += '<video src="{}" controls></video>'.format(tweet['video'])
            html += '<img src="{}" alt="Video Thumbnail">'.format(tweet['video_thumb'])

        html += '''
          <p>Likes: {}</p>
          <p>Retweets: {}</p>
          <p>Replies: {}</p>
        </div>
        '''.format(tweet.get('likes', '0'), tweet.get('retweets', '0'), tweet.get('replies', '0'))

    html += '''
    </body>
    </html>
    '''

    return html