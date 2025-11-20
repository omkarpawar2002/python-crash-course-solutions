'''
8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
loop that allows users to enter an album’s artist and title . Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created . Be sure to include a quit value in the while loop 
'''

def make_album(artist_name,album_title):
    music_album = {}
    music_album['Artist_Name'] = artist_name
    music_album['Album_Title'] = album_title
    return music_album

while True:
    artist_name = input("Enter artist Name :- ")
    if(artist_name == 'q'):
        break
    album_title = input("Enter Album Title :- ")
    if(album_title == 'q'):
        break
    first = make_album(artist_name=artist_name,album_title=album_title)
    print(first)