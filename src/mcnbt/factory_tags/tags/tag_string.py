from src.mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class String(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 8
        self.tag_name = 'TagString'
        self.value = None
