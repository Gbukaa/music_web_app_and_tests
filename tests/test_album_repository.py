from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/albums_table.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, 'Imagine', 1978, 1),
        Album(2, 'Thriller', 1982, 2),
        Album(3, 'Dark Side of the Moon', 1973, 3),
        Album(4, 'Abbey Road', 1969, 4),
        Album(5, "Sgt. Pepper's Lonely Hearts Club Band", 1967, 5),
        Album(6, 'Hotel California', 1976, 6),
        Album(7, 'The Wall', 1979, 7),
        Album(8, 'Back in Black', 1980, 8),
        Album(9, 'Led Zeppelin IV', 1971, 9),
        Album(10, 'Rumours', 1977, 10),
        Album(11, 'Cotton Eyed Joe', 1994, 11)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(2)
    assert album == Album(2, 'Thriller', 1982, 2)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Master of Puppets", "1986", "12"))

    result = repository.all()
    assert result == [
        Album(1, 'Imagine', 1978, 1),
        Album(2, 'Thriller', 1982, 2),
        Album(3, 'Dark Side of the Moon', 1973, 3),
        Album(4, 'Abbey Road', 1969, 4),
        Album(5, "Sgt. Pepper's Lonely Hearts Club Band", 1967, 5),
        Album(6, 'Hotel California', 1976, 6),
        Album(7, 'The Wall', 1979, 7),
        Album(8, 'Back in Black', 1980, 8),
        Album(9, 'Led Zeppelin IV', 1971, 9),
        Album(10, 'Rumours', 1977, 10),
        Album(11, 'Cotton Eyed Joe', 1994, 11),
        Album(12, 'Master of Puppets', 1986, 12)
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(2) 

    result = repository.all()
    assert result == [
        Album(1, 'Imagine', 1978, 1),
        Album(3, 'Dark Side of the Moon', 1973, 3),
        Album(4, 'Abbey Road', 1969, 4),
        Album(5, "Sgt. Pepper's Lonely Hearts Club Band", 1967, 5),
        Album(6, 'Hotel California', 1976, 6),
        Album(7, 'The Wall', 1979, 7),
        Album(8, 'Back in Black', 1980, 8),
        Album(9, 'Led Zeppelin IV', 1971, 9),
        Album(10, 'Rumours', 1977, 10),
        Album(11, 'Cotton Eyed Joe', 1994, 11)
    ]