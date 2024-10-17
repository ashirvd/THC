from config import Config
from utils import DataUtils

class Almosafer:
    @staticmethod
    def apply_filters(df):
        """
        Apply department, account name, record flag, and steps count filters to the DataFrame.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        df = DataUtils.filter_record_flag(df, Config.RECORD_FLAG)
        return DataUtils.filter_steps_count(df, Config.STEPS_COUNT)

    @staticmethod
    def alomosafer_id_count_test():
        """
        Count the total distinct Alomosafer IDs without date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = Almosafer.apply_filters(df)
        alomosafer_count = DataUtils.count_unique_alomosafer_ids(filtered_df)
        print(f"Total Distinct Alomosafer IDs: {alomosafer_count}")

    @staticmethod
    def alomosafer_id_count_test_with_date_filter():
        """
        Count the total distinct Alomosafer IDs with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = Almosafer.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        alomosafer_count = DataUtils.count_unique_alomosafer_ids(booking_date_df)
        print(f"Total Distinct Alomosafer IDs with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {alomosafer_count}")
