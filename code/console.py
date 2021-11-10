import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# ARTIST CRUD testing - 

# Create and Save
artist_1 = Artist('Ed Sheeran')
artist_repository.save(artist_1)

artist_2 = Artist('Eminem')
artist_repository.save(artist_2)

#  READ ALL
artists = artist_repository.select_all()
for artist in artists:
        print(artist.__dict__)
# READ INDIVIDUAL
myArtist = artist_repository.select(1)
print(myArtist.__dict__)

# UPDATE
artist_2.name = "Slim Shady"
artist_repository.update(artist_2)

# Delete all
artist_repository.delete_all()

# DELETE Individual
artist_repository.delete(1)







#  ALBUM CRUD testing

# CREATE two albums for the Albums table and saving
album_1 = Album("Equals", artist_1, "Pop")
album_repository.save(album_1)
album_2 = Album("Divide", artist_1, "Pop")
album_repository.save(album_2)

# READ all
albums = album_repository.select_all()
for album in albums:
        print(album.__dict__)
# READ Individual
myAlbum = album_repository.select(2)
print(myAlbum.__dict__)

# UPDATE the first albums genre to rock
album_1.genre = "Rock"
album_repository.update(album_1)

# DELETE all
album_repository.delete_all()

# DELETE individual
album_repository.delete(2)


album_list_from_artist = artist_repository.albums(artist_1)
for artist in album_list_from_artist:
        print(artist.__dict__)

        
pdb.set_trace()