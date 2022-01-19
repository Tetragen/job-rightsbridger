from typing                         import Union, Any

from src.print.utils                import print_msg
from src.providers.utils            import get_object_field
from src.entities.RBArtist          import RBArtist
from src.providers.MusicProvider    import MusicProvider
from src.endpoints.Spotify          import ENDPOINTS
from src.requests.Network           import Network


# Spotify Credentials (to fill)
SPOTIFY_CLIENT_ID                   = ''
SPOTIFY_CLIENT_SECRET               = ''

class Spotify( MusicProvider ):
    def __init__( self , * , network : Network , config : dict ) -> None:
        super().__init__(
            name            = 'Spotify',
            endpoints       = ENDPOINTS,
            network         = network
        )
        spotify_connect_response = super().login_basic( username = config.get('SPOTIFY_CLIENT_ID') , password = config.get('SPOTIFY_CLIENT_SECRET') )
        if spotify_connect_response is not None:
            super().set_header( 'Authorization' , 'Bearer ' + spotify_connect_response['access_token'] )

    def search_artist( self , artist_name : str ) -> Union[ RBArtist , None ] :
        artists_response    : Any           = super().search_artist( artist_name )        
        artist              : Any           = get_object_field( artists_response , 'artists.items[0]' )
        artistID            : str           = get_object_field( artist , 'id' )
        albums_response     : Any           = super().albums( artistID )
        albums              : Any           = get_object_field( albums_response , 'items' )
        rb_artist           : RBArtist      = RBArtist.from_spotify_artist( artist=artist , albums=albums )
        return rb_artist