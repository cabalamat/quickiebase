# quickietypes = types used by QuickieBase

from typing import List, Union, Dict, Optional, Any, Tuple

#---------------------------------------------------------------------

DocId = str
""" identifier for a document. Must be a string. """

""" a Python dict containing JSON data """
JsonDoc = Dict[str, 'JsonValue']
JsonValue = Union[JsonDoc, List['JsonValue'], str, int, float, bool, None]

#end
