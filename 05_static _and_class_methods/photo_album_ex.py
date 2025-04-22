from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__creating_album(pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        separator = f"{'-' * 11}"
        result = separator + "\n"
        for page in range(self.pages):
            result += ' '.join("[]" for _ in self.photos[page]) + "\n"
            result += separator + "\n"
        return result


    def __creating_album(self, pages):
        result = []
        for page in range(pages):
            result.append([])
        return result


album = PhotoAlbum(2)
album_1 = PhotoAlbum.from_photos_count(33)

print(album.add_photo("photo_1"))
print(album.add_photo("photo_2"))
print(album.add_photo("photo_3"))
print(album.add_photo("photo_4"))
print(album.add_photo("photo_5"))

print(album.display())
