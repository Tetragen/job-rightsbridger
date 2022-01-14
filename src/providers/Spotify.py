from typing                         import Union, Any

from src.artist.utils               import get_object_field
from src.artist.RBArtist            import RBArtist
from src.providers.MusicProvider    import MusicProvider
from src.endpoints.Spotify          import ENDPOINTS
from src.requests.Network           import Network


SPOTIFY_CLIENT_ID                   = '48a7d80fe3be49acba15a866ec917dd5'
SPOTIFY_CLIENT_SECRET               = '045e4e61b45f485fbb7560d0c9834bf5'


class Spotify( MusicProvider ):
    def __init__( self , * , network : Network ) -> None:
        super().__init__(
            name            = 'Spotify',
            endpoints       = ENDPOINTS,
            network         = network
        )
        spotify_connect_response = super().login_basic( username = SPOTIFY_CLIENT_ID , password = SPOTIFY_CLIENT_SECRET )
        if spotify_connect_response is not None:
            super().set_header( 'Authorization' , 'Bearer ' + spotify_connect_response['access_token'] )

    def search_artist( self , artist_name : str ) -> Union[ RBArtist , None ] :
        artists_response    : Any           = super().search_artist( artist_name )        
        artist              : Any           = get_object_field( artists_response , 'artists.items[0]' )
        artistID            : str           = get_object_field( artist , 'id' )
        albums_response     : Any           = super().albums( artistID )
        albums              : Any           = get_object_field( albums_response , 'items' )

        rb_artist           : RBArtist      = RBArtist.from_spotify_artist(
            artistID        = artistID,
            artistName      = get_object_field( artist , 'name' ),
            nb_albums       = len( albums ),
            followers       = get_object_field( artist , 'followers.total' )
        )
        return rb_artist