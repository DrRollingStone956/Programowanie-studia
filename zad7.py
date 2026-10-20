import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: Optional[str] = None

    def __str__(self) -> str:
        return f"Brewery(name='{self.name}', type='{self.brewery_type}', city='{self.city}', country='{self.country}', website='{self.website_url}')"

def main():
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    breweries = []
    for item in data:
        valid_keys = Brewery.__annotations__.keys()
        filtered_data = {k: v for k, v in item.items() if k in valid_keys}
        brewery = Brewery(**filtered_data)
        breweries.append(brewery)

    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()