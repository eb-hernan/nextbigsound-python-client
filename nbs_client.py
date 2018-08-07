import os

import requests

user_token = os.environ.get('NEXT_BIG_SOUND_TOKEN')

def get_artists(max_chart_releases = 5, max_chart_appearances = 5, logging = False):

    count_chart_releases = 0
    count_chart_appearances = 0
    count_artist = 0

    # Get charts https://api.nextbigsound.com/charts/?accessToken=

    req = requests.get('https://api.nextbigsound.com/charts/?accessToken={0}'.format(user_token))

    charts = req.json()['items']

    for chart in charts:
        if logging:
            print('Chart: {0} \n'.format(chart))

        # Get chart https://api.nextbigsound.com/charts/1/?accessToken=
        req = requests.get(chart['self']['url'])

        releases_url = req.json()['releases']['self']['url']

        # Get releases https://api.nextbigsound.com/charts/1/releases/?accessToken=
        req = requests.get(releases_url)

        releases = req.json()['items']

        count_chart_releases = 0

        for release in releases:
            if count_chart_releases >= max_chart_releases:
                break

            count_chart_releases += 1
            release_url = release['self']['url']
            if logging:
                print('Release: {0} \n'.format(release_url))

            # Get release https://api.nextbigsound.com/charts/1/releases/2018-08-03/?accessToken=
            req = requests.get(release_url)

            appearances_url = req.json()['appearances']['self']['url']

            # Get appearances https://api.nextbigsound.com/charts/1/releases/2018-08-03/appearances/?accessToken=
            req = requests.get(appearances_url)

            appearances = req.json()['items']

            count_chart_appearances = 0

            for appearance in appearances:
                if count_chart_appearances >= max_chart_appearances:
                    break

                count_chart_appearances += 1
                appearance_url = appearance['self']['url']
                if logging:
                    print('Appearance URL: {0} \n'.format(appearance_url))

                # Get appearance https://api.nextbigsound.com/charts/1/releases/2018-08-03/appearances/1/?accessToken=
                req = requests.get(appearance_url)

                try:
                    artist = req.json().get('artist')

                    if not artist:
                        continue

                    # Get artist https://api.nextbigsound.com/artists/1300829/?accessToken=
                    req = requests.get(artist['self']['url'])

                    artist_json = req.json()

                    artist = {
                        'id': artist_json['id'],
                        'name': artist_json['name'],
                        'genres': artist_json['genres'],
                        'images': artist_json['images'],
                        'social_media_links': artist_json['endpointUrls'],
                    }
                except KeyError:
                    print('ERROR Appearance: {0}'.format(req.json()))

                yield artist

def get_artist(id):
    artist_url = 'https://api.nextbigsound.com/artists/{0}/?accessToken={1}'.format(id, user_token)

    # Get artist https://api.nextbigsound.com/artists/1300829/?accessToken=
    print('Requesting Artist URL: {0} \n'.format(artist_url))

    req = requests.get(artist_url)

    artist_json = req.json()

    if artist_json.get('errors'):
        print('Artist {0}: '.format(id) + artist_json['errors'][0]['message'])
        return None

    artist = {
        'id': artist_json['id'],
        'name': artist_json['name'],
        'genres': artist_json['genres'],
        'images': artist_json['images'],
        'social_media_links': artist_json['endpointUrls'],
    }

    return artist