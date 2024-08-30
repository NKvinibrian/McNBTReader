from src.mcnbt.factory_tags.tags.base_tags.baseValue import TagBaseValue


class Int(TagBaseValue):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 3
        self.tag_name = 'TagInt'
        self.value = None
