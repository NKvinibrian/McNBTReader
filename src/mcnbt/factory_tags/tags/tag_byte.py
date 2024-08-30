from src.mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class Byte(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 1
        self.tag_name = 'TagByte'
