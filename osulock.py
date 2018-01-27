import requests
from osuapi import OsuApi, ReqConnector
import json

api = OsuApi("f0bfd051b9e0dba2d56b96a71b416061593d7f31", connector=ReqConnector())
user = "Lilily"
scoreThreshold = 5000000000

results = api.get_user_recent( user, limit=1 )

recentScore = results[ 0 ]

beatmaps = api.get_beatmaps( beatmap_id = recentScore.beatmap_id, limit = 1 )
beatmapData = beatmaps[ 0 ]

debugMessage = "User {} ({}) got a score of {} and rank {} on beatmap {} (#{}) at {}"
print( debugMessage.format( user, recentScore.user_id, recentScore.score,
recentScore.rank, beatmapData.title, recentScore.beatmap_id, recentScore.date ) )
