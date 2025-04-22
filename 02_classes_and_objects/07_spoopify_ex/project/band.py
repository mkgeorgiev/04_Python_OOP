from project.song import Song
from project.album import Album

class Band:
    def __init__(self, name:str):
        self.name = name
        self.albums = []

    def add_album(self, album:Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album_in_band in self.albums:
            if album_in_band.name == album_name:
                if album_in_band.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album_in_band)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        if self.albums:
            result += "\n".join([album.details() for album in self.albums])
            result += "\n"
        return result


