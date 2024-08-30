from src.mcnbt.factory_tags.tags.base_tags.base import TagBase


class TagBaseParent(TagBase):

    def __init__(self, name: str):
        super().__init__(name)
        self.length = 0
        self.children_tag_id = None
        self.children = []

    def __getitem__(self, item):
        return self.children[item]
