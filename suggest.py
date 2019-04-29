import requests
import re
import argparse




# Input args
parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="Enter a keyword (i.e., a search string)")
args = parser.parse_args()
print(args.keyword)

# Build url
url = "https://clients1.google.com/complete/search?client=youtube&hl=en&gl=gb&gs_rn=23&gs_ri=youtube&ds=yt&cp=5&gs_id=9&q={}&callback=google.sbox.p50&gs_gbg=DCK2xxW6vto2FGXTX8nec69nB8lkn47dM".format(args.keyword)

# Make request
resp = requests.get(url)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('Unexpected error')

# Parse response
regex = '\["(.*?)"'
matches = re.findall(regex, resp.text)

# Print output
for match in matches:
    print(match)
