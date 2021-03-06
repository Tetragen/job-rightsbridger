from asyncio import base_tasks
from typing                         import List, Union
from deezer                         import Client as dzClient, Artist

from src.providers.MusicProvider    import MusicProvider
from src.endpoints.Deezer           import ENDPOINTS
from src.requests.Network           import Network
from src.entities.RBArtist          import RBArtist


class Deezer( MusicProvider ):
    __client                        : dzClient

    def __init__( self , * , network : Network , config : dict ) -> None:
        self.__client               = dzClient()
        super().__init__(
            name            = 'Deezer',
            endpoints       = ENDPOINTS,
            network         = network
        )

    def search_artist( self , artist_name : str ) -> Union[ RBArtist , None ] :
        artists         : List[Artist]  = self.__client.search_artists( query=artist_name )
        if artists is None:
            return None
        nb_artists  : int = artists.__getattribute__('total')
        if nb_artists is None or nb_artists == 0:
            return None
        artist          : Artist        = artists[0]
        rb_artist       : RBArtist      = RBArtist.from_deezer_artist( artist )
        return rb_artist