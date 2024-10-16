# tests/total_cost.py

from config import Config
from utils import DataUtils

class TotalCostTest:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        total_cost, formatted_total = DataUtils.calculate_total_cost(steps_count_df)
        print(f"Total Cost: {total_cost} ({formatted_total})")


class TotalCostTestWithDateFilter:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply relevant filters (including date filter)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Apply date filter
        date_filtered_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)

        # Calculate total cost
        total_cost, formatted_total = DataUtils.calculate_total_cost(date_filtered_df)

        # Display the results
        print(f"Total Cost: {total_cost} ({formatted_total})")

