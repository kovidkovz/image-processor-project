from database import database

async def insert_request(request_id: str):
    query = "INSERT INTO requests (request_id, status) VALUES (:request_id, 'PENDING')"
    await database.execute(query, values={"request_id": request_id})

async def get_request_status(request_id: str) -> str:
    query = "SELECT status FROM requests WHERE request_id = :request_id"
    result = await database.fetch_one(query, values={"request_id": request_id})
    return result['status'] if result else None

async def insert_product(request_id, serial_number, product_name, input_urls, output_urls):
    query = """
    INSERT INTO products (request_id, serial_number, product_name, input_image_urls, output_image_urls, status) 
    VALUES (:request_id, :serial_number, :product_name, :input_urls, :output_urls, 'PENDING')
    """
    await database.execute(query, values={
        "request_id": request_id,
        "serial_number": serial_number,
        "product_name": product_name,
        "input_urls": input_urls,
        "output_urls": output_urls
    })

async def mark_request_completed(request_id: str) -> bool:
    query = "UPDATE requests SET status = 'COMPLETED' WHERE request_id = :request_id"
    await database.execute(query, values={"request_id": request_id})
    return True
