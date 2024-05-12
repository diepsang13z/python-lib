# Read data from CSV file

# The table has one row for each album and several columns.

# artist: Name of the artist
# album: Name of the album
# released_year: Year the album was released
# length_min_sec: Length of the album (hours,minutes,seconds)
# genre: Genre of the album
# music_recording_sales_millions: Music recording sales (millions in USD) on [SONG://DATABASE]
# claimed_sales_millions: Album's claimed sales (millions in USD) on [SONG://DATABASE]
# date_released: Date on which the album was released
# soundtrack: Indicates if the album is the movie soundtrack (Y) or (N)
# rating_of_friends: Indicates the rating from your friends from 1 to 10

# Install dependencies: pandas, xlrd, openpyxl

import requests
import pandas as pd


xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'


def download_file(url, filename):
    '''Dowload file to local disk

    Args:
        url (_type_): remote file url
        filename (_type_): local file name
    '''
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


async def main():
    df = pd.read_excel(xlsx_path)
    print(df.head())

    # Get the column as a dataframe
    print(df[['Length']])
    print(df[['Artist', 'Length', 'Genre']])

    # Get the column as a series
    print(df['Artist'])

    # Access columns
    print(df.iloc[0, 2])
    print(df.loc[0, 'Released'])

    # Slicing the dataframe using index [start:end]: start -> end - 1
    print(df.iloc[0:2, 0:3])

    # Slicing the dataframe using name
    print(df.loc[0:2, 'Artist':'Released'])


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
