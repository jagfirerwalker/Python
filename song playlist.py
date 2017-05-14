songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] 
max_size = 12.2
#['Roar','Wannabe','Timber']

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    
    check if first song can fit
        add it or return empty list
    next smallest song that hasn't been picked
    """
   
    songlist = []
    totalSize = 0

    if songs[0][2] > max_size:
        return songlist
    songlist.append(songs[0][0])
    totalSize += songs[0][2]
    del songs[0]

    while len(songs) > 0:
        smallestSong = min(songs, key = lambda t: t[2])

        smallestSize = smallestSong[2]
        smallestName = smallestSong[0] 
        
        if totalSize + smallestSize <= max_size:
            songlist.append(smallestName)
            totalSize += smallestSize 
        songs.remove(smallestSong)
        
    return songlist
    
print(song_playlist(songs, max_size))