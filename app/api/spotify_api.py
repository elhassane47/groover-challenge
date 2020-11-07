import requests


class SpotifyApi:
    """
    Spotify Python Handler
    """

    SPOTIFY_URL_API = "https://api.spotify.com/v1/"

    def __init__(self, token=False):
        self._token = token
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._token}"

        }

    def set_token(self, token):
        self._token = token

    def get_new_releases(self, **params):

        """
        call new-releases endpoint of spotify api
        :param country
        :param limit:
        :param offset:
        :return:
        """
        # todo handle next
        try:
            response = self.get(
                "browse/new-releases",
                self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise

    def artists_new_relases(self):

        artists = []
        releases = self.get_new_releases()

        for item in releases['albums']['items']:
            for ar in item['artists']:
                artists.append(ar)

        return artists

    def get(self, uri, headers, **params):

        url = f"{self.SPOTIFY_URL_API}{uri}"

        return requests.get(url, headers=headers, params=params)

