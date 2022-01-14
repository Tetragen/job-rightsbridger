import requests
from typing                         import List

from src.RightsBridger              import RightsBridger
from src.artist.utils               import get_object_field
from src.artist.RBArtist            import RBArtist


def main( debug : bool = True ):
    rb              : RightsBridger     = RightsBridger()
    results         : List[RBArtist]    = rb.search_artist( artist_name='Justice' )
    print( f'RESULTS = {results}' )

    # result = get_object_field(
    #     {
    #         'persons'   : [
    #             { 'name' : { 'first' : 'Ursule' , 'last' : 'Wojanski' } ,   'age' : 13 },
    #             { 'name' : { 'first' : 'Gael'   , 'last' : 'Cerini' } ,     'age' : 21 },
    #             { 'name' : { 'first' : 'Lucien' , 'last' : 'Diop' } ,       'age' : 42 },
    #             { 'name' : { 'first' : 'Hector' , 'last' : 'Malivaux' } ,   'age' : 99 }
    #         ]
    #     },
    #     [ 'persons' , 'persons.name.last' ]
    #     # 'persons.age'
    #     # 'persons.name.last'
    # )
    # print( f'RESULT = { result }')


if __name__ == '__main__':
    main()