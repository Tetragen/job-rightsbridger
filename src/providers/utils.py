import re
from typing						import List, Dict, NewType, TypeVar, Any

ObjectField                     = TypeVar( 'ObjectField' , str , int )
ObjectFields                    = NewType( 'ObjectFields' , List[ ObjectField ] )
ObjectFieldPath                 = TypeVar( 'ObjectFieldPath' , str , List[str] )


def get_object_field( data : dict , sfields : ObjectFieldPath ) -> Any:
    def __recurse_object_field( o : Any , fieldspath : List[ ObjectField ] ) -> Any:
        if fieldspath is None or len( fieldspath ) == 0:
            return o
        elif isinstance( fieldspath[0] , int ):
            if not isinstance( o , list ):  return None
            else:                           return __recurse_object_field( o.__getitem__( fieldspath[0] ) , fieldspath[1:] )
        elif isinstance( fieldspath[0] , str ):
            if isinstance( o , list ):      return [ __recurse_object_field( okey , fieldspath ) for okey in o ]
            elif isinstance( o , dict ):    return __recurse_object_field( o.get( fieldspath[0] ) , fieldspath[1:] )
            else:                           return None
        else:
            return None

    def __pathify_sliced_fieldpath( fieldpath : List[str] ) -> List[ ObjectField ] :
        pathified_fieldpath : List[ ObjectField ] = []
        for f in fieldpath:
            slices : list = re.findall( '\[[0-9]+\]$' , f )
            if len( slices ) > 1    : return None
            if len( slices ) == 0   : pathified_fieldpath.append( f )
            else:
                field_and_index     = re.search( r'^([a-zA-Z-_]+)\[([0-9]+)\]$' , f )
                field : str         = field_and_index.group( 1 ) 
                index : int         = int( field_and_index.group( 2 ) )
                pathified_fieldpath.append( field )
                pathified_fieldpath.append( index )
        return pathified_fieldpath

    def __get_sfields_values( data : dict , sfields : ObjectFieldPath ) -> Any :
        if sfields is not None:
            if isinstance( sfields , list ):
                field_values        : Dict[ str , Any ]             = {}
                for sfield in sfields:
                    field_values.__setitem__(
                        sfield,
                        __recurse_object_field( data , __pathify_sliced_fieldpath( sfield.split( '.' ) ) )
                    )
                return field_values
            elif isinstance( sfields , str ):
                fields          = sfields.split( '.' )
                return __recurse_object_field( data , __pathify_sliced_fieldpath( fields ) )

    values = __get_sfields_values( data , sfields )
    return values