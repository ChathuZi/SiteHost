import requests

API_KEY = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"
BASE_URL = "https://api.recruitment.shq.nz"
CLIENT_ID = 100

def get_domains(client_id):
    url = f"{BASE_URL}/domains/{client_id}?api_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_zone_records(zone_id):
    url = f"{BASE_URL}/zones/{zone_id}?api_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_zone_id(uri):
    return uri.split('/')[-1]

def main():
    print("Fetching domain info...\n")
    domains_data = get_domains(CLIENT_ID)

    for domain in domains_data:
        print(f"Domain: {domain['name']}")
        for zone in domain.get('zones', []):
            zone_id = extract_zone_id(zone['uri'])
            print(f"  Zone name: {zone['name']}, Zone ID: {zone_id}")

            zone_records_data = get_zone_records(zone_id)

            print("    DNS Records:")
            if isinstance(zone_records_data, dict) and 'records' in zone_records_data:
                records = zone_records_data['records']
            else:
                records = zone_records_data

            for record in records:
                if isinstance(record, dict):
                    print(f"      Type: {record.get('type')}, Name: {record.get('name')}, Content: {record.get('content')}")
                else:
                    print(f"      Record: {record}")

if __name__ == "__main__":
    main()
