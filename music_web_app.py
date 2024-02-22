import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
music_web_app = Flask(__name__)

# @music_web_app.route('/albums', methods=['POST'])
# def add_album():
#     title = request.form('title')
#     release_year = request.form('release_year')
#     artist_id = request.form('artist_id')
#     return f'album title: {title}, release year: {release_year}, artist id: {artist_id}'

@music_web_app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(music_web_app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create(album)
    return "Album added successfully"


@music_web_app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(music_web_app)
    repository = AlbumRepository(connection)
    return "\n".join([
        str(album) for album in repository.all()
    ])









# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    music_web_app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
