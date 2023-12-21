import os
import sys
import requests
import markdown
from dotenv import load_dotenv

load_dotenv()

def publish_to_medium(filename):
    try:
        token = os.getenv("MEDIUM_TOKEN")
        if not token:
            print("Medium token not found in .env file.")
            return

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print("The file is empty.")
            return

        title = lines[0].strip().lstrip('#').strip()
        content = ''.join(lines)
        info_url = "https://api.medium.com/v1/me"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8'
        }

        data = {
            'title': title,
            'contentFormat': 'markdown',
            'content': content,
            'publishStatus': 'draft'
        }
        
        r = requests.get(info_url, headers=headers)
        userid = r.json().get('data').get('id')
        print(userid)
        r = requests.get(f'https://api.medium.com/v1/users/{userid}/publications', headers=headers)
        url = f"https://api.medium.com/v1/users/{userid}/posts"
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        print(f"Article published successfully: {response.json().get('data').get('url')}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python publish_to_medium.py <markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]

    publish_to_medium(markdown_file)

