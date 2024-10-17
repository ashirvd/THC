from config import Config
from utils import DataUtils


class AvgCostByTrip:
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
    def avg_cost_by_trip_test():
        """
        Calculates the average one-way and round-trip costs without date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        steps_count_df = AvgCostByTrip.apply_filters(df)
        avg_costs = DataUtils.avg_cost_by_trip(steps_count_df)

        print(f"Average One-Way Cost: {avg_costs['avg_one_way_cost']} "
              f"({avg_costs['percentage_one_way']}%)")
        print(f"Average Round Trip Cost: {avg_costs['avg_round_trip_cost']} "
              f"({avg_costs['percentage_round_trip']}%)")

    @staticmethod
    def avg_cost_by_trip_test_with_date_filter():
        """
        Calculates the average one-way and round-trip costs with date filters.
        """
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        steps_count_df = AvgCostByTrip.apply_filters(df)
        booking_date_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)
        avg_costs = DataUtils.avg_cost_by_trip(booking_date_df)

        print(f"From {Config.DATE_FROM} to {Config.DATE_TO},\n"
              f"Average One-Way Cost: {avg_costs['avg_one_way_cost']} "
              f"({avg_costs['percentage_one_way']}%),\n"
              f"Average Round Trip Cost: {avg_costs['avg_round_trip_cost']} "
              f"({avg_costs['percentage_round_trip']}%)")
