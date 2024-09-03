from mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent


class Compound(TagBaseParent):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 10
        self.tag_name = 'TagCompound'
        self.children = {}

    def __iter__(self):
        self.__interator_index = self.children.keys().__iter__()
        return self

    def __next__(self):
        return self.children[self.__interator_index.__next__()]
