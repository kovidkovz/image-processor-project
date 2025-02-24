async def build_response(message: str, status, status_code, data=None):
    # Check if the status is a boolean, if not, convert it to a string
    response_status = status if isinstance(status, bool) else str(status)
    
    response = {
        'status': response_status,
        'message': str(message),
        'data'      : None
    }
    
    if data:
        response['data'] = data

    return response, status_code