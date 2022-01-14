from typing                         import List, Union
from deezer                         import Client as dzClient, Artist

from src.providers.MusicProvider    import MusicProvider
from src.endpoints.Deezer           import ENDPOINTS
from src.requests.Network           import Network
from src.artist.RBArtist            import RBArtist


class Deezer( MusicProvider ):
    __client                        : dzClient

    def __init__( self , * , network : Network ) -> None:
        self.__client               = dzClient()
        super().__init__(
            name            = 'Deezer',
            endpoints       = ENDPOINTS,
            network         = network
        )

    def search_artist( self , artist_name : str ) -> Union[ RBArtist , None ] :
        artists         : List[Artist]  = self.__client.search_artists( query=artist_name , strict=True , limit=1 )
        artist          : Artist        = artists[0] if artists is not None and len(artists) == 1 else None
        rb_artist       : RBArtist      = RBArtist.from_deezer_artist( artist )
        return rb_artist