from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent, BytesIO
from mcnbt.factory_tags.tags.tag_byte_array import ByteArray


class BuilderArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(ByteArray, name)

    def append(self, array: bytes, stack=None):
        self.tag_class.children = array

    def append_buffer(self, buffer: BytesIO, stack=None):
        length = self.get_len_children()
        self.append(buffer.read(length))
        return True
