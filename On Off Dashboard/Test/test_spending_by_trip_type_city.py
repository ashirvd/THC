from config import Config
from utils import DataUtils

class TestSpendingByTripTypeAndCity:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME2)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)

        # Calculate spending for W2H and H2W by city
        DataUtils.spending_by_trip_type_and_city(record_flag_df)

class TestSpendingByTripTypeAndCityWithDateFilter:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME2)
        # Apply the department filter
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        # Apply the account name filter
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        # Apply the record flag filter
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        # Apply the date filter
        booking_date_df = DataUtils.filter_booking_date(record_flag_df, Config.DATE_FROM, Config.DATE_TO)
        # Calculate spending for W2H and H2W by city
        spending_results = DataUtils.spending_by_trip_type_and_city(booking_date_df)

        # Print the results
        print(f"Spending by Trip Type and City from {Config.DATE_FROM} to {Config.DATE_TO}:")
        print(spending_results)
