from config import Config
from utils import DataUtils

class SpendingByTripTypeAndCity:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters (department, account name) and other filters like record flag.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        return DataUtils.filter_record_flag(df, Config.RECORD_FLAG)

    @staticmethod
    def spending_by_trip_type_and_city_test():
        """
        Calculate spending by trip type and city without a date filter.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = SpendingByTripTypeAndCity.apply_filters(df)
        DataUtils.spending_by_trip_type_and_city(filtered_df)

    @staticmethod
    def spending_by_trip_type_and_city_test_with_date_filter():
        print(f"Displaying results from {Config.DATE_FROM} to {Config.DATE_TO}...")
        """
        Calculate spending by trip type and city with a date filter applied.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = SpendingByTripTypeAndCity.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        DataUtils.spending_by_trip_type_and_city(booking_date_df)
