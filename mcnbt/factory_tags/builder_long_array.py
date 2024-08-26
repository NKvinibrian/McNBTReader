from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from mcnbt.factory_tags.tags.tag_long_array import LongArray


class BuilderLongArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(LongArray, name)
