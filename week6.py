import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extracts filename from URL or generates one based on a hash."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename:
        # Generate a unique name using a hash of the URL
        hash_digest = hashlib.md5(url.encode()).hexdigest()
        filename = f"downloaded_image_{hash_digest}.jpg"
    
    return filename

def fetch_image(url, save_dir="Fetched_Images"):
    """Fetches a single image from a URL and saves it in the specified directory."""
    try:
        # Create the directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)

        # Fetch the image with a timeout
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0 (Respectful Fetcher)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Check content-type to ensure it's an image
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print(f"✗ Skipped: URL does not point to an image: {url}")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(save_dir, filename)

        # Prevent duplicates: skip if file already exists
        if os.path.exists(filepath):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    urls_input = input("Please enter image URLs (comma-separated if multiple): ")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    
    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
