import requests
import argparse
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetches and returns the HTTP headers of a given URL.
    :param url: The target URL to analyze.
    :return: A dictionary containing HTTP headers.
    """
    try:
        response = requests.get(url)
        # Return the HTTP headers as a dictionary
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes the HTTP headers and extracts key information.
    :param headers: The HTTP headers to analyze.
    :return: A summary of key header information.
    """
    analysis = {
        "Server": headers.get("Server", "N/A"),
        "Content-Type": headers.get("Content-Type", "N/A"),
        "Content-Length": headers.get("Content-Length", "N/A"),
        "X-Powered-By": headers.get("X-Powered-By", "N/A"),
        "Strict-Transport-Security": headers.get("Strict-Transport-Security", "N/A"),
    }
    return analysis

def print_analysis(analysis):
    """
    Prints the analysis of HTTP headers in a readable format.
    :param analysis: The analyzed header information.
    """
    print("\n--- HTTP Header Analysis ---")
    for key, value in analysis.items():
        print(f"{key}: {value}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Analyze HTTP Headers of a URL.")
    parser.add_argument("url", help="The URL to analyze (e.g., http://example.com)")
    args = parser.parse_args()

    # Parse the input URL
    parsed_url = urlparse(args.url)
    if not parsed_url.scheme:
        print("Please provide a valid URL with scheme (http/https).")
        return

    # Fetch and analyze HTTP headers
    headers = fetch_http_headers(args.url)
    if headers:
        analysis = analyze_headers(headers)
        print_analysis(analysis)

if __name__ == "__main__":
    main()