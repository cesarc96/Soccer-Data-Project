import httpx
from soccer_data.models import LeaguesResponse


BASE_URL = "https://v3.football.api-sports.io"


class SoccerDataClient:
    def __init__(self, api_key: str) -> None:
        self._client = httpx.Client(
            base_url=BASE_URL,
            headers={"x-apisports-key": api_key},
        )

    def get_leagues(self) -> LeaguesResponse:
        response = self._client.get("/leagues")
        response.raise_for_status()
        return LeaguesResponse.model_validate(response.json())

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "SoccerDataClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
