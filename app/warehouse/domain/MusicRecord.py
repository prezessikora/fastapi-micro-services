class MusicRecord:
    def __init__(self, id, title, artist, stock, location):
        self.id = id
        self.title = title
        self.artist = artist
        self.stock = stock
        self.location = location

    def __repr__(self):
        return f'MusicRecord: {self.title} by {self.artist}'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'stock': self.stock,
            'location': self.location,
        }