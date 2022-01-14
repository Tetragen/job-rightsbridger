from typing     import Dict
from string     import Template

ENDPOINTS   : Dict[str, str] = {
    # 'LOGIN'             : 'https://accounts.spotify.com/api/token',
    'SEARCH_ARTIST'     : 'https://api.deezer.com/search?q=artist:"${query}"&output=json',
    'SEARCH_TRACK'      : 'https://api.deezer.com/search?q=track:"${query}"&output=json',
    'SEARCH_ALBUM'      : 'https://api.deezer.com/search?q=album:"${query}"&output=json',
    'SEARCH_LABEL'      : 'https://api.deezer.com/search?q=label:"${query}"&output=json',
    'ARTIST'            : 'https://api.deezer.com/artist/${id}'
}

URLS        : Dict[str, Template] = { k : Template( endpoint ) for k,endpoint in ENDPOINTS.items() }