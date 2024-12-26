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


def calculate_filesystem_checksum(input_file_path: str, move_whole_files: bool = False) -> int:
    disk_map = _get_disk_map(input_file_path)
    blocks = _convert_to_blocks(disk_map)
    blocks = _fragment(blocks, move_whole_files)
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


def _fragment(blocks: List[Block], move_whole_files: bool) -> List[Block]:
    if move_whole_files:
        return _fragment_by_whole_files(blocks)
    else:
        return _fragment_by_individual_blocks(blocks)


def _fragment_by_whole_files(blocks: List[Block]) -> List[Block]:
    moved_files_ids = []
    file_blocks_ids = []
    file_blocks = []

    for block_id in range(len(blocks) - 1, -1, -1):
        if not _are_empty_blocks_available(blocks, block_id):
            break

        block = blocks[block_id]

        if _was_file_already_moved(block, moved_files_ids):
            continue

        if _is_it_end_of_file(block, file_blocks):
            _move_file(blocks, file_blocks_ids, file_blocks)
            moved_files_ids.append(file_blocks[0].value)
            file_blocks_ids.clear()
            file_blocks.clear()

        if _is_it_file_block(block, file_blocks):
            file_blocks_ids.insert(0, block_id)
            file_blocks.insert(0, block)

    return blocks


def _are_empty_blocks_available(blocks: List[Block], block_id: int) -> bool:
    return '.' in blocks[:block_id]


def _was_file_already_moved(block: Block, moved_files_ids: List[str]) -> bool:
    return block in moved_files_ids


def _is_it_end_of_file(block: Block, file_blocks: List[Block]) -> bool:
    return file_blocks and file_blocks[0].value != block.value


def _move_file(blocks: List[Block], file_blocks_ids: List[int], file_blocks: List[Block]):
    required_target_blocks = ['.'] * len(file_blocks)

    for target_block_id_start in range(0, file_blocks_ids[0]):
        target_blocks = blocks[target_block_id_start:target_block_id_start + len(file_blocks)]

        if target_blocks == required_target_blocks:
            for file_block_id in file_blocks_ids:
                blocks[file_block_id] = Block(value='.')
            blocks[target_block_id_start:target_block_id_start + len(file_blocks)] = file_blocks
            break


def _is_it_file_block(block: Block, file_blocks: List[Block]) -> bool:
    return block != '.' and (not file_blocks or file_blocks[0].value == block.value)


def _fragment_by_individual_blocks(blocks: List[Block]) -> List[Block]:
    for block_id in range(len(blocks) - 1, -1, -1):
        if not _are_empty_blocks_available(blocks, block_id):
            break

        block = blocks[block_id]

        if block != '.':
            _move_block(blocks, block_id, block)

    return blocks


def _move_block(blocks: List[Block], source_block_id: int, source_block: Block):
    for target_block_id, target_block in enumerate(blocks):
        if target_block == '.':
            blocks[source_block_id] = Block(value='.')
            blocks[target_block_id] = source_block
            break


def _calculate_checksum(blocks: List[Block]) -> int:
    checksum = 0

    for block_id, block in enumerate(blocks):
        if block != '.':
            checksum += block_id * int(block.value)

    return checksum
