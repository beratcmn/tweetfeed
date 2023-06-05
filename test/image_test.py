from PIL import Image, ImageDraw, ImageFont


def create_tweet_image(tweet_data):
    # Define image dimensions
    image_width = 800
    image_height = 300

    # Create a blank image with a darker background
    background_color = (30, 30, 30)  # Dark gray color
    image = Image.new('RGB', (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # Define font styles
    font_family = 'arial.ttf'
    font_size = 18
    line_spacing = 5

    # Define text positions
    text_x = 10
    text_y = 10

    # Load fonts
    username_font = ImageFont.truetype(font_family, font_size + 2)
    tweet_font = ImageFont.truetype(font_family, font_size)

    # Draw username
    username = tweet_data['username']
    draw.text((text_x, text_y), f'@{username}', fill='white', font=username_font)

    # Adjust the text position
    text_y += font_size + line_spacing

    # Split the tweet text into words
    words = tweet_data['text'].split()

    # Create lines to fit the text within the image width
    lines = []
    current_line = ''
    for word in words:
        if draw.textbbox((0, 0), current_line + word, font=tweet_font)[2] <= image_width - 2 * text_x:
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    # Draw the wrapped text
    for line in lines:
        draw.text((text_x, text_y), line, fill='white', font=tweet_font)
        text_y += font_size + line_spacing

    # Save the image
    image.save('tweet_image.png')


# Example usage
tweet_data = {
    'text': 'AI is taking over',
    'username': '@_akhaliq',
    'datetime': '2023-06-04T15:12:55.000Z',
    'verified': True,
    'url': '/_akhaliq/status/1665376088594214917',
    'video': 'https://video.twimg.com/ext_tw_video/1665375924206878720/pu/vid/406x720/TGUYq7SIlXQzP6tZ.mp4?tag=12',
    'video_thumb': 'https://pbs.twimg.com/ext_tw_video_thumb/1665375924206878720/pu/img/gUo2J7DyD5CkWMnO.jpg',
    'likes': '3,868',
    'retweets': '452',
    'replies': '100',
    'views': '500561'
}

create_tweet_image(tweet_data)
