from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

# CREATE
def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# READ all
def select_all():  
    albums = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['user_id'], row['id'] )
        albums.append(album)
    return albums

# READ individual
def select(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
    return album
# UPDATE
def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values =[id]
    run_sql(sql, values)