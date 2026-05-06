import json
import urllib.request


def hent_json(url, headers=None):
    """
    Henter JSON fra en URL og returnerer Python-data.
    Bruker bare Python standardbibliotek.
    """
    if headers is None:
        headers = {}

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        statuskode = response.status
        innhold = response.read().decode("utf-8")

    data = json.loads(innhold)
    return statuskode, data
