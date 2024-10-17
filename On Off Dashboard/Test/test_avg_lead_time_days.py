from config import Config
from utils import DataUtils

class AvgLeadTimeDays:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters (department, account name) and then apply the record flag filter.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        return DataUtils.filter_record_flag(df, Config.RECORD_FLAG)

    @staticmethod
    def avg_lead_time_days_test():
        """
        Calculates the average lead time in days without date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLeadTimeDays.apply_filters(df)
        avg_lead_time = DataUtils.avg_lead_time_days(filtered_df)
        print(f"Average Lead Time in Days: {avg_lead_time}")

    @staticmethod
    def avg_lead_time_days_test_with_date_filter():
        """
        Calculates the average lead time in days with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLeadTimeDays.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        avg_lead_time = DataUtils.avg_lead_time_days(booking_date_df)
        print(f"Average Lead Time in Days (with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}): {avg_lead_time}")
