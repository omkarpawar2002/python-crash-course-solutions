'''

 8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album . The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information . Use the function to make three dictionaries representing different 
albums . Print each return value to show that the dictionaries are storing the 
album information correctly .
 Add an optional parameter to make_album() that allows you to store the 
number of tracks on an album . If the calling line includes a value for the num
ber of tracks, add that value to the album’s dictionary . Make at least one new 
function call that includes the number of tracks on an album 

'''

def make_album(artist_name,album_title,tracks=''):
    music_album = {}
    music_album['Artist_Name'] = artist_name
    music_album['Album_Title'] = album_title
    if(tracks):
        music_album['tracks'] = tracks
    return music_album

first = make_album('raju','suno na sang marmar')
print(first)
second = make_album('arjit','tum hi ho')
print(second)
third = make_album('rfak','khuda gava')
print(third)
fourth = make_album('nfak','jara jara',44)
print(fourth)