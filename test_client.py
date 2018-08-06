import sys
import time
import os

from utils import (
    hms_string,
)

user_token = os.environ.get('NEXT_BIG_SOUND_TOKEN')

def main(argv):

    if not user_token:
        print 'Missing NEXT_BIG_SOUND_TOKEN environment variable'
        sys.exit(2)

    start_time = time.time()

    count_artist = 0




    elapsed_time = time.time() - start_time

    print('Elapsed time: {}'.format(hms_string(elapsed_time)))
    print('Artists Parsed: {}'.format(count_artist))

if __name__ == '__main__':
   main(sys.argv[1:])
