import csv
from fastapi import UploadFile
from services.image_processor import compress_image
from services.db_handler import insert_product, update_product_status
import os
import aiofiles

async def process_csv(file: UploadFile, request_id: str):
    # Save the uploaded file temporarily
    temp_file = f"temp_{request_id}.csv"
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    # Read and process the CSV file
    async with aiofiles.open(temp_file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            serial_number = row['S. No.']
            product_name = row['Product Name']
            input_urls = row['Input Image Urls'].split(',')

            output_urls = []
            for i, url in enumerate(input_urls):
                output_path = f"app/static/{product_name}_output_{i}.jpg"
                compressed_path = await compress_image(url.strip(), output_path)
                output_urls.append(compressed_path)

            await insert_product(request_id, serial_number, product_name, ",".join(input_urls), ",".join(output_urls))
            await update_product_status(serial_number, "COMPLETED")
    
    os.remove(temp_file)
