import json
from authentication import authenticate
import argparse
import os
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys


class MyStreamListener(StreamListener):
    def __init__(self, outdir):
        self.outdir = outdir

    def on_data(self, data):
        try:
            if self.outdir == None:
                data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"Hollywood", '..', 'data'))
            else:
                data_path = self.outdir
            if data_path[-1] != "/":
                data_path += "/"

            filename = data_path + 'dataEthan.json'
            print("opening file: ", filename)
            with open(filename, 'a') as f:
                # Check if lang = 'en'
                tweet = json.loads(data)
                # if tweet['location'] == "hollywood":
                if tweet['lang'] == "en":
                    print(data)
                    print("\n\n\n\n")
                    f.write(data)
                return True

        except BaseException as e:
            print("Error at: %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def get_arguments():
    parser = argparse.ArgumentParser(description='Twitter Scraper')
    parser.add_argument("--outdir", type=str, nargs="*", help="Labels or hashtags used to filter tweets")
    args = parser.parse_args()
    if args.outdir:
        return args.outdir[0]
    return None


if __name__ == '__main__':
    # # agent = Scraper(sys.argv[1])
    # agent.get_tweets()
    outdir = get_arguments()
    twitter_stream = Stream(authenticate(), MyStreamListener(outdir))
    twitter_stream.sample()

