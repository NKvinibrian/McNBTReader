from src.mcnbt.factory_tags.base_builder import BuilderBase
from typing import Union
from io import BytesIO
from src.mcnbt.factory_tags.tags.base_tags.baseParent import TagBaseParent
import struct


class BuilderBaseParent(BuilderBase):

    def __init__(self, class_addr: any, name: str):
        super().__init__(class_addr, name)
        self.is_parent_tag = True
        self.aux_count = 0

    def info_of_parent_tag(self, buffer: BytesIO):
        self.tag_class.length = struct.unpack('>i', buffer.read(4))[0]

    def append(self, tag: Union[TagBaseParent, any], stack: list=None):
        self.tag_class.children.append(tag.tag_class)

    def get_children_tag_id(self):
        return self.tag_class.children_tag_id

    def get_len_children(self):
        return self.tag_class.length

    def append_buffer(self, buffer: BytesIO, stack: list=None):
        return None

    def is_list_end(self):
        return False
