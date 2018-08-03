# Zadanie 11
# Zaimplementuj klasy odpowiedzialne za tworzenie dokumenty w
# składni MarkDown. Stwórz klase bazowa Element zawierajaca
# podstawowa implementacje metody render() oraz kilka jej klas
# pochodnych. Stwórz klase Document umozliwiajaca wyrendorowanie
# dodanych elementów.
# Przykład uzycia:
# >>> document = Document()
# >>> document.add_element(HeaderElement('Header'))
# >>> document.add_element(LinkElement('ABC', 'abc.com'))
# >>> document.add_element(Element('Simple'))
# >>> document.render()
# Header
# ======
# (ABC)[http://abc.com]
# Simple

class Element:
    def __init__(self, content):
        self.content = content

    def render(self):
        return (self.content)


class HeaderElement(Element):
    def render(self):
        return f'{self.content} \n======'


class LinkElement(Element):
    def __init__(self, link_name, link):
        self.link_name = link_name
        self.link = link

    def render(self):
        return (f'({self.link_name}) [http://{self.link}]')


class Document:
    def __init__(self):
        self.document_content = []

    def add_element(self, element):
        self.document_content.append(element.render())

    def render(self):
        for i in self.document_content:
            print(i)


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()