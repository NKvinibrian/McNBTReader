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
    assert Nbt().read_file(path_file) is not None


@pytest.mark.parametrize(
    ('path_file', 'keys', 'value'),
    (
        ('test/files/level.dat', ['Data', 'Version', 'Name'], '1.19.2'),
    )
)
def test_keys(path_file, keys, value):
    tree = Nbt().read_file(path_file)
    assert tree is not None
    for i in keys:
        tree = tree[i]
    assert tree is not None
    assert tree.value == value
