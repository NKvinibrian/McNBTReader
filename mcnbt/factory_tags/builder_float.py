from mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from mcnbt.factory_tags.tags.tag_float import Float


class BuilderFloat(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(Float, name)

    def insert_value(self, buffer: BytesIO):
        self.tag_class.value = struct.unpack('>f', buffer.read(4))[0]
