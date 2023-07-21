def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given page and page size in a paginated list.

    Parameters:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the specified page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both 'page' and 'page_size' should be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index

