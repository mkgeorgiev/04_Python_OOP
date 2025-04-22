class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


with open("The Rumbling  Lyrics") as file:
    song_lyrics = file.read()


song = Music("The Rumbling", "SiM", song_lyrics)
print(song.print_info())
print(song.play())

