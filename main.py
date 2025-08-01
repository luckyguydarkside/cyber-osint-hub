import requests
from urllib.parse import urlparse
import json

def fetch_http_headers(url):
    """
    Fetch HTTP headers from a given URL.
    
    Parameters:
    - url (str): The URL from which to fetch headers.
    
    Returns:
    - headers (dict): A dictionary of HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return {}

def parse_url(url):
    """
    Parse the URL to extract its components.
    
    Parameters:
    - url (str): The URL to parse.
    
    Returns:
    - components (dict): A dictionary of URL components.
    """
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path": parsed.path,
        "params": parsed.params,
        "query": parsed.query,
        "fragment": parsed.fragment
    }

def main():
    """
    Main function to run the OSINT tool.
    """
    target_url = input("Enter a URL to analyze (e.g., https://example.com): ")
    
    # Fetch HTTP headers
    headers = fetch_http_headers(target_url)
    if headers:
        print("\nHTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")

    # Parse URL
    components = parse_url(target_url)
    print("\nParsed URL Components:")
    print(json.dumps(components, indent=4))

if __name__ == "__main__":
    main()
```