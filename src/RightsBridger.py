from typing                             import List, Any

from src.entities.RBArtist              import RBArtist
from src.requests.Network               import Network
from src.providers.Deezer               import Deezer
from src.providers.Spotify              import Spotify
from src.providers.MusicProvider        import MusicProvider


class RightsBridger:
    __network                   : Network
    __providers                 : List[ MusicProvider ]

    def __init__( self , * , config : dict ) -> None:
        self.__network          = Network()
        self.__providers        = [
            Deezer( network = self.__network , config = config ),
            Spotify( network = self.__network , config = config )
        ]

    def search_artist( self , artist_name : str ) -> List[ RBArtist ]:
        results : List[RBArtist] = []
        for provider in self.__providers:
            artist = provider.search_artist( artist_name )
            if artist is not None:
                results.append( artist )
        return results
