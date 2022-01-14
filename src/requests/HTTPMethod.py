from enum                   import Enum, auto


class HTTPMethodEnumName( Enum ):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class HTTPMethod( HTTPMethodEnumName ):
    GET             = auto()
    POST            = auto()
    DELETE          = auto()