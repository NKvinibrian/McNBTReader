from io import BytesIO
from gzip import GzipFile

from src.mcnbt.factory_tags.base_builder import BuilderBase
from src.mcnbt.factory_tags.builder_byte import BuilderByte
from src.mcnbt.factory_tags.builder_short import BuilderShort
from src.mcnbt.factory_tags.builder_int import BuilderInt
from src.mcnbt.factory_tags.builder_long import BuilderLong
from src.mcnbt.factory_tags.builder_float import BuilderFloat
from src.mcnbt.factory_tags.builder_double import BuilderDouble
from src.mcnbt.factory_tags.builder_byte_array import BuilderArray
from src.mcnbt.factory_tags.builder_string import BuilderString
from src.mcnbt.factory_tags.builder_list import BuilderList
from src.mcnbt.factory_tags.builder_compound import BuilderCompound
from src.mcnbt.factory_tags.builder_int_array import BuilderIntArray
from src.mcnbt.factory_tags.builder_long_array import BuilderLongArray

from src.mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from src.mcnbt.factory_tags.base_builder_value import BuilderBaseValue


tag_list = {
    1: BuilderByte,
    2: BuilderShort,
    3: BuilderInt,
    4: BuilderLong,
    5: BuilderFloat,
    6: BuilderDouble,
    7: BuilderArray,
    8: BuilderString,
    9: BuilderList,
    10: BuilderCompound,
    11: BuilderIntArray,
    12: BuilderLongArray
}


class Nbt:

    @staticmethod
    def __build_tree(buffer: BytesIO):
        initial_tag_id, initial_tag_title = BuilderBase.read__block(buffer)
        if initial_tag_id == 0:
            raise Exception('File initiate with end tag')

        parent_stack = []
        initial_tag: BuilderBaseParent = tag_list[initial_tag_id](initial_tag_title)
        if initial_tag.is_parent_tag:
            initial_tag.info_of_parent_tag(buffer)
            parent_stack.append(initial_tag)
        else:
            raise Exception('Need initiate with a group tag')

        while parent_stack:
            current_parent: BuilderBaseParent = parent_stack[-1]

            tag_id, tag_title = current_parent.read__block(buffer)
            if tag_id == 0 or current_parent.is_list_end():
                parent_stack.pop()
            else:
                tag = tag_list[tag_id](tag_title)
                if tag.is_parent_tag:
                    tag: BuilderBaseParent
                    tag.info_of_parent_tag(buffer)
                    tag.append_buffer(buffer, parent_stack)
                else:
                    tag: BuilderBaseValue
                    tag.insert_value(buffer)
                current_parent.append(tag, parent_stack)
        return initial_tag.tag_class

    def read_file(self, file_path: str):
        file = GzipFile(file_path, mode='rb')
        buffer = BytesIO(file.read())
        file.close()
        return self.__build_tree(buffer)

    def read_buffer(self, buffer: BytesIO):
        return self.__build_tree(buffer)
