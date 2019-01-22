import flickr_api
from flickr_api.api import flickr
import xml.etree.ElementTree
import urllib

from argparse import ArgumentParser
import functools
import multiprocessing

import os

def download_image(id, key):
    respond = flickr.photos.getInfo(api_key=key, photo_id=id)
    e = xml.etree.ElementTree.fromstring(respond)

    for atype in e.findall('photo'):
        original_secret = atype.get('originalsecret')
        farm = atype.get('farm')
        server = atype.get('server')
        original_format = atype.get('originalformat')

        if original_format is not None:
            image_name = '%s.%s' % (id, original_format)

            urllib.urlretrieve("https://farm%s.staticflickr.com/%s/%s_%s_o.%s" % (
                farm, server, id, original_secret, original_format
            ), 'result/' + image_name)

            print 'Got image: ', image_name
        else:
            print 'Image %s does not want to be downloaded' % id

if not os.path.exists('result'):
    os.makedirs('result')

parser = ArgumentParser()
parser.add_argument('-n', '--num_threads', default=16)
parser.add_argument('-key', type=str)
parser.add_argument('-ids', type=str)

args = parser.parse_args()

lines = open(args.ids).read().split('\n')
print 'Number of images:', len(lines)

pool = multiprocessing.Pool(args.num_threads)
pool.map(functools.partial(download_image, key=args.key), lines)

