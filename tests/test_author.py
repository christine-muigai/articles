from lib.models.author import Author

def test_author_initialization():
    author = Author(id=1, name="Alice")  
    assert author.id == 1
    assert author.name == "Alice"
