from src.mcnbt.factory_tags.base_builder_value import BuilderBaseValue
from io import BytesIO
import struct

from src.mcnbt.factory_tags.tags.tag_string import String


class BuilderString(BuilderBaseValue):

    def __init__(self, name: str):
        super().__init__(String, name)

    def insert_value(self, buffer: BytesIO):
        string_len = struct.unpack('>h', buffer.read(2))[0]
        self.tag_class.value = bytes.decode(struct.unpack(f'>{string_len}s', buffer.read(string_len))[0], 'utf-8')
