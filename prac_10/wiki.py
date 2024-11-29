"""
CP1404 Practical
Harrison O'Kane
Prompts user for page title and prints page details
Estimated Time to Complete - 0:30
Actual Time to Complete -
"""

import wikipedia

"""
FUNCTION fetch_wiki_page(title):
    TRY:
        page = GET Wikipedia page with title (autosuggest=False)
        RETURN page
    EXCEPT DisambiguationError AS e:
        PRINT "Disambiguation error: " + e.options
    EXCEPT PageError:
        PRINT "Page not found for title: " + title
    EXCEPT Exception AS e:
        PRINT "An error occurred: " + e

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