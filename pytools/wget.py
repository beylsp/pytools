"""
A lightweight network downloader.
"""
import urllib2
import urlparse
import os
import logging
from pytools.cli import query_yes_no

__all__ = ['download']

_LOGGER = logging.getLogger(__name__)

def download(url, destination=None):
    """
    Download resource to destination.

    @param url: http resource location.
    @type url: C{string}.
    @param destination: path where resource is saved (default=current dir).
    @type destination: C{string}.
    @raise Exception
    """
    if not destination:
        destination = os.getcwd()
    try:
        resource = urllib2.urlopen(url)
        url = urlparse.urlparse(resource.geturl())
        _file = os.path.basename(url.path)
        full_path = os.path.join(destination, _file)
        answer = ""
        if os.path.exists(full_path):
            answer = query_yes_no(
             "Do you want to download and overwrite {0}? ".format(_file), "no")
        if answer == "yes" or not os.path.exists(full_path):
            _LOGGER.info(msg="Downloading %s from %s" % (_file, url.netloc))
            with open(full_path, 'w') as _file:
                chunk_read(resource, _file, 8192)
    except Exception as err:
        raise err
    except KeyboardInterrupt:
        pass

def chunk_read(response, _file, chunk_size):
    """reads chunk_size from response and reports progress if needed."""
    total_size = int(response.info().getheader('Content-Length').strip())
    bytes_so_far = 0
    while 1:
        chunk = response.read(chunk_size)
        _file.write(chunk)
        bytes_so_far += len(chunk)
        if not chunk:
            break
        if _LOGGER.isEnabledFor(logging.DEBUG):
            percent = float(bytes_so_far) / total_size
            percent = round(percent*100, 2)
            _LOGGER.debug(msg="Downloaded %0.2f of %0.2f MiB (%0.2f%%)\r" %
                  (float(bytes_so_far)/1048576, float(total_size)/1048576,
                   percent))
    return bytes_so_far

