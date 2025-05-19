
import pandas as pd
import re

def clean_query(response):
    start_index = response.find('[\INST]') + len('[\INST]')
    response_text = response[start_index:]

    return response_text



def separate_artists(artist_str):
    # Define separators (extend this list as needed)
    separators = ['Featuring', 'Feat', 'With', '&', ',', ' x ']
    pattern = '|'.join(map(re.escape, separators))  # Create regex pattern to match any separator

    # Split artist_str by the pattern and strip whitespace from each artist name
    artists = [artist.strip() for artist in re.split(pattern, artist_str)]
    return artists

