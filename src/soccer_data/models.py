from pydantic import BaseModel


class League(BaseModel):
    id: int
    name: str
    type: str
    logo: str


class Country(BaseModel):
    name: str
    code: str | None
    flag: str | None


class LeagueEntry(BaseModel):
    league: League
    country: Country


class Paging(BaseModel):
    current: int
    total: int


class LeaguesResponse(BaseModel):
    results: int
    paging: Paging
    response: list[LeagueEntry]
