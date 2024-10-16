from config import Config
from utils import DataUtils

class TestAvgLeadTimeFromWorkBaseTop10:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply relevant filters (excluding step count)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)

        # Calculate average lead time from work base excluding 'Annual team'
        top_10_work_bases = DataUtils.avg_lead_time_from_work_base_top_10(record_flag_df)

        # Display the results
        print("Top 10 Work Bases by Average Lead Time:")
        print(top_10_work_bases.to_string(index=False))

class TestAvgLeadTimeFromWorkBaseTop10WithDateFilter:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply relevant filters
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)

        # Apply date filter
        date_filtered_df = DataUtils.filter_booking_date(record_flag_df, Config.DATE_FROM, Config.DATE_TO)

        # Calculate average lead time from work base excluding 'Annual team'
        top_10_work_bases = DataUtils.avg_lead_time_from_work_base_top_10(date_filtered_df)

        # Display the results
        print("Top 10 Work Bases by Average Lead Time:")
        print(top_10_work_bases.to_string(index=False))

