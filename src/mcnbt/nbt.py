from io import BytesIO
from gzip import GzipFile
from typing import Union, BinaryIO

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
    def __serializer(tree: any):
        if tree is None:
            return None

        if not hasattr(tree, "__iter__"):
            raise Exception('Not group tree')

        tree_stack = [tree]
        parent_stack = [tree]
        while parent_stack:
            node = parent_stack.pop()
            for tag in node.__iter__():
                tree_stack.append(tag)
                if hasattr(tag, "__iter__"):
                    parent_stack.append(tag)

        return tree_stack   # todo: I stop here, test code!!

    @staticmethod
    def __build_tree(buffer: Union[BytesIO, GzipFile, BinaryIO] ):
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

    def read_file(self, file_path: str, fast_mode: bool=True):
        """
        Reads an NBT file in GZIP format.

        This function parses a GZIP-compressed NBT (Named Binary Tag) file and returns its contents as a tree structure.

        :param file_path: str
            The path to the GZIP-compressed NBT file.

        :param fast_mode: bool, optional
            If True, the function reads the file in fast mode, which uses more memory but provides quicker processing.
            If False, the function uses a memory-efficient mode that may be slower.

        :return: Tree
            A tree structure representing the contents of the NBT file.
        """
        file = GzipFile(file_path, mode='rb')
        if fast_mode:
            buffer = BytesIO(file.read())
            file.close()
            return self.__build_tree(buffer)
        else:
            return self.__build_tree(file)

    def read_buffer(self, buffer: BytesIO):
        """
        Reads a Buffer in GZIP-decompressed format.

        This function parses a GZIP-decompressed NBT buffer file and returns its contents as a tree structure.

        :param buffer: BytesIO

        :return: Tree
            A tree structure representing the contents of the NBT file.
        """
        return self.__build_tree(buffer)

    def read_unzip_file(self, file_path: str, fast_mode=True):
        """
        Reads an NBT file in decompressed format.

        This function parses a file NBT (Named Binary Tag) file and returns its contents as a tree structure.

        :param file_path: str
            The path to the NBT file.

        :param fast_mode: bool, optional
            If True, the function reads the file in fast mode, which uses more memory but provides quicker processing.
            If False, the function uses a memory-efficient mode that may be slower.

        :return: Tree
            A tree structure representing the contents of the NBT file.
        """
        file = open(file_path, mode='rb')
        if fast_mode:
            buffer = BytesIO(file.read())
            file.close()
            return self.__build_tree(buffer)
        else:
            return self.__build_tree(file)

    def write_file(self, tree):
        self.__serializer(tree)
