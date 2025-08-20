# README.md
# Magazine Management System

This project is a simple Python implementation of a magazine management system using three classes: `Article`, `Author`, and `Magazine`.

## Features

- **Article**: Represents an article written by an author for a magazine.
- **Author**: Represents an author who can write articles for different magazines.
- **Magazine**: Represents a magazine that can have multiple articles and contributors.

## Example Usage

```python
m1 = Magazine("Global Voices", "World Affairs")
m2 = Magazine("Inspire", "Art and Culture")

a1 = Author("Abdullah Khan")
a2 = Author("Hana Ali")

art1 = Article(a1, m1, "The Future of AI")
art2 = Article(a2, m1, "Navigating the World of Remote Learning")
art3 = Article(a1, m2, "The Art of Digital Painting")

print("Articles by Abdullah:", [a.title for a in a1.articles()])
print("Contributors to Global Voices:", [a.name for a in m1.contributors()])
print("Titles in Global Voices:", m1.article_titles())
print("Frequent authors in Global Voices:", [a.name for a in m1.frequent_authors()])
top_mag = Magazine.most_popular()
print("Most popular magazine:", top_mag.name if top_mag else None)
```

## How to Run

1. Make sure you have Python 3 installed.
2. Save the code in `index.py`.
3. Run the script:
   ```
   python3 index.py
   ```
   or
   ```
   python index.py
   ```

## License

This project is for educational purposes.
