"""
CP1404 Practical
Harrison O'Kane
Prompts user for page title and prints page details
Estimated Time to Complete - 0:30
Actual Time to Complete -
"""

import wikipediaapi

def fetch_wiki_page(title):
    """Attempts to fetch Wiki page with given title."""
    wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent='YourAppName/1.0 (Your Contact Info)')
    page = wiki_wiki.page(title)
    if page.exists():
        return page
    else:
        print(f'Page id "{title}" does not match any pages. Try another id!')
        return None

def is_disambiguation(page):
    """Check if a page is a disambiguation page."""
    return "may refer to:" in page.summary[:100]

def main():
    """Prompt user for page title or search phrase to print details."""
    while True:
        title = input("Enter a Wikipedia page title or search phrase (or leave blank to exit): ")
        if not title:
            print("Thank you.")
            break
        page = fetch_wiki_page(title)
        if page:
            if is_disambiguation(page):
                print("We need a more specific title. Try one of the following, or a new search:")
                for link in page.links.keys():
                    print(link)
            else:
                print(f"\nTitle: {page.title}\n")
                print(f"Summary: {page.summary[:500]}...\n")  # Print first 500 characters of summary
                print(f"URL: {page.fullurl}\n")

if __name__ == '__main__':
    main()
