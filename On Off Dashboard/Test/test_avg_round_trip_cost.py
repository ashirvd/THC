from config import Config
from utils import DataUtils


class TestAvgRoundTripCost:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)

        # Calculate the average round trip cost
        avg_round_trip_cost = DataUtils.avg_round_trip_cost(steps_count_df)
        print(f"Average Round Trip Cost: {avg_round_trip_cost}")
