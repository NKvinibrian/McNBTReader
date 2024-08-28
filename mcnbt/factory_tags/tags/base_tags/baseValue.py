from mcnbt.factory_tags.tags.base_tags.base import TagBase


class TagBaseValue(TagBase):

    def __init__(self, name: str):
        super().__init__(name)
        self.value = None

    def __repr__(self):
        return f'{self.name}: {self.value}'