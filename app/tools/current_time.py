from datetime import datetime


def get_current_time():

    # Get current system time
    now = datetime.now()

    # Format time nicely
    current_time = now.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return (
        f"Current Time: {current_time}"
    )