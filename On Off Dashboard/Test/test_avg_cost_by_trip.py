from config import Config
from utils import DataUtils

class TestAvgCostByTrip:
    def run(self):
        # Load the Excel data
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)

        # Apply necessary filters
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Calculate average costs by trip type without date filters
        avg_costs = DataUtils.avg_cost_by_trip(steps_count_df)

        # Print the results
        print(f"Average One Way Cost: {avg_costs['avg_one_way_cost']}")
        print(f"Average Round Trip Cost: {avg_costs['avg_round_trip_cost']}")
        print(f"Percentage of One Way Trips: {avg_costs['percentage_one_way']}%")
        print(f"Percentage of Round Trip Trips: {avg_costs['percentage_round_trip']}%")