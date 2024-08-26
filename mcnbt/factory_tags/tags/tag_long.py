from mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent


class Long(TagBaseParent):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 4
        self.tag_name = 'TagLong'
        self.value = None
