from src.mcnbt.nbt import Nbt
import pytest

files = [
    'test/files/FileTeste.schematic',
    'test/files/FileTeste2.schematic',
    'test/files/level.dat'
]


@pytest.mark.parametrize(
    'path_file',
    (
        files
    )
)
def test_read(path_file):
    tree = Nbt().read_file(path_file)
    assert tree is not None
    stack = Nbt().write_file(tree)
    assert stack is not None





