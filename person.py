# def person_detail(f_name,l_name,age='',occupation=''):
#     person = {
#         'first':f_name,
#         'last':l_name
#     }
#     if age:
#         person['age']=age
#     if occupation:
#         person['occupation']=occupation

#     return person

# get_person_detail = person_detail('rick','grimes','47')
# print(get_person_detail)


#################################################################
# def city_country(city,country):
#     location = city + ', ' + country
#     return location.title()

# while True:
#     print("\nTell us where you live")
#     print("(you can quit this anytime by entering q)\n:")

#     city = input("Your city: ")
#     if city.lower() == 'q':
#         break

#     country = input("Your country: ")
#     if country.lower() == 'q':
#         break

#     get_location = city_country(city,country)
#     print("\nYour current location is "+get_location)


###################################################################

def make_album(artist, album, number_of_tracks='0'):
    music = {
        'artist_name':artist,
        'album_name':album
    }
    if number_of_tracks:
        music['tracks'] = number_of_tracks
    else:
        music['tracks'] = '0'

    return music

while True:
    print("\nWelcome to the music library")
    print("(press q to quit anytime)")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    album = input("Album name: ")
    if album.lower() == 'q':
        break

    tracks = input("Number of tracks: ")
    if tracks.lower() == 'q':
        break

    just_made_album = make_album(artist,album,tracks)
    print("The artist is "+just_made_album['artist_name'].title() +
    " and the album which is releasing is "+just_made_album['album_name'].title() +
    " and it has "+ just_made_album['tracks'] +" tracks")


just_made_album = make_album('arjit','dont get in my way','4')
print(just_made_album)

just_made_album = make_album('zack','the way')
print(just_made_album)