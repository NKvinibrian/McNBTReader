from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from io import BytesIO
import struct
from mcnbt.factory_tags.tags.tag_list import List


class BuilderList(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(List, name)

    def info_of_parent_tag(self, buffer: BytesIO):
        self.tag_class.children_tag_id, self.tag_class.length = struct.unpack('>bi', buffer.read(5))
