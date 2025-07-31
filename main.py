import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetch HTTP headers for a given URL.
    
    Parameters:
    url (str): The URL to fetch headers from.

    Returns:
    dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyze HTTP headers and extract key information.

    Parameters:
    headers (dict): The HTTP headers to analyze.

    Returns:
    None
    """
    if headers:
        print("HTTP Headers Analysis:")
        print("-" * 30)
        for header, value in headers.items():
            print(f"{header}: {value}")

        # Check for security-related headers
        security_headers = ['Content-Security-Policy', 'X-Content-Type-Options', 'X-Frame-Options']
        print("\nSecurity Headers:")
        for header in security_headers:
            if header in headers:
                print(f"{header}: {headers[header]}")
            else:
                print(f"{header}: Not present")

def main():
    """
    Main function to execute the OSINT HTTP header analysis.
    """
    # Input URL from user
    url = input("Enter a URL to analyze (e.g., https://example.com): ")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url  # Add HTTP scheme if missing

    # Fetch and analyze HTTP headers
    headers = fetch_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()
```