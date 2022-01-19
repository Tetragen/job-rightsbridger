from typing                         import List, Dict
from dotenv                         import dotenv_values
from tabulate                       import tabulate

from src.print.utils                import print_msg
from src.RightsBridger              import RightsBridger
from src.providers.utils            import get_object_field
from src.entities.RBArtist          import RBArtist


REQUIRED_ENVIRONMENT_VALUES                 = [ 'ARTIST' , 'SPOTIFY_CLIENT_ID' , 'SPOTIFY_CLIENT_SECRET' ]

def main( debug : bool = True ):
    config                                  : dict              = dotenv_values('.env')
    env_requirements_status                 : Dict[str, bool]   = { required : (config.get(required) is not None and config[required] != '') for required in REQUIRED_ENVIRONMENT_VALUES }
    env_requirements_fulfilled              : List[bool]        = list( env_requirements_status.values() )
    if all( env_requirements_fulfilled ):
        rb              : RightsBridger     = RightsBridger( config = config )
        results         : List[RBArtist]    = rb.search_artist( config['ARTIST'] )
        print(
            tabulate(
                tabular_data    = [ [ r.artistProvider , r.name , r.artistID , r.followers , r.nb_albums ] for r in results ],
                headers         = [ 'Provider' , 'Name' , 'ID' , 'followers' , 'albums' ],
                tablefmt='github'
            )
        )
    else:
        unfulfilled_env_requirements = [ req for req , fulfilled in env_requirements_status.items() if fulfilled is False ]
        print_msg( 'error', f'Missing environment key-values : { unfulfilled_env_requirements }' )


if __name__ == '__main__':
    main()