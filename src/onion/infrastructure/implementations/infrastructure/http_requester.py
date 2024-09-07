import sys
from urllib.error import URLError
from urllib.parse import ParseResult, urlencode, urlparse
from urllib.request import Request, urlopen
import base64
import json

from onion.domain.interfaces.infrastructure.logger import ILogger


class HttpRequester:
    """
    Class that sends HTTP requests.
    """

    def __init__(self, logger: ILogger, auth: tuple[str, str] | None = None):
        self._logger = logger
        self._auth = auth

    def get(self, url: str, params: list[tuple[str, str]]) -> dict[str, str]:
        """
        Sends a GET request to the given URL.

        We do not handle exceptions here, because we want to raise them in the calling code.
        This way, the calling code can decide what to do in case of an error.

        If the remote randomizer service is not available, we log an error message and exit the application.
        In all other cases, we raise the exception to the calling code.

        :param url: URL to send the request to
        :param params: query string parameters in format [('key1', 'value1'), ('key2', 'value2')]
        :return: response from the server in JSON format
        """
        parsed_url: ParseResult = urlparse(url)
        query_string: str = urlencode(params)

        full_url: str = (
            f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{query_string}"
        )

        headers: dict[str, str] = {}

        if self._auth:
            base64_auth = base64.b64encode(
                f"{self._auth[0]}:{self._auth[1]}".encode("utf-8")
            ).decode("utf-8")
            headers["Authorization"] = f"Basic {base64_auth}"

        try:
            response = urlopen(Request(full_url, headers=headers))
        except URLError as e:
            if e.args[0].errno == 111:
                self._logger.error(
                    f"Remote randomizer services is not available at {parsed_url.netloc}. "
                    f"Try to use local randomizer by passing 'local' value to '--randomizer-type' "
                    f"CLI argument."
                )
                sys.exit(-1)
            else:
                raise e
        else:
            return json.load(response)
