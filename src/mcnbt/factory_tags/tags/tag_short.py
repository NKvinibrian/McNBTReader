from mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class Short(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 2
        self.tag_name = 'TagShort'
        self.value = None
