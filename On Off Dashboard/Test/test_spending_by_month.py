from config import Config
from utils import DataUtils

class TotalSpendingByMonth:
    @staticmethod
    def apply_filters(df):
        """
        Apply combined filters (department, account name) and other filters like record flag and steps count.
        """
        # Use the apply_combined_filters method from DataUtils
        df = DataUtils.apply_combined_filters(df, Config.DEPARTMENTS, Config.ACCOUNT_NAMES)
        df = DataUtils.filter_record_flag(df, Config.RECORD_FLAG)
        return DataUtils.filter_steps_count(df, Config.STEPS_COUNT)

    @staticmethod
    def spending_by_month():
        """
        Calculate total spending by month without applying a date filter.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = TotalSpendingByMonth.apply_filters(df)
        monthly_spending = DataUtils.total_spending_by_month(filtered_df)

        # Display the results
        print("Total Spending by Month:")
        print(monthly_spending)

    @staticmethod
    def spending_by_month_with_date_filter():
        """
        Calculate total spending by month with a date filter applied.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        filtered_df = TotalSpendingByMonth.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(filtered_df, Config.DATE_FROM, Config.DATE_TO)
        monthly_spending = DataUtils.total_spending_by_month(booking_date_df)

        # Display the results
        print(f"Total Spending by Month from {Config.DATE_FROM} to {Config.DATE_TO}:")
        print(monthly_spending)
