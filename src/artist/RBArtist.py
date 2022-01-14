from typing                     import Any, List
from deezer                     import Artist, Album

from src.artist.utils           import get_object_field

class RBAlbum:
    pass


class RBArtist:
    __id                        : str
    @property
    def artistID( self ) -> str         : return self.__id

    __name                      : str
    @property
    def name( self ) -> str             : return self.__name

    __nb_albums                 : int
    @property
    def nb_albums( self ) -> int        : return self.__nb_albums

    __followers                 : int
    @property
    def followers( self ) -> int        : return self.__followers


    def __init__(
        self , * ,
        artistID                : str,
        artistName              : str,
        nb_albums               : int,
        followers               : int
    ) -> None  :
        self.__id           = artistID
        self.__name         = artistName
        self.__nb_albums    = nb_albums
        self.__followers    = followers

    def __str__(self) -> str:
        # return f'<RBArtist "{self.name}" f={self.followers}>'
        return 
    def __repr__(self) -> str:
        self.__str__()

    @classmethod
    def from_deezer_artist( cls , artist : Artist ):
        if artist is None: return None
        albums  : List[ Album ] = artist.get_albums()
        return cls(
            artistID            = str( artist.id ),
            artistName          = artist.name,
            nb_albums           = len( albums ),
            followers           = artist.nb_fan
        )

    @classmethod
    def from_spotify_artist(
        cls , * ,
        artistID        : int,
        artistName      : str,
        nb_albums       : int,
        followers       : int
    ):
        return cls(
            artistID            = artistID,
            artistName          = artistName,
            nb_albums           = nb_albums,
            followers           = followers
        )