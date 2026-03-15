import instaloader


def crawl_instagram(username, max_posts=5):

    events = []

    print(f"Crawling Instagram: {username}")

    try:

        loader = instaloader.Instaloader()

        profile = instaloader.Profile.from_username(
            loader.context,
            username
        )

        count = 0

        for post in profile.get_posts():

            if post.caption:

                events.append({
                    "raw_text": post.caption,
                    "source_url": f"https://www.instagram.com/{username}/"
                })

            count += 1

            if count >= max_posts:
                break

    except Exception as e:

        print("Instagram crawler error:", username, e)

    return events