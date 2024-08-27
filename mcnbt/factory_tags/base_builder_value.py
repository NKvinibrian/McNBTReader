from mcnbt.factory_tags.base_builder import BuilderBase
from io import BytesIO


class BuilderBaseValue(BuilderBase):

    def __init__(self, class_addr: any, name: str):
        super().__init__(class_addr, name)

    def insert_value(self, buffer: BytesIO):
        raise NotImplemented('This method is abstract')

