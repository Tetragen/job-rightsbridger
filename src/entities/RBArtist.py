from typing                     import Any, List
from deezer                     import Artist, Album

from src.providers.utils        import get_object_field
from src.entities.RBAlbum       import RBAlbum


class RBArtist:
    __id                        : str
    @property
    def artistID( self ) -> str         : return self.__id

    __provider                  : str
    @property
    def artistProvider( self ) -> str   : return self.__provider

    __name                      : str
    @property
    def name( self ) -> str             : return self.__name

    @property
    def nb_albums( self ) -> int        : return len( self.__albums )

    __albums                    : List[RBAlbum]
    @property
    def albums( self ) -> List[RBAlbum] : return self.__albums

    __followers                 : int
    @property
    def followers( self ) -> int        : return self.__followers


    def __init__(
        self , * ,
        artistProvider          : str,
        artistID                : str,
        artistName              : str,
        albums                  : List[RBAlbum],
        followers               : int
    ) -> None :
        self.__id           = artistID
        self.__provider     = artistProvider
        self.__name         = artistName
        self.__albums       = albums
        self.__followers    = followers

    def __str__(self) -> str:
        return f'<["{self.name}" @ {self.artistProvider}] ("{self.artistID}") F={self.followers} NB_ALBUMS={len( self.albums )}>' 
    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_deezer_artist( cls , artist : Artist ):
        if artist is None: return None
        albums  : List[ Album ] = artist.get_albums()
        return cls(
            artistProvider      = 'Deezer',
            artistID            = str( artist.id ),
            artistName          = artist.name,
            albums              = [ RBAlbum.from_deezer_album( album ) for album in albums ],
            followers           = artist.nb_fan
        )

    @classmethod
    def from_spotify_artist( cls , * , artist : Any , albums : Any ):
        if artist is None or albums is None: return None
        return cls(
            artistProvider      = 'Spotify',
            artistID            = get_object_field( artist , 'id' ),
            artistName          = get_object_field( artist , 'name' ),
            albums              = [ RBAlbum.from_spotify_album( album ) for album in albums ],
            followers           = get_object_field( artist , 'followers.total' )
        )