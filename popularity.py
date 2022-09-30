import pandas as pd

# iterate through the file outside of the functions
# so it has global scope
songs = pd.read_csv("./TikTok_songs_2022.csv")

# Main function that will automatically run.

def main():
    top5_artists = top_artists()
    top5_tracks = top_tracks()
    # First find the top 5 artists in the dataset
    print("What are the top 5 artists?")
    print(f"1. {top5_artists[0]}")
    print(f"2. {top5_artists[1]}")
    print(f"3. {top5_artists[2]}")
    print(f"4. {top5_artists[3]}")
    print(f"5. {top5_artists[4]}")
    print()
    # Then the top 5 tracks in the dataset
    print("What are the top 5 tracks?")
    print(f"1. {top5_tracks[0]}")
    print(f"2. {top5_tracks[1]}")
    print(f"3. {top5_tracks[2]}")
    print(f"4. {top5_tracks[3]}")
    print(f"5. {top5_tracks[4]}")
    print()
    # My 2nd question was what is the average valence/positivity of the track?
    print("Valence describes the musical positiveness of a track. \nTracks with high valence sound more positive, cheerful, or euphoric. \nTracks with low valence sound more negative, sad, or angry. ")
    print("What is the average valence for the top 100 most popular TikTok songs?")
    print(round(valence_mean(), 2))
    print()

    # Gives user a list of columns to choose from
    # --only flaw is that some of the columns are strings and will
    # not work with the .corr() method.
    # Get two columns from user, find correlation between the two.
    print("Here is a list of all 18 columns.")
    for col in songs.columns:
        print(col)
    print("Find the correlation between 2 columns: ")
    col1 = input("1st column: ")
    col2 = input("2nd column: ")
    col_corr = correlation(col1, col2)
    print(col_corr)

# FUNCTIONS 

def valence_mean():
    # Finds the average of the column "valence"
    valenceMean = songs["valence"].mean()
    return valenceMean

def top_artists():
    # Finds the top 5 artists through the .sort_values() method
    top_artists = songs[["artist_name", "artist_pop"]].sort_values('artist_pop', ascending=False)
    top_artists = top_artists.artist_name.unique()[:5]
    return top_artists

def top_tracks():
    # Finds the top 5 tracks through the .sort_values() method
    top_tracks = songs[["track_name", "track_pop"]].sort_values('track_pop', ascending=False)
    top_tracks = top_tracks.track_name.unique()[:5]
    return top_tracks

def correlation(col1, col2):

    # Built in pandas correlation method.
    # If the correlation is between 1 and .6 or -1 and -0.6,
    # it is considered good correlation.
    # If the correlation is between -0.2 and 0.2,
    # it is considered bad correlation, if one number changes
        # it most likely will not affect the other.

    # check to see if both col inputs are actually columns
    corr = songs[f'{col1}'].corr(songs[f'{col2}'])
    correlation = round(corr, 2)
    if (correlation >= -1 and correlation <= -0.6):
        return f'{col1} and {col2} have a good correlation: {correlation}.\n If {col1} goes up, {col2} will most likely go down.'
    elif (correlation >= 0.6 and correlation <= 1):
        return f'{col1} and {col2} have a good correlation: {correlation}.\n If {col1} goes up, {col2} will most likely go up as well.'
    elif (correlation > -0.6 and correlation <= -0.2):
        return f'{col1} and {col2} have a correlation of {correlation}. \n If {col1} goes up, {col2} may go down.'
    elif (correlation >= 0.2 and correlation < 0.6):
        return f'{col1} and {col2} have a correlation of {correlation}. \n If {col1} goes up, {col2} may go up as well.'
    elif (correlation > -0.2 and correlation < 0.2):
        return f'{col1} and {col2} have a bad correlation: {correlation}. \n There is little to no relationship between {col1} and {col2}.'
    else:
        return 'Error, value not accounted for.'

    
# This portion makes it so the main function 
# automatically runs when the program runs.

if __name__ == "__main__":
    main()
