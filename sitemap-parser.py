import xml.etree.ElementTree as ET



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
    

# Load the sitemap.xml file
tree = ET.parse('./gpt-hacking/sitemap.xml')
root = tree.getroot()

# Extract the links
links = []
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    links.append(loc)

# Write the links to a file
with open('./gpt-hacking/sitemap_links.txt', 'w') as f:
    for link in links:
        f.write(extract_id_from_url(link) + ' exists ' + link + '\n')    