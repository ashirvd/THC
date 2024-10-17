# main.py
from Test.test_Almosafer_ID_count import Almosafer
from Test.test_total_cost import TotalCost
from Test.test_avg_one_way_cost import OneWayCost
from Test.test_avg_round_trip_cost import AvgRoundTripCost
from Test.test_avg_lead_time_days import AvgLeadTimeDays
from Test.test_avg_layover_hours import AvgLayoverHours
from Test.test_avg_cost_by_trip import AvgCostByTrip
from Test.test_spending_by_month import TotalSpendingByMonth
from Test.test_spending_by_trip_type_city import SpendingByTripTypeAndCity
from Test.test_avg_lead_time_from_work_base_top_10 import AvgLeadTimeFromWorkBaseTop10

def main():

     print("Running Alomosafer ID Count Test...")
     Almosafer.alomosafer_id_count_test()
     print("\nRunning Alomosafer ID Count with Date Filter Test...")
     Almosafer.alomosafer_id_count_test_with_date_filter()

     print("Running Total Cost Test...")
     TotalCost.total_cost_test()
     print("\nRunning Total Cost with Date Filter Test...")
     TotalCost.total_cost_test_with_date_filter()

     print("Running Average One-Way Cost Test...")
     OneWayCost.avg_one_way_cost_test()
     print("\nRunning Average One-Way Cost with Date Filter Test...")
     OneWayCost.avg_one_way_cost_test_with_date_filter()

     print("Running Average Round Trip Cost Test...")
     AvgRoundTripCost.avg_round_trip_cost_test()
     print("\nRunning Average Round Trip Cost with Date Filter Test...")
     AvgRoundTripCost.avg_round_trip_cost_test_with_date_filter()

     print("Running Average Lead Time in Days without Date Filter...")
     AvgLeadTimeDays.avg_lead_time_days_test()
     print("\nRunning Average Lead Time in Days with Date Filter...")
     AvgLeadTimeDays.avg_lead_time_days_test_with_date_filter()

     print("Running Average Layover Hours without Date Filter...")
     AvgLayoverHours.avg_layover_hours_test()
     print("\nRunning Average Layover Hours with Date Filter...")
     AvgLayoverHours.avg_layover_hours_test_with_date_filter()

     print("Running Average Cost by Trip without Date Filter...")
     AvgCostByTrip.avg_cost_by_trip_test()
     print("\nRunning Average Cost by Trip with Date Filter...")
     AvgCostByTrip.avg_cost_by_trip_test_with_date_filter()

     print("Running test for Total Spending By Month without Date Filter:")
     TotalSpendingByMonth.spending_by_month()
     print("\nRunning test for Total Spending By Month with Date Filter:")
     TotalSpendingByMonth.spending_by_month_with_date_filter()

     print("Calculating Spending by Trip Type and City without Date Filter...")
     SpendingByTripTypeAndCity.spending_by_trip_type_and_city_test()
     print("\nCalculating Spending by Trip Type and City with Date Filter...")
     SpendingByTripTypeAndCity.spending_by_trip_type_and_city_test_with_date_filter()

     print("Calculating Average Lead Time from Work Base (without Date Filter)...")
     AvgLeadTimeFromWorkBaseTop10.avg_lead_time_from_work_base_top_10_test()
     print("\nCalculating Average Lead Time from Work Base (with Date Filter)...")
     AvgLeadTimeFromWorkBaseTop10.avg_lead_time_from_work_base_top_10_test_with_date_filter()


if __name__ == "__main__":
    main()