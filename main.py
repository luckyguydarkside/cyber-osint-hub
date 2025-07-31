import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetches HTTP headers from a given URL.
    
    Parameters:
        url (str): The URL to fetch headers from.
    
    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Return the headers as a dictionary
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers to extract relevant information.
    
    Parameters:
        headers (dict): The HTTP headers to analyze.
    
    Returns:
        None
    """
    if headers is None:
        print("No headers to analyze.")
        return

    print("HTTP Header Analysis:")
    print("---------------------")
    
    # Print the status code and server type
    print(f"Status Code: {headers.get('Status', 'N/A')}")
    print(f"Server: {headers.get('Server', 'N/A')}")
    
    # Check for security-related headers
    security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy']
    for header in security_headers:
        print(f"{header}: {headers.get(header, 'Not Set')}")

def main():
    """
    Main function to run the OSINT HTTP header analysis tool.
    
    Returns:
        None
    """
    # User input for the URL to analyze
    url = input("Enter a URL to analyze (e.g., http://example.com): ")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not parsed_url.scheme:  # Add 'http://' if no scheme is provided
        url = 'http://' + url
    
    # Fetch and analyze HTTP headers for the given URL
    headers = fetch_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()