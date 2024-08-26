from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from mcnbt.factory_tags.tags.tag_byte_array import ByteArray


class BuilderArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(ByteArray, name)

