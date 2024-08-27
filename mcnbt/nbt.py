from io import BytesIO
from gzip import GzipFile

from mcnbt.factory_tags.base_builder import BuilderBase
from mcnbt.factory_tags.builder_byte import BuilderByte
from mcnbt.factory_tags.builder_short import BuilderShort
from mcnbt.factory_tags.builder_int import BuilderInt
from mcnbt.factory_tags.builder_long import BuilderLong
from mcnbt.factory_tags.builder_float import BuilderFloat
from mcnbt.factory_tags.builder_double import BuilderDouble
from mcnbt.factory_tags.builder_byte_array import BuilderArray
from mcnbt.factory_tags.builder_string import BuilderString
from mcnbt.factory_tags.builder_list import BuilderList
from mcnbt.factory_tags.builder_compound import BuilderCompound
from mcnbt.factory_tags.builder_int_array import BuilderIntArray
from mcnbt.factory_tags.builder_long_array import BuilderLongArray

from mcnbt.factory_tags.base_builder_parent import BuilderBaseParent
from mcnbt.factory_tags.base_builder_value import BuilderBaseValue

import struct


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

    # @staticmethod
    # def __read__block__(buffer: BytesIO):
    #     tag_id = struct.unpack('>b', buffer.read(1))[0]
    #     title = ''
    #     if tag_id:
    #         title_length = struct.unpack('>h', buffer.read(2))[0]
    #         title = bytes.decode(struct.unpack(f'>{title_length}s', buffer.read(title_length))[0], 'utf-8')
    #
    #     return tag_id, title

    # Todo: I don't even know what this code does anymore, but it works
    def __build_tree(self, buffer: BytesIO):
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
        tree = self.__build_tree(buffer)
        return tree
