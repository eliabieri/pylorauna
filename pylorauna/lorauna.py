from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dataclasses import dataclass


@dataclass
class LoraunaData:
    """ The current capacity of the sauna
    """
    capacity_message: str


class LoraunaClient:
    QUERY = gql(
        """
        query {
            allSaunas { capacity_message }
        }
    """
    )

    def __init__(self) -> None:
        transport = AIOHTTPTransport(url="https://lorauna.app/api")
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def get_data(self) -> LoraunaData:
        return LoraunaData(
            capacity_message=self._client.execute(self.QUERY)["allSaunas"][0]["capacity_message"]
        )