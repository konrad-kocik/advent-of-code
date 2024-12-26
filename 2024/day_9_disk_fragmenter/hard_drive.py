from typing import List


class Block:
    def __init__(self, value: str):
        self._value = value

    def __eq__(self, other: str):
        return self._value == other

    def __ne__(self, other: str):
        return self._value != other

    @property
    def value(self) -> str:
        return self._value


def calculate_filesystem_checksum(input_file_path: str) -> int:
    disk_map = _get_disk_map(input_file_path)
    blocks = _convert_to_blocks(disk_map)
    blocks = _fragment(blocks)
    return _calculate_checksum(blocks)


def _get_disk_map(input_file_path: str) -> str:
    with open(input_file_path, 'r') as file:
        return file.readline().strip()


def _convert_to_blocks(disk_map: str) -> List[Block]:
    blocks = []
    file_id = 0

    for block_id, block_size in enumerate(disk_map, start=1):
        if block_id % 2 != 0:
            for _ in range(int(block_size)):
                blocks.append(Block(value=str(file_id)))
            file_id += 1
        else:
            for _ in range(int(block_size)):
                blocks.append(Block(value='.'))

    return blocks


def _fragment(blocks: List[Block]) -> List[Block]:
    for source_block_id in range(len(blocks) - 1, -1, -1):
        source_block = blocks[source_block_id]

        if '.' not in blocks[:source_block_id]:
            break

        if source_block != '.':
            for target_block_id, target_block in enumerate(blocks):
                if target_block == '.':
                    blocks[source_block_id] = Block(value='.')
                    blocks[target_block_id] = source_block
                    break

    return blocks


def _calculate_checksum(blocks: List[Block]) -> int:
    checksum = 0

    for block_id, block in enumerate(blocks):
        if block != '.':
            checksum += block_id * int(block.value)

    return checksum
