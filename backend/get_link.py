import requests
try:
    resp = requests.get("https://data.mendeley.com/api/datasets/9jnf2jvghy/2", timeout=5)
    if resp.status_code == 200:
        data = resp.json()
        print("Data keys:", data.keys())
        if 'files' in data:
            for f in data['files']:
                if 'content_details' in f and 'download_url' in f['content_details']:
                    print("LINK:", f['content_details']['download_url'])
        if 'repository_urls' in data:
            print("REPO URLS:", data['repository_urls'])
    else:
        print("Failed to fetch API:", resp.status_code)
except Exception as e:
    print("Error:", e)
