# Find didden Directory using key words
#!/bin/python
# @Time    : 07/11/2024
# @Author  : DEADARMY
# Version: 1.0
import requests
from concurrent.futures import ThreadPoolExecutor
import sys

def find_hidden_directory(domain, wordlist_file, max_threads=10):
    """
    Finds hidden directories on a domain using a wordlist for brute-forcing.

    Parameters:
    - domain (str): The target domain (e.g., "https://example.com").
    - wordlist_file (str): Path to the wordlist file containing potential directory names.
    - max_threads (int): Maximum number of threads for concurrent requests.
    """
    # Normalize the domain to ensure it starts with http/https
    if not domain.startswith("http"):
        domain = "https://" + domain

    # Load the wordlist
    try:
        with open(wordlist_file, 'r') as file:
            paths = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Wordlist file not found.")
        sys.exit(1)

    # Check a single path
    print("[++] Start Scanning")
    def check_path(path):
        url = f"{domain}/{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found directory: {url}")
        except requests.RequestException:
            pass

    # Use threading for faster performance
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(check_path, paths)

if __name__ == "__main__":
    domain = input("Enter the domain (e.g., example.com): ")
    wordlist_file = input("Enter the path to your wordlist file: ")
    find_hidden_directory(domain, wordlist_file)
