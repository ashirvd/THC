from config import Config
from utils import DataUtils

class TestAvgLayoverHours:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply necessary filters (without date filters)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        # steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Calculate and print the average layover hours
        avg_layover_hours = DataUtils.avg_layover_hours(record_flag_df)
        print(f"Average Layover Hours: {avg_layover_hours}")
