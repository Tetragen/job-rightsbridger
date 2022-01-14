from typing     import Dict
from string     import Template

ENDPOINTS   : Dict[str, str] = {
    'LOGIN'             : 'https://accounts.spotify.com/api/token',
    'SEARCH_ARTIST'     : 'https://api.spotify.com/v1/search?q=${query}&type=artist&limit=1',
    'SEARCH_TRACK'      : 'https://api.spotify.com/v1/search?q=${query}&type=track',
    'ARTIST'            : 'https://api.spotify.com/v1/artists/${id}',
    'ALBUMS'            : 'https://api.spotify.com/v1/artists/${id}/albums'
}

URLS        : Dict[str, Template] = { k : Template( endpoint ) for k,endpoint in ENDPOINTS.items() }