from src.mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent


class IntArray(TagBaseParent):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 11
        self.children_tag_id = 3
        self.tag_name = 'TagIntArray'
