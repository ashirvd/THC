from config import Config
from utils import DataUtils


class TestAvgOneWayCost:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Calculate the average one-way cost
        avg_one_way_cost = DataUtils.avg_one_way_cost(steps_count_df)
        print(f"Average One-Way Cost: {avg_one_way_cost}")

class TestAvgOneWayCostWithDateFilter:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        booking_date_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)

        # Calculate the average one-way cost with date filters applied
        avg_one_way_cost = DataUtils.avg_one_way_cost(booking_date_df)
        print(f"Average One-Way Cost with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {avg_one_way_cost}")
