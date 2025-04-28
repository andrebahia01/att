import requests

def main():
    url = "https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("=== Cobertura de Vacinação COVID-19 ===")
        for country in data:
            country_name = country.get('country')
            timeline = country.get('timeline', {})
            for date, vaccines in timeline.items():
                print(f"{country_name}: {vaccines} doses aplicadas em {date}")
    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")

if __name__ == "__main__":
    main()
