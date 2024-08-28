
class TagBase:

    def __init__(self, name: str):
        self.name = name
        self.tag_name = ''
        self.tag_id = None

    def __repr__(self):
        return f'{self.name}'
