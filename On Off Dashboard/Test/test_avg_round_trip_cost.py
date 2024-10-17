from config import Config
from utils import DataUtils

class AvgRoundTripCost:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters (department, account name) and then apply record flag and steps count filters.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        df = DataUtils.filter_record_flag(df, Config.RECORD_FLAG)
        return DataUtils.filter_steps_count(df, Config.STEPS_COUNT)

    @staticmethod
    def avg_round_trip_cost_test():
        """
        Calculates the average round trip cost without date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgRoundTripCost.apply_filters(df)
        avg_round_trip_cost = DataUtils.avg_round_trip_cost(filtered_df)
        print(f"Average Round Trip Cost: {avg_round_trip_cost}")

    @staticmethod
    def avg_round_trip_cost_test_with_date_filter():
        """
        Calculates the average round trip cost with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = AvgRoundTripCost.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        avg_round_trip_cost = DataUtils.avg_round_trip_cost(booking_date_df)
        print(f"Average Round Trip Cost with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {avg_round_trip_cost}")
