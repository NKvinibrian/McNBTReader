from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from io import BytesIO

from mcnbt.factory_tags.base_builder import BuilderBase
from mcnbt.factory_tags.tags.tag_compound import Compound


class BuilderCompound(BuilderBaseParent):

    def __init__(self, name: str):
        super().__init__(Compound, name)

    def info_of_parent_tag(self, buffer: BytesIO):
        return

    def append(self, tag: BuilderBase, stack=None):
        self.tag_class.children[tag.name] = tag.tag_class

    def append_buffer(self, buffer: BytesIO, stack: list=None):
        stack.append(self)
