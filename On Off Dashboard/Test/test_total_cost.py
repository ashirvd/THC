from config import Config
from utils import DataUtils

class TotalCost:
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
    def total_cost_test():
        """
        Test case to calculate the total cost without applying date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = TotalCost.apply_filters(df)
        total_cost, formatted_total = DataUtils.calculate_total_cost(filtered_df)
        print(f"Total Cost: {total_cost} ({formatted_total})")

    @staticmethod
    def total_cost_test_with_date_filter():
        """
        Test case to calculate the total cost with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = TotalCost.apply_filters(df)
        date_filtered_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        total_cost, formatted_total = DataUtils.calculate_total_cost(date_filtered_df)
        print(f"From {Config.DATE_FROM} to {Config.DATE_TO}, the total cost is {total_cost} ({formatted_total})")
