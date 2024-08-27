from mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from mcnbt.factory_tags.tags.tag_double import Double


class BuilderDouble(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Double, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>d', buffer.read(8))[0]
