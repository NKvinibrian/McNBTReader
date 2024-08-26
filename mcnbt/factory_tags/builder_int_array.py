from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from mcnbt.factory_tags.tags.tag_int_array import IntArray


class BuilderIntArray(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(IntArray, name)
