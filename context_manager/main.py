import json
from datetime import datetime
from context_manager import ActivityManager

if __name__ == "__main__":
    
    # test class based context manager
    with ActivityManager("new_activity.json") as activity:
        activity_json = {
            "name": "Stelvio",
            "length": "16.36",
            "units": "km",
            "time": "159",
            "time_units": "minutes",
            "date": str(datetime.strptime('2021-08-25','%Y-%m-%d').date())
        }
        json.dump(activity_json, activity)