from src.mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from src.mcnbt.factory_tags.tags.tag_byte import Byte


class BuilderByte(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Byte, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>b', buffer.read(1))[0]
