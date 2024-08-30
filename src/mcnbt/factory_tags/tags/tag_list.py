from mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent


class List(TagBaseParent):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 9
        self.tag_name = 'TagList'
