import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetch the HTTP headers from a given URL.

    Parameters:
        url (str): The URL to fetch the headers from.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        # Return the headers in a dictionary format
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyze HTTP headers for common security vulnerabilities.

    Parameters:
        headers (dict): The HTTP headers to analyze.

    Returns:
        dict: A dictionary with analysis results.
    """
    analysis = {
        "X-Content-Type-Options": headers.get("X-Content-Type-Options", "Missing"),
        "X-Frame-Options": headers.get("X-Frame-Options", "Missing"),
        "Content-Security-Policy": headers.get("Content-Security-Policy", "Missing"),
        "Strict-Transport-Security": headers.get("Strict-Transport-Security", "Missing"),
    }
    return analysis

def main():
    """
    Main function to run the OSINT HTTP Header Analyzer.
    """
    # Example target URL
    target_url = input("Enter the URL to analyze (e.g., https://example.com): ")
    
    # Parse the URL to ensure it is valid
    parsed_url = urlparse(target_url)
    if not parsed_url.scheme:
        print("Please include the scheme (http or https) in the URL.")
        return

    # Fetch and analyze the HTTP headers
    headers = fetch_http_headers(target_url)
    if headers:
        print("\nHTTP Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")

        print("\nSecurity Header Analysis:")
        analysis = analyze_headers(headers)
        for header, result in analysis.items():
            print(f"{header}: {result}")

if __name__ == "__main__":
    main()
```