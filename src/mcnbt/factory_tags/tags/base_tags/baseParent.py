from mcnbt.factory_tags.tags.base_tags.base import TagBase


class TagBaseParent(TagBase):

    def __init__(self, name: str):
        super().__init__(name)
        self.__interator_index = 0
        self.length = 0
        self.children_tag_id = None
        self.children = []

    def __getitem__(self, item):
        return self.children[item]

    def __iter__(self):
        self.__interator_index = 0
        return self

    def __len__(self):
        return self.length

    def __next__(self):
        if self.__interator_index >= len(self.children):
            raise StopIteration
        else:
            item = self.children[self.__interator_index]
            self.__interator_index += 1
            return item
