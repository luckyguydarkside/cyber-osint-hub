import requests

def fetch_http_headers(url):
    """
    Fetches HTTP headers from a given URL and returns them in a dictionary.

    :param url: str - The URL to fetch headers from
    :return: dict - A dictionary containing HTTP headers
    """
    try:
        response = requests.head(url, allow_redirects=True)
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes the HTTP headers for security-related information.

    :param headers: dict - The HTTP headers to analyze
    :return: None
    """
    # Check for common security headers
    security_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 
                        'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
    
    print("Security Header Analysis:")
    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header}: Not present")

def main():
    """
    Main function to run the script.
    Prompts user for a URL and fetches and analyzes its HTTP headers.
    """
    url = input("Enter a URL (including http:// or https://): ")
    headers = fetch_http_headers(url)
    
    if headers:
        print("\nFetched HTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```