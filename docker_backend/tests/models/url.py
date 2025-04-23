class URL:
    def __init__(self, url: str):
        self.url = url

    def __truediv__(self, other: str):
        return f"{self.url}/{other}"

    def __str__(self):
        return self.url

    def __repr__(self):
        return f"URL({self.url})"
