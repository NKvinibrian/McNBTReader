from typing import Union

from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from io import BytesIO
import struct

from mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent
from mcnbt.factory_tags.tags.tag_list import List


class BuilderList(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(List, name)

    def info_of_parent_tag(self, buffer: BytesIO):
        self.tag_class.children_tag_id, self.tag_class.length = struct.unpack('>bi', buffer.read(5))

    def append(self, tag: Union[TagBaseParent, any], stack: list=None):
        if self.aux_count > self.get_len_children():
            raise OverflowError('')
        super().append(tag)
        self.aux_count += 1

    def is_list_end(self):
        return self.aux_count >= self.get_len_children()

    def append_buffer(self, buffer: BytesIO, stack: list=None):
        stack.append(self)

    def read__block(self, buffer: BytesIO):
        tag_id = self.get_children_tag_id()
        tag_title = self.aux_count
        return tag_id, tag_title
