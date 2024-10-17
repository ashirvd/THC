from config import Config
from utils import DataUtils

class AvgLeadTimeFromWorkBaseTop10:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters for department, account name, and record flag.
        """
        # Use the apply_combined_filters method to combine department and account name filters
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        return DataUtils.filter_record_flag(df, Config.RECORD_FLAG)

    @staticmethod
    def avg_lead_time_from_work_base_top_10_test():
        """
        Calculate the top 10 work bases by average lead time without a date filter.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLeadTimeFromWorkBaseTop10.apply_filters(df)
        top_10_work_bases = DataUtils.avg_lead_time_from_work_base_top_10(filtered_df)

        print("Top 10 Work Bases by Average Lead Time:")
        print(top_10_work_bases.to_string(index=False))

    @staticmethod
    def avg_lead_time_from_work_base_top_10_test_with_date_filter():
        """
        Calculate the top 10 work bases by average lead time with a date filter applied.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLeadTimeFromWorkBaseTop10.apply_filters(df)
        date_filtered_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        top_10_work_bases = DataUtils.avg_lead_time_from_work_base_top_10(date_filtered_df)

        print(f"Top 10 Work Bases by Average Lead Time from {Config.DATE_FROM} to {Config.DATE_TO}:")
        print(top_10_work_bases.to_string(index=False))
