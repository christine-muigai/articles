from lib.models.author import Author

def test_author_name():
    author = Author(id=1, name="Alice")
    assert author.name == "Alice"
