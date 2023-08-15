import requests
from urllib.parse import urlencode

def fetch_content(character):
    base_url = "https://somesite.internet/api/phonebook/search?"  # Replace with your actual API endpoint
    # Replace query
    params = {'query': character}
    url = base_url + urlencode(params)

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch content for '{character}'"

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        content = fetch_content(char)
        print(f"Content for character '{char}':\n{content}\n")

if __name__ == "__main__":
    main()
