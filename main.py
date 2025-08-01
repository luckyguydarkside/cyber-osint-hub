import requests
from urllib.parse import urlparse
import json

def get_http_headers(url):
    """
    Function to retrieve HTTP headers from a given URL.
    
    Parameters:
    url (str): The URL from which to fetch the headers.
    
    Returns:
    dict: A dictionary containing HTTP headers.
    """
    try:
        response = requests.get(url)
        # Return the headers as a dictionary
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Function to analyze HTTP headers for common security vulnerabilities.
    
    Parameters:
    headers (dict): A dictionary of HTTP headers.
    
    Returns:
    dict: A dictionary containing analysis results.
    """
    analysis = {}
    
    # Check for security-related headers
    security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security']
    for header in security_headers:
        analysis[header] = 'Present' if header in headers else 'Missing'
    
    # Check for Content-Type header
    if 'Content-Type' in headers:
        analysis['Content-Type'] = headers['Content-Type']
    else:
        analysis['Content-Type'] = 'Missing'
    
    return analysis

def main():
    url = input("Enter a URL to analyze (e.g., https://example.com): ")
    parsed_url = urlparse(url)
    
    if not parsed_url.scheme:
        print("Please include the scheme (http:// or https://)")
        return
    
    headers = get_http_headers(url)
    
    if headers:
        print("\nHTTP Headers:")
        print(json.dumps(headers, indent=4))
        
        print("\nSecurity Header Analysis:")
        analysis = analyze_headers(headers)
        print(json.dumps(analysis, indent=4))

if __name__ == "__main__":
    main()
```