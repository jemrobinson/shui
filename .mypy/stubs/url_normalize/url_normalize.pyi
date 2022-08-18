from .tools import (
    deconstruct_url as deconstruct_url,
    force_unicode as force_unicode,
    quote as quote,
    reconstruct_url as reconstruct_url,
    unquote as unquote,
)
from _typeshed import Incomplete

DEFAULT_PORT: Incomplete
DEFAULT_CHARSET: str
DEFAULT_SCHEME: str

def provide_url_scheme(url, default_scheme=...): ...
def generic_url_cleanup(url): ...
def normalize_scheme(scheme): ...
def normalize_userinfo(userinfo): ...
def normalize_host(host, charset=...): ...
def normalize_port(port, scheme): ...
def normalize_path(path, scheme): ...
def normalize_fragment(fragment): ...
def normalize_query(query, sort_query_params: bool = ...): ...
def url_normalize(
    url, charset=..., default_scheme=..., sort_query_params: bool = ...
): ...