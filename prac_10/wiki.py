"""
CP1404 Practical
Harrison O'Kane
Prompts user for page title and prints page details
Estimated Time to Complete - 0:30
Actual Time to Complete -
"""

import wikipedia

def fetch_wiki_page(title):
    """Attempts to fetch Wiki page with given title."""
    try:
        page = wikipedia.page(title, autosuggest=False)
        return page
    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
    except wikipedia.PageError:
        print(f"Page not found for title: {title}")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
FUNCTION main():
    WHILE True:
        title = INPUT "Enter a Wikipedia page title or search phrase (or leave blank to exit): "
        IF title IS empty:
            BREAK
        page = CALL fetch_wiki_page(title)
        IF page IS NOT None:
            PRINT "Title: " + page.title
            PRINT "Summary: " + page.summary
            PRINT "Content: " + first 500 characters of page.content
            PRINT separator line

CALL main()
"""