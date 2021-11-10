from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

# CREATE
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

# READ INDIVIDUAL
def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])

    return artist

# READ ALL
def select_all(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], artist, row['genre'], row['id'] )
        albums.append(album)
    return albums

# UPDATE
def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id] 
    run_sql(sql, values)

# DELETE ALL
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# DELETE Individual
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values =[id]
    run_sql(sql, values)


# function to return all albums for a selected artist
def albums(artist):

    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums