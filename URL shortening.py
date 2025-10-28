import requests


def get_long_url_from_user():
    """
    Prompts the user to enter a long URL.
    Returns the URL as a string.
    """
    print("==============================================")
    print("          URL SHORTENER USING TINYURL         ")
    print("==============================================\n")

    while True:
        long_url = input("Step 1 - Enter the long URL you want to shorten: ").strip()
        if long_url.startswith("http://") or long_url.startswith("https://"):
            print(f"✅ Valid URL entered: {long_url}\n")
            return long_url
        else:
            print("❌ Invalid URL. Please make sure it starts with 'http://' or 'https://'\n")


def shorten_url(long_url):
    """
    Uses TinyURL's public API to shorten a long URL.
    Returns the shortened URL as a string.
    """
    print("Step 2 - Sending request to TinyURL API...")
    api_endpoint = f"https://tinyurl.com/api-create.php?url={long_url}"

    try:
        response = requests.get(api_endpoint, timeout=10)  # 10-second timeout
        response.raise_for_status()  # Raise exception for HTTP errors
        short_url = response.text.strip()

        print("Step 3 - Response received successfully.")
        return short_url
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to TinyURL API. Check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Try again later."
    except requests.exceptions.RequestException as err:
        return f"An unexpected error occurred: {err}"


def display_results(long_url, short_url):
    """
    Displays the results in a clear and formatted way.
    """
    print("\n==============================================")
    print("                 SHORTENING RESULT            ")
    print("==============================================")
    print(f"Original URL: {long_url}")
    print(f"Shortened URL: {short_url}")
    print("==============================================\n")
    print("🎉 You can now copy and use the shortened URL!")


def main():
    """
    Main function to run the program.
    """
    long_url = get_long_url_from_user()
    short_url = shorten_url(long_url)
    display_results(long_url, short_url)


if __name__ == "__main__":
    main()
