import requests
import re

def get_hidden_code():
    ip = "120.138.30.179"
    url = f"http://{ip}/"
    headers = {
        "Host": "site.recruitment.shq.nz"
    }

    try:
        print(f"Requesting {url} with Host: site.recruitment.shq.nz...\n")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Preview part of the response
        print("----- HTML Preview (first 500 chars) -----")
        print(response.text[:500])
        print("------------------------------------------\n")

        # Search for the hidden code in the HTML comment inside <head>
        match = re.search(r'<!--\s*This is what you\'re looking for:\s*(.*?)\s*-->', response.text)
        if match:
            code = match.group(1)
            print("✅ Hidden code found:", code)
        else:
            print("⚠️ Hidden code comment not found in the page source.")

    except requests.RequestException as e:
        print("❌ Error fetching the site:", e)

if __name__ == "__main__":
    get_hidden_code()
