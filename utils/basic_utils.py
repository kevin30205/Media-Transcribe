import datetime


def format_timestamp(seconds):
    """
    Convert a number of seconds into a formatted timestamp.

    Parameters:
    seconds (float): The number of seconds to convert.

    Returns:
    str: The formatted timestamp in the format "HH:MM:SS,mmm".
    """
    # Convert seconds to a timedelta object
    td = datetime.timedelta(seconds=seconds)

    # Extract hours, minutes, seconds, and milliseconds from the timedelta object
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000

    # Format the timestamp as "HH:MM:SS,mmm"
    formatted_timestamp = f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
    
    return formatted_timestamp
