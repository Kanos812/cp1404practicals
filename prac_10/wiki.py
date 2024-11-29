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
    try:
        wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent='YourAppName/1.0 (Your Contact Info)')
        page = wiki_wiki.page(title)
        if page.exists():
            return page
        else:
            print(f"Page not found for title: {title}")
            return None
    except wikipediaapi.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
    except wikipediaapi.PageError:
        print(f"Page not found for title: {title}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Prompt user for page title or search phrase to print details."""
    while True:
        title = input("Enter a Wikipedia page title or search phrase (or leave blank to exit): ")
        if not title:
            break
        page = fetch_wiki_page(title)
        if page:
            print(f"\nTitle: {page.title}\n")
            print(f"Summary: {page.summary[:500]}...\n")  # Print first 500 characters of summary
            print(f"Content: {page.text[:500]}...")  # Print first 500 characters of content
            print("\n" + "-" * 80 + "\n")

if __name__ == '__main__':
    main()
