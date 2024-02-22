from lib.album import Album

"""
Album constructs with an id, title, release_year, artist_id
"""
def test_book_constructs():
    album = Album(1, "Imagine", "1978", 1)
    assert album.id == 1
    assert album.title == "Imagine"
    assert album.release_year == "1978"
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Imagine", "1978", 1)
    assert str(album) == "Album(1, Imagine, 1978, 1)"


"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Imagine", "1978", 1)
    album2 = Album(1, "Imagine", "1978", 1)
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.
