from mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent


class ByteArray(TagBaseParent):

    def __init__(self, name: str):
        super().__init__(name)
        self.tag_id = 7
        self.children_tag_id = 1
        self.children: bytes = b''
        self.tag_name = 'TagByteArray'
