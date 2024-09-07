from typing import Protocol


class IHttpRequester(Protocol):
    """
    Interface for class that sends HTTP requests.
    """

    def get(self, url: str, params: list[tuple[str, str]]) -> dict[str, str]:
        """
        Sends a GET request to the given URL.

        :param url: URL to send the request to
        :param params: query string parameters in format [('key1', 'value1'), ('key2', 'value2')]
        :return: response from the server in JSON format
        """
