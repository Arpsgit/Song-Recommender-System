import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=st.secrets['client_id'], client_secret=st.secrets['client_secret']))


st.header('Song Recommender System')
song_df = pickle.load(open('song_df.pkl', 'rb'))
song_df = pd.DataFrame(song_df)
song_feat_scaled = pickle.load(open('song_feat_scaled.pkl', 'rb'))

song_list = song_df['name'].values
selected_song = st.selectbox("Type or select a Song from the dropdown", song_list)


def song_recommend(song):
    similar_song_names = []
    song_index = song_df[song_df['name'] == song].index[0]
    a = euclidean_distances([song_feat_scaled[song_index]], np.delete(song_feat_scaled, song_index, axis=0))[0]
    similar_songs = sorted(enumerate(a), key=lambda x: x[1])[1:6]
    for s in similar_songs:
        similar_song_names.append(song_df.iloc[s[0]]['name'])
    return similar_song_names


if st.button('Show Recommendations'):
    similar_song = song_recommend(selected_song)
    img_url = spotify.search(q=f'track:{selected_song}', type='track')['tracks']['items'][0]['album']['images'][1]['url']
    st.subheader(selected_song)
    try:
        st.image(img_url)
        prv = spotify.search(q=f'track:{selected_song}', type='track')['tracks']['items'][0]['preview_url']
        st.audio(prv, format="audio/wav", start_time=0, sample_rate=None)
    except:
        tr_id = song_df[song_df['name'] == selected_song]['id'].values[0]
        st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])
    st.subheader('Recommended Songs...')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['recommendation:1', 'recommendation:2', 'recommendation:3', 'recommendation:4', 'recommendation:5'])
    with tab1:
        try:
            st.subheader(similar_song[0])
            st.image(spotify.search(q=f'track:{similar_song[0]}', type='track')['tracks']['items'][0]['album']['images'][1]['url'])
            prv1 = spotify.search(q=f'track:{similar_song[0]}', type='track')['tracks']['items'][0]['preview_url']
            st.audio(prv1, format="audio/wav", start_time=0, sample_rate=None)
        except:
            tr_id = song_df[song_df['name'] == similar_song[0]]['id'].values[0]
            st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])
    with tab2:
        try:
            st.subheader(similar_song[1])
            st.image(spotify.search(q=f'track:{similar_song[1]}', type='track')['tracks']['items'][0]['album']['images'][1]['url'])
            prv2 = spotify.search(q=f'track:{similar_song[1]}', type='track')['tracks']['items'][0]['preview_url']
            st.audio(prv2, format="audio/wav", start_time=0, sample_rate=None)
        except:
            tr_id = song_df[song_df['name'] == similar_song[1]]['id'].values[0]
            st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])

    with tab3:
        try:
            st.subheader(similar_song[2])
            st.image(spotify.search(q=f'track:{similar_song[2]}', type='track')['tracks']['items'][0]['album']['images'][1]['url'])
            prv3 = spotify.search(q=f'track:{similar_song[2]}', type='track')['tracks']['items'][0]['preview_url']
            st.audio(prv3, format="audio/wav", start_time=0, sample_rate=None)
        except:
            tr_id = song_df[song_df['name'] == similar_song[2]]['id'].values[0]
            st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])
    with tab4:
        try:
            st.subheader(similar_song[3])
            st.image(spotify.search(q=f'track:{similar_song[3]}', type='track')['tracks']['items'][0]['album']['images'][1]['url'])
            prv4 = spotify.search(q=f'track:{similar_song[3]}', type='track')['tracks']['items'][0]['preview_url']
            st.audio(prv4, format="audio/wav", start_time=0, sample_rate=None)
        except:
            tr_id = song_df[song_df['name'] == similar_song[3]]['id'].values[0]
            st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])
    with tab5:
        try:
            st.subheader(similar_song[4])
            st.image(spotify.search(q=f'track:{similar_song[4]}', type='track')['tracks']['items'][0]['album']['images'][1]['url'])
            prv5 = spotify.search(q=f'track:{similar_song[4]}', type='track')['tracks']['items'][0]['preview_url']
            st.audio(prv5, format="audio/wav", start_time=0, sample_rate=None)
        except:
            tr_id = song_df[song_df['name'] == similar_song[4]]['id'].values[0]
            st.image(spotify.track(track_id=tr_id)['album']['images'][1]['url'])