from typing                     import Any, List
from deezer                     import Artist, Album

from src.providers.utils        import get_object_field

class RBAlbum:
    __id                        : str
    @property
    def albumID( self ) -> str         : return self.__id

    __name                      : str
    @property
    def name( self ) -> str             : return self.__name


    def __init__(
        self , * ,
        albumID                 : str,
        albumName               : str
    ) -> None  :
        self.__id           = albumID
        self.__name         = albumName

    def __str__(self) -> str:
        return f'<RBAlbum ({self.albumID}) "{self.name}">' 
    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_deezer_album( cls , album : Any ):
        if album is None: return None
        return cls(
            albumID     = get_object_field( album , 'id' ),
            albumName   = get_object_field( album , 'title' )
        )

    @classmethod
    def from_spotify_album( cls , album : Any ):
        if album is None: return None
        return cls(
            albumID     = get_object_field( album , 'id' ),
            albumName   = get_object_field( album , 'name' )
        )