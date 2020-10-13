# -*- coding: utf-8 -*-

# Demo Code Sample for Su
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import json
import pandas as pd
from pprint import pprint
from youtube_api import YouTubeDataAPI


def main():
    api_key = 'AIzaSyAC9cPtTvTp6tauWvDEgPVIAas4IGPoC5M'
    yt = YouTubeDataAPI(api_key)

    # searches for video, topic_ids: https://developers.google.com/youtube/v3/docs/search/list#
    searches = find_video('news', '/m/05qt0', yt)

    # gets meta data of video including description
    # video_meta = get_meta(search, yt)

    # recomended = get_recommendations(search, yt)

    df_searches = pd.DataFrame(searches, index=[1])
    df_searches.head(5)


def find_video(query, topic, yt):
    """Takes in query and returns one result"""

    response = yt.search(q=query, max_results=5, topic_id=topic)

    print("-----------------SEARCH-----------------")
    pprint(response)

    return response[0]


def get_meta(video, yt):
    """Gets the full meta data associated with video param"""
    _id = video['video_id']
    response = yt.get_video_metadata(_id)

    print("-----------------META-----------------")
    pprint(response)

    return response


def get_recommendations(video, yt):
    """Takes youtube video and returns list of recommendations"""
    _id = video['video_id']
    response = yt.get_recommended_videos(_id, max_results=1)

    print("-------------RECOMMENDATIONS-------------")
    pprint(response)

    return response


if __name__ == "__main__":
    main()


# @misc{leon_yin_2018_1414418,
#   author       = {Leon Yin and
#                   Megan Brown},
#   title        = {SMAPPNYU/youtube-data-api},
#   month        = sep,
#   year         = 2018,
#   doi          = {10.5281/zenodo.1414418},
#   url          = {https://doi.org/10.5281/zenodo.1414418}
# }
