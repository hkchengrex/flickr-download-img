# Flickr image downloader

This script is initially used for downloading images of Colosseum from the ROME16K dataset. I have extracted image ids for cluster 4.4.0.0 and have successfully reconstructed the Colosseum with the downloaded images. It works faster than [similar project](https://github.com/ceciliavision/flickr_get_img) since it directly uses Flickr's API.

## Requirements
- Python 2.7 (Python 3 would not work, since the library below does not work with Python 3)
- [Python Flickr API](https://github.com/alexis-mignon/python-flickr-api)

## Usage:
`python crawl.py -key=[Your flickr API key] -ids=[Your list of image ids]`

Your can obtain your Flickr API key here: https://www.flickr.com/services/apps/create/apply/

