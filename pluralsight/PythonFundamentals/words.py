#!/usr/bin/env python3
"""Retrieve and print words from an URL

Usage:
    python3 words.py <url>
"""


from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from an URL.

    Args:
        url: The URL of an utf-8 text document.

    Returns:
        A list of string containing words from the document.
    """
    # 'http://sixty-north.com/c/t.txt'
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == "__main__":
    main(sys.argv[1])
