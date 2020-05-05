

from datetime import datetime


def get_timestamp():
	Unformated_time=datetime.now()
	formatted_time = Unformated_time.strftime("%Y%m%d%H%M%S")
	return formatted_time