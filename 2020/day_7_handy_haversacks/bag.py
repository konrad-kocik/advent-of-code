class Bag:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    def __repr__(self):
        return '{}: {}'.format(self._name, self._content)

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    def add_content(self, content):
        self._content = list(set(self._content + content))
