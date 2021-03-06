#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

DB_PATH = path.join(path.dirname(path.dirname(
    path.abspath(__file__))), "data/db.sqlite3")

ALBUM_FIELDS = [
    ("album_id", "INTEGER PRIMARY KEY"),
    ("album", "TEXT"),
    ("artist", "TEXT"),
]

REVIEW_FIELDS = [
    ("album_id", "INTEGER PRIMARY KEY"),
    ("time", "TIMESTAMP"),
    ("allmusic", "REAL"),
    ("metacritic", "REAL"),
    ("pitchfork", "REAL"),
    ("score_mean", "REAL"),
    ("score_std", "REAL"),
    ("reviewers", "TEXT"),
]


GENRE_FIELDS = [
    ("album_id", "INTEGER PRIMARY KEY"),
    ("country", "INTEGER"),
    ("classical", "INTEGER"),
    ("electronic", "INTEGER"),
    ("experimental", "INTEGER"),
    ("folk", "INTEGER"),
    ("hiphop", "INTEGER"),
    ("international", "INTEGER"),
    ("jazz", "INTEGER"),
    ("metal", "INTEGER"),
    ("pop", "INTEGER"),
    ("rock", "INTEGER"),
]

FEATURE_FIELDS = [
    ("album_id", "INTEGER PRIMARY KEY"),
    ("explicit", "REAL"),
    ("tracks_count", "REAL"),
    ("duration_mean", "REAL"),
    ("duration_med", "REAL"),
    ("duration_min", "REAL"),
    ("duration_max", "REAL"),
    ("danceability_mean", "REAL"),
    ("danceability_med", "REAL"),
    ("danceability_min", "REAL"),
    ("danceability_max", "REAL"),
    ("energy_mean", "REAL"),
    ("energy_med", "REAL"),
    ("energy_min", "REAL"),
    ("energy_max", "REAL"),
    ("key_mean", "REAL"),
    ("key_med", "REAL"),
    ("key_min", "REAL"),
    ("key_max", "REAL"),
    ("loudness_mean", "REAL"),
    ("loudness_med", "REAL"),
    ("loudness_min", "REAL"),
    ("loudness_max", "REAL"),
    ("mode_mean", "REAL"),
    ("mode_med", "REAL"),
    ("speechiness_mean", "REAL"),
    ("speechiness_med", "REAL"),
    ("speechiness_min", "REAL"),
    ("speechiness_max", "REAL"),
    ("acousticness_mean", "REAL"),
    ("acousticness_med", "REAL"),
    ("acousticness_min", "REAL"),
    ("acousticness_max", "REAL"),
    ("instrumentalness_mean", "REAL"),
    ("instrumentalness_med", "REAL"),
    ("instrumentalness_min", "REAL"),
    ("instrumentalness_max", "REAL"),
    ("liveness_mean", "REAL"),
    ("liveness_med", "REAL"),
    ("liveness_min", "REAL"),
    ("liveness_max", "REAL"),
    ("valence_mean", "REAL"),
    ("valence_med", "REAL"),
    ("valence_min", "REAL"),
    ("valence_max", "REAL"),
    ("tempo_mean", "REAL"),
    ("tempo_med", "REAL"),
    ("tempo_min", "REAL"),
    ("tempo_max", "REAL"),
    ("time_signature_mean", "REAL"),
    ("time_signature_med", "REAL"),
    ("time_signature_min", "REAL"),
    ("time_signature_max", "REAL"),
]

IND_REVIEW_FIELDS = [
    ("album_id", "INTEGER PRIMARY KEY"),
    ("album", "TEXT"),
    ("artist", "TEXT"),
    ("time", "TIMESTAMP"),
    ("genre", "TEXT"),
    ("score", "REAL"),
    ("reviewer", "TEXT"),
]
