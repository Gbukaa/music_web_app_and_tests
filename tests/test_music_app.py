from lib.album import Album
from lib.album_repository import AlbumRepository

"""
POST /albums
"""
def test_create_album(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")

    response = web_client.post("/albums", data={'id': None, 'title': 'Voyage', 'release_year': 2022, 'artist_id': 12})

    assert response.status_code == 200

    response = web_client.get("/albums")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
    str(Album(1, 'Imagine', 1978, 1)),
    str(Album(2, 'Thriller', 1982, 2)),
    str(Album(3, 'Dark Side of the Moon', 1973, 3)),
    str(Album(4, 'Abbey Road', 1969, 4)),
    str(Album(5, "Sgt. Pepper's Lonely Hearts Club Band", 1967, 5)),
    str(Album(6, 'Hotel California', 1976, 6)),
    str(Album(7, 'The Wall', 1979, 7)),
    str(Album(8, 'Back in Black', 1980, 8)),
    str(Album(9, 'Led Zeppelin IV', 1971, 9)),
    str(Album(10, 'Rumours', 1977, 10)),
    str(Album(11, 'Cotton Eyed Joe', 1994, 11)),
    str(Album(12, 'Voyage', 2022, 12))
    ])