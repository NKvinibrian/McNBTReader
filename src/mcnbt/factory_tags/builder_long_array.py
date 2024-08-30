from src.mcnbt.factory_tags.base_builder_parent import BuilderBaseParent, BytesIO
from src.mcnbt.factory_tags.builder_long import BuilderLong
from src.mcnbt.factory_tags.tags.tag_long_array import LongArray


class BuilderLongArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(LongArray, name)

    def append_buffer(self, buffer: BytesIO, stack=None):
        length = self.get_len_children()
        for i in range(length):
            tag = BuilderLong(str(i))
            tag.insert_value(buffer)
            self.append(tag)
        return True