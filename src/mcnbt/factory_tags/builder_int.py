from src.mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from src.mcnbt.factory_tags.tags.tag_int import Int


class BuilderInt(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Int, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>i', buffer.read(4))[0]
