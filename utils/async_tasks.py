import asyncio

# Utility function to run tasks asynchronously
async def run_async_tasks(tasks: list):
    # Gather all async tasks and run them concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Check for exceptions and handle them
    for result in results:
        if isinstance(result, Exception):
            print(f"Error during async task execution: {result}")
    
    return results
