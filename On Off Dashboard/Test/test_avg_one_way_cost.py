from config import Config
from utils import DataUtils

class OneWayCost:
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
    def avg_one_way_cost_test():
        """
        Test case to calculate the average one-way cost without applying date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = OneWayCost.apply_filters(df)
        avg_one_way_cost = DataUtils.avg_one_way_cost(filtered_df)
        print(f"Average One-Way Cost: {avg_one_way_cost}")

    @staticmethod
    def avg_one_way_cost_test_with_date_filter():
        """
        Test case to calculate the average one-way cost with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = OneWayCost.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        avg_one_way_cost = DataUtils.avg_one_way_cost(booking_date_df)
        print(f"Average One-Way Cost with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {avg_one_way_cost}")
