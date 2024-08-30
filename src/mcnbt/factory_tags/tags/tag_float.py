from mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class Float(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 5
        self.tag_name = 'TagFloat'
        self.value = None


