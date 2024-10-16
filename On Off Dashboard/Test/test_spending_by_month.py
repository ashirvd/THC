from config import Config
from utils import DataUtils

class TestTotalSpendingByMonth:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Calculate total spending by month (without date filter)
        monthly_spending = DataUtils.total_spending_by_month(steps_count_df)

        # Display the results
        print(monthly_spending)

class TestTotalSpendingByMonthWithDateFilter:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        booking_date_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)

        # Calculate total spending by month
        monthly_spending = DataUtils.total_spending_by_month(booking_date_df)

        # Display the results
        print(monthly_spending)
