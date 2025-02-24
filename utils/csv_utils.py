import csv
import aiofiles
from typing import List, Dict

# Utility function to read CSV file asynchronously
async def read_csv(file_path: str) -> List[Dict[str, str]]:
    rows = []
    async with aiofiles.open(file_path, mode='r') as f:
        reader = csv.DictReader(await f.read().splitlines())
        for row in reader:
            rows.append(row)
    return rows

# Utility function to write CSV file asynchronously
async def write_csv(file_path: str, data: List[Dict[str, str]], fieldnames: List[str]):
    async with aiofiles.open(file_path, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        await f.write(",".join(fieldnames) + "\n")
        
        for row in data:
            await f.write(",".join([str(row[field]) for field in fieldnames]) + "\n")
