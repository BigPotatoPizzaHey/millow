from dataclasses import dataclass, field
import re
from pprint import pprint

@dataclass
class RGB:
    r: int
    g: int
    b: int

@dataclass
class HexGrid:
    columns: list[list[RGB]]

    @staticmethod
    def _parse_row(row: str):
        row = row.upper()
        return [code for code in row.split() if re.match(r"([0-9a-fA-F]{3}){1,2}", code)]

    @classmethod
    def parse(cls, data: str):
        rows = data.splitlines()
        height = len(rows)
        width = len(cls._parse_row(rows[0]))
        columns = [[None for _ in range(height)] for _ in range(width)]

        for y, row in enumerate(rows):
            row = cls._parse_row(row)
            assert len(row) == width, f"Inconsistent row length {row!r}"
            for x, code in enumerate(row):
                assert columns[x][y] is None
                columns[x][y] = code
        
        return cls(columns)


print(HexGrid.parse("""\
FFF 000 FAF
EFG abc 012\
"""))
