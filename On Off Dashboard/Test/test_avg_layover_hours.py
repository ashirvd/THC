from config import Config
from utils import DataUtils

class AvgLayoverHours:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters (department, account name) and then apply the record flag filter.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        return DataUtils.filter_record_flag(df, Config.RECORD_FLAG)

    @staticmethod
    def avg_layover_hours_test():
        """
        Calculates the average layover hours without date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLayoverHours.apply_filters(df)
        avg_layover_hours = DataUtils.avg_layover_hours(filtered_df)
        print(f"Average Layover Hours: {avg_layover_hours}")

    @staticmethod
    def avg_layover_hours_test_with_date_filter():
        """
        Calculates the average layover hours with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgLayoverHours.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        avg_layover_hours = DataUtils.avg_layover_hours(booking_date_df)
        print(f"Average Layover Hours with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {avg_layover_hours}")
