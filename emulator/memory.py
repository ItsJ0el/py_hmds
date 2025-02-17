"""This module deals with reading and writing memory from DeSmuME"""


class Memory:

    """Read and write memory from DeSmuME"""

    def __init__(self, emulator) -> None:
        self.emu = emulator

    def read(self, address: int, size: int, signed: bool) -> int:

        """Read a 1, 2, 4 bytes from an address, signed or not"""

        return self.emu.emu.memory.read(address, address, size, signed)
