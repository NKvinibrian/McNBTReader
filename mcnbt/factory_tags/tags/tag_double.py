from mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class Double(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 6
        self.tag_name = 'TagDouble'
        self.value = None
