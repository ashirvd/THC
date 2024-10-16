from config import Config
from utils import DataUtils

class TestAvgLeadTimeDays:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)

        # Calculate the average lead time in days
        avg_lead_time = DataUtils.avg_lead_time_days(record_flag_df)
        print(f"Average Lead Time in Days: {avg_lead_time}")

class TestAvgLeadTimeDaysWithDateFilter:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply necessary filters
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)

        # Apply date filter (with booking_date between DATE_FROM and DATE_TO)
        booking_date_df = DataUtils.filter_booking_date(record_flag_df, Config.DATE_FROM, Config.DATE_TO)

        # Calculate the average lead time in days
        avg_lead_time = DataUtils.avg_lead_time_days(booking_date_df)

        # Print the average lead time result
        print(f"Average Lead Time in Days (with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}): {avg_lead_time}")
