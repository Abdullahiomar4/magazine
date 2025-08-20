class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("title must be between 5 and 50 characters")
        if hasattr(self, "_title"):
            raise AttributeError("title cannot be changed once set")
        self._title = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [art for art in Article.all_articles if art.author == self]

    def magazines(self):
        return list({art.magazine for art in self.articles()})

    def write_article(self, magazine, title):
        return Article(self, magazine, title)

    def topics(self):
        mags = self.magazines()
        if not mags:
            return []
        return list({mag.category for mag in mags})


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("name must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("category must be a non-empty string")
        self._category = value

    def articles(self):
        return [art for art in Article.all_articles if art.magazine == self]

    def contributors(self):
        return list({art.author for art in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [art.title for art in arts] if arts else []

    def frequent_authors(self):
        authors = [art.author for art in self.articles()]
        return [a for a in set(authors) if authors.count(a) > 2] or []

    @classmethod
    def most_popular(cls):
        if not Article.all_articles:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()), default=None)


if __name__ == "__main__":
    m1 = Magazine("Global Voices", "World Affairs")
    m2 = Magazine("Inspire", "Art and Culture")

    a1 = Author("Abdullah Khan")
    a2 = Author("Hana Ali")

    art1 = Article(a1, m1, "The Future of AI")
    art2 = Article(a2, m1, "Navigating the World of Remote Learning")
    art3 = Article(a1, m2, "The Rat of Digital Painting")

    print("Articles by Abdullah:", [a.title for a in a1.articles()])
    print("Contributors to Global Voices:", [a.name for a in m1.contributors()])
    print("Titles in Global Voices:", m1.article_titles())
    print("Frequent authors in Global Voices:", [a.name for a in m1.frequent_authors()])
    top_mag = Magazine.most_popular()
    print("Most popular magazine:", top_mag.name if top_mag else None)