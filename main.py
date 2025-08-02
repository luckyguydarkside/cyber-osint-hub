import requests
from urllib.parse import urlparse
import json

def get_http_headers(url):
    """
    Fetch the HTTP headers from a given URL.

    :param url: The URL from which to fetch headers.
    :return: A dictionary of HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return {}

def analyze_headers(headers):
    """
    Analyze HTTP headers for security-related information.

    :param headers: A dictionary of HTTP headers.
    :return: A summary of security-related findings.
    """
    security_headers = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Content-Type-Options',
        'X-Frame-Options',
        'X-XSS-Protection'
    ]
    
    findings = {}
    for header in security_headers:
        findings[header] = headers.get(header, 'Missing')
    
    return findings

def main():
    """
    Main function to run the OSINT HTTP header analysis.
    Prompts user for a URL and outputs security header analysis.
    """
    url = input("Enter the URL to analyze (e.g., https://example.com): ")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please include the scheme (http/https).")
        return
    
    print(f"Fetching HTTP headers for: {url}")
    
    # Get HTTP headers
    headers = get_http_headers(url)
    
    if headers:
        print("HTTP Headers retrieved successfully.")
        print(json.dumps(headers, indent=4))  # Print all headers for reference
        
        # Analyze the headers for security-related information
        findings = analyze_headers(headers)
        
        print("\nSecurity Header Analysis:")
        for header, status in findings.items():
            print(f"{header}: {status}")

if __name__ == "__main__":
    main()
```