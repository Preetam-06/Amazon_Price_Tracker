import requests

headers_ = {"User-Agent": (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/115.0.0.0 Safari/537.36")
    }

def get_page_content(url_):
    try:
        response = requests.get(url_, headers=headers_, timeout=10)
        response.raise_for_status()
        print("Amazon Page fetched successfully.")
        print(f"Returned response successfully with status code: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the Amazon page: {e}")
        return None
    finally:
        print("Request completed.")
       