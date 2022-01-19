import urllib.parse

from typing                         import Dict, Mapping, Union, Any
from string                         import Template
from base64                         import b64encode

from src.requests.HTTPMethod        import HTTPMethod
from src.requests.Network           import Network
from src.providers.MusicProviderData    import MusicProviderData


class MusicProvider:
    __name              : str
    __network           : Network
    __headers           : Dict[ str , str ]
    __endpoints         : Dict[ str , str ]


    def __init__(
        self, *,
        name            : str,
        endpoints       : Dict[ str, str ],
        network         : Network
    ) -> None:
        self.__name             = name
        self.__network          = network
        self.__headers          = {}
        self.__endpoints        = endpoints

    @property
    def name( self ) -> str : return self.__name
    @property
    def headers( self ) -> Dict[ str , str ] : return self.__headers

    def login(
        self , * ,
        method          : HTTPMethod    = HTTPMethod.POST,
        query           : dict          = None,
        headers         : dict          = None,
        data            : dict          = None
    ) -> None :
        if self.endpoint('LOGIN') is None: return None
        return self.request( endpoint_name='LOGIN' , method=method , query=query , headers=headers , data=data )

    def login_basic( self , * , username : str , password : str ):
        return self.login(
            headers     = { 'Authorization' : 'Basic ' + b64encode( f'{username}:{password}'.encode() ).decode() },
            data        = { 'grant_type' : 'client_credentials' }
        )

    def set_header( self , key : str , value : str ) -> None :
        self.__headers.__setitem__( key , value )

    def endpoint( self , endpoint_name : str ) -> Union[ Template , None ] :
        endpoint : str = self.__endpoints.get( endpoint_name )
        if endpoint is None: return None
        return Template( endpoint )

    def get_endpoint( self , endpoint_name : str , **query : Mapping ) -> str :
        try:
            endpoint = self.endpoint( endpoint_name ).substitute( **query )
        except Exception as e:
            return None
        else:
            return endpoint

    def request(
        self,
        endpoint_name           : str,
        method                  : HTTPMethod    = HTTPMethod.GET,
        query                   : dict          = None,
        headers                 : dict          = None,
        data                    : dict          = None
    ) -> Union[ Any , None ] :
        endpoint                : str   = self.get_endpoint( endpoint_name , **( query or {} ) )
        if endpoint is None:    return None
        return self.__network.request(
            method          = method,
            url             = endpoint,
            headers         = ( headers or {} ) | self.__headers,
            data            = data
        )

    def search_artist( self , artist_name : str ) -> Union[ Any , None ] :
        response = self.request(
            'SEARCH_ARTIST',
            query = { 'query' : urllib.parse.quote( artist_name ) }
        )
        return response

    def artist( self , artistID : int ) -> Union[ Any , None ] :
        artist_data = self.request( 'ARTIST' , query = { 'id' : artistID } )
        return artist_data

    def albums( self , artistID : int ) -> Union[ Any , None ] :
        artist_data = self.request( 'ALBUMS' , query = { 'id' : artistID } )
        return artist_data