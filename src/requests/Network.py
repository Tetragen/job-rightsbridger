import requests
from typing                     import Dict, Union, Any

from src.requests.HTTPMethod    import HTTPMethod
from src.print.utils            import powershell, print_msg, curl


class Network:
    __headers                   : Dict[ str , str ]    = None
    __requests                  = None

    def __init__(self) -> None:
        self.__requests         = requests

    def __request(
        self , * ,
        method          : HTTPMethod    = HTTPMethod.GET,
        url             : str,
        data            : dict          = None,
        headers         : dict          = None,
        debug           : bool          = False
    ):
        if debug is True:
            print_msg("info", curl(url, method, data, headers))
        result  = getattr( self.__requests , method.value )(
            url         = url,
            data        = data,
            headers     = headers
        )
        return result
 
    def request(
        self , * ,
        method          : HTTPMethod        = HTTPMethod.GET,
        url             : str,
        data            : dict              = None,
        headers         : dict              = None,
        debug           : bool              = True
    ) -> Union[ Any , None ] :
        resp = self.__request(
            method          = method,
            url             = url,
            data            = data,
            headers         = headers,
            debug           = debug
        )
        if resp.status_code != 200:
            print_msg("error", "Error {} while requesting {}...".format(resp.status_code, url))
            return None
        return resp.json()