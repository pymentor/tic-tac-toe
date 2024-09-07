from typing import Any

from onion.infrastructure.interfaces.http_requester import IHttpRequester


class RemoteRandomizer:
    """
    Class that returns random elements from a given list of values,
    using a remote random number generator.
    """

    def __init__(
        self,
        http_requester: IHttpRequester,
        query_string_key: str,
        api_url: str,
    ) -> None:
        self._api_url = api_url
        self._http_requester = http_requester
        self._query_string_key = query_string_key

    def choice(self, *values: Any) -> Any:
        """
        Returns a random element from the given values.

        Important: hashes of values get sent to the server instead of values itself,
        thus we don't need to serialize the values before sending and then deserialize
        the response from the server.

        :param values: values to choose from randomly
        :return: a random element from the given values
        """
        # create a dictionary with hash of values as keys and values as values
        hash_map: dict[str, Any] = {str(hash(value)): value for value in values}

        # create a list of tuples with query string key and hash of values
        params: list[tuple[str, str]] = [
            (self._query_string_key, value_hash) for value_hash in hash_map.keys()
        ]

        # get the response from the server
        response: dict[str, str] = self._http_requester.get(self._api_url, params)

        # return the value from the hash map using the hash from the response
        return hash_map[response[self._query_string_key]]
