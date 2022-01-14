import json

from typing                     import List
from string                     import Template
from src.requests.HTTPMethod    import HTTPMethod


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_msg(type, msg, end=None):
    if type == 'info':
        print(bcolors.OKBLUE, msg, bcolors.ENDC)
    elif type == 'success':
        print(bcolors.OKGREEN, msg, bcolors.ENDC) 
    elif type == 'warning':
        print(bcolors.WARNING, msg, bcolors.ENDC)
    elif type == 'error':
        print(bcolors.FAIL, msg, bcolors.ENDC)


def curl(url, method, data, headers) -> str :
    command     : str       = "curl -X {method} -H {headers} -d '{data}' '{url}'"
    headers     : List[str] = [ '"{0}: {1}"'.format(k, v) for k, v in headers.items() ]
    return command.format(
        method              = method.name,
        data                = json.dumps( data or {} ),
        headers             = " -H ".join(headers),
        url                 = url
    )


def powershell( url : str , method : HTTPMethod , data : dict , headers : dict ) -> str :
    command     : Template       = Template(
        "Invoke-WebRequest"                 +
        " -Method ${method}"                +
        " -Headers ${headers}"              +
        " -Body '${data}'"                  +
        " -ContentType ${content_type}"     +
        " -Uri '${url}'"
    )
    powershell_headers  = "@{"  +  ", ".join(  [ '"'+k+'"' + " = " + '"'+v+'"' for k,v in headers.items() ]  )  + "}"
    return command.safe_substitute(
        method              = method.name,
        data                = json.dumps( data or {} ),
        headers             = powershell_headers,
        content_type        = 'application/json',
        url                 = url
    )