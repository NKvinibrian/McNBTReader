from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent, BytesIO
from mcnbt.factory_tags.tags.tag_int_array import IntArray
from mcnbt.factory_tags.builder_int import BuilderInt

class BuilderIntArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(IntArray, name)


    def append_buffer(self, buffer: BytesIO, stack=None):
        length = self.get_len_children()
        for i in range(length):
            tag = BuilderInt(str(i))
            tag.insert_value(buffer)
            self.append(tag)
        return True