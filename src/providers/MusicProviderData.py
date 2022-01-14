class MusicProviderData:
    __provider_name                     : str
    @property
    def name( self ) -> str : return self.__provider_name

    __followers                         : int   = None
    @property
    def followers( self ) -> str : return self.__followers

    def __str__(self) -> str:
        return '<Result [ {provider_name} ] followers={followers}>'.format(
            provider_name       = self.__provider_name,
            followers           = self.__followers
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __init__( self , * , provider_name : str , followers : int ) -> None:
        self.__provider_name    = provider_name
        self.__followers        = followers