from googlesearch import search

search_string = 'site:sharegpt.com'  # Replace with your desired search string
num_pages = 10  # Number of pages to fetch

# Function to fetch results for all pages
def fetch_all_results(query, num_pages):
    results = []
    for page in range(num_pages):
        try:
            for link in search(query, num_results=1000):
                results.append(link)
                print(extract_id_from_url(link) + ' exists ' + link)
        except Exception as e:
            print(f'Error fetching results for page {page}: {e}')
    return results

# Fetch results for all pages
all_results = fetch_all_results(search_string, num_pages)
print('Results:', all_results)


def extract_id_from_url(url):
    # Check if the URL is empty
    if not url:
        return None

    try:
        # Split the URL by '/'
        url_parts = url.split('/')

        # Find the index of 'c' in the URL parts
        c_index = url_parts.index('c')

        # Extract the ID from the URL
        id = url_parts[c_index + 1]

        return id

    except ValueError:
        # If 'c' is not found in the URL, return None
        return None