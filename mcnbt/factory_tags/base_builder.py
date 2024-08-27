from io import BytesIO
import struct

class BuilderBase:

    def __init__(self, class_addr: any, name: str):
        self.name = name
        self.tag_class = class_addr
        self.is_parent_tag = False
        self.build()

    def build(self):
        self.tag_class = self.tag_class(self.name)

    @staticmethod
    def read__block(buffer: BytesIO):
        tag_id = struct.unpack('>b', buffer.read(1))[0]
        title = ''
        if tag_id:
            title_length = struct.unpack('>h', buffer.read(2))[0]
            title = bytes.decode(struct.unpack(f'>{title_length}s', buffer.read(title_length))[0], 'utf-8')

        return tag_id, title
