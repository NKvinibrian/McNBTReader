from mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from mcnbt.factory_tags.tags.tag_short import Short


class BuilderShort(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Short, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>h', buffer.read(2))[0]
