import sys
import webbrowser
import requests

from guessit import guessit

def _makeAnilistQuery(name):
    # This function makes a query to Anilist and returns the response.
    # It takes the name of the series to search by.
    # If successful, it will return the Anilist URL.
    # If failed, it will rasie an Exception.

    ANILIST_API_URL = 'https://graphql.anilist.co'

    query = '''
    query ($searchStr: String) { 
        Media (search: $searchStr, type: ANIME) {
            siteUrl
        }
    }
    '''

    variables = {
        'searchStr': name
    }

    response = requests.post(ANILIST_API_URL, json={'query': query, 'variables': variables})

    if response.status_code == 200:
        # Parse out the Anilist URL to use.
        return response.json()["data"]["Media"]["siteUrl"]
    else:
        raise Exception("Query failed!")

    return None

def get_anilist_url(filename):
    # Given a filename (as passed from mpv) this function attempts
    # to locate the corresponding Anilist page. It uses guessit 
    # to determine relevant properties.
    name = ""

    # Use guessit to get as much information as we can
    g = guessit(filename)

    # Dump the info to the console for debugging purposes
    print(g)
    
    # Get the name of the anime from the results (hopefully)
    name = g["title"]

    # If there is a season attached, append it to the name.
    if "season" in g:
        name = name + " " + str(g["season"])

    # If there is a part attached, append it to the name.
    if "part" in g:
        name = name + " " + str(g["part"])

    # Do any other modifications here based on guessit results.

    # Make query for the anime!
    return _makeAnilistQuery(name)

if __name__ == "__main__":
    try:
        url = get_anilist_url(sys.argv[1])
        webbrowser.open_new_tab(url)
    except Exception as e:
        print("ERROR: {}".format(e))
        sys.exit(1)