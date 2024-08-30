from src.mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from src.mcnbt.factory_tags.tags.tag_long import Long


class BuilderLong(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Long, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>q', buffer.read(8))[0]
