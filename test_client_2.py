import sys
import time
import os

from utils import (
    hms_string,
)

from nbs_client import (
    get_artist,
)

DEFAULT_MAX_ARTISTS = 100

user_token = os.environ.get('NEXT_BIG_SOUND_TOKEN')

def main(argv):

    if not user_token:
        print 'Missing NEXT_BIG_SOUND_TOKEN environment variable'
        sys.exit(2)

    max_artists = DEFAULT_MAX_ARTISTS

    if len(argv) >= 1:
        try:
            max_artists = int(argv[0])
        except ValueError:
            pass

    print('Generating {} artist ids'.format(max_artists))

    start_time = time.time()

    count_artist = 0
    artist_without_images = 0
    artist_without_genres = 0
    artist_without_social_media_links = 0

    for artist_id in xrange(1, max_artists + 1):
        artist = get_artist(id=artist_id)

        if artist:
            count_artist += 1
            print('Artist {0}: {1} \n'.format(artist_id, artist))

            if not artist['images']:
                artist_without_images += 1

            if not artist['genres']:
                artist_without_genres += 1

            if not artist['social_media_links']:
                artist_without_social_media_links += 1

    elapsed_time = time.time() - start_time

    print('Elapsed time: {}'.format(hms_string(elapsed_time)))
    print('Artists Parsed: {} from {}'.format(count_artist, max_artists))
    print('Artists without images: {} from {}'.format(artist_without_images, max_artists))
    print('Artists without genres: {} from {}'.format(artist_without_genres, max_artists))
    print('Artists without social_media_links: {} from {}'.format(artist_without_social_media_links, max_artists))

if __name__ == '__main__':
   main(sys.argv[1:])
