# main.py

from Test.test_Almosafer_ID_count import AlomosaferIDCountTest
from Test.test_Almosafer_ID_count_with_date_filter import AlomosaferIDDateCountTest
from Test.test_total_cost import TotalCostTest
from Test.test_avg_one_way_cost import TestAvgOneWayCost
from Test.test_avg_one_way_cost_with_date_filter import TestAvgOneWayCostWithDateFilter
from Test.test_avg_round_trip_cost import TestAvgRoundTripCost
from Test.test_avg_round_trip_cost_with_date_filter import TestAvgRoundTripCostWithDateFilter
from Test.test_avg_lead_time_days import TestAvgLeadTimeDays
from Test.test_avg_lead_time_days_with_date_filter import TestAvgLeadTimeDaysWithDateFilter
from Test.test_avg_layover_hours import TestAvgLayoverHours
from Test.test_avg_layover_hours_with_date_filter import TestAvgLayoverHoursWithDateFilter
from Test.test_avg_cost_by_trip_with_date_filter import TestAvgCostByTripWithDateFilter
from Test.test_avg_cost_by_trip import TestAvgCostByTrip
from Test.test_spending_by_month_with_date_filter import TestTotalSpendingByMonthWithDateFilter
from Test.test_spending_by_month import TestTotalSpendingByMonth
from Test.test_spending_by_trip import TestSpendingByTripTypeAndCity

def main():
     print("Running Alomosafer ID Count Test...")
     AlomosaferIDCountTest().run()

     print("\nRunning Total Cost Test...")
     TotalCostTest().run()

     print("\nRunning Alomosafer ID Count with Date Filter Test...")
     AlomosaferIDDateCountTest().run()

     print("\nRunning Avg one way cost...")
     TestAvgOneWayCost().run()

     print("\nRunning Avg one way cost with Date Filter Test...")
     TestAvgOneWayCostWithDateFilter().run()

     print("\nRunning Avg Round Trip Cost...")
     TestAvgRoundTripCost().run()

     print("\nRunning Avg Round Trip Cost with Date Filter Test...")
     TestAvgRoundTripCostWithDateFilter().run()

     print("\nRunning Avg Lead Time Days Test...")
     TestAvgLeadTimeDays().run()

     print("\nRunning Avg Lead Time Days with Date Filter Test...")
     TestAvgLeadTimeDaysWithDateFilter().run()

     print("\nRunning Avg Layover Hours Test...")
     TestAvgLayoverHours().run()

     print("\nRunning Avg Layover Hours Test with date filter...")
     TestAvgLayoverHoursWithDateFilter().run()

     print("\nRunning cost by trip with date filter...")
     TestAvgCostByTripWithDateFilter().run()

     print("\nRunning cost by trip...")
     TestAvgCostByTrip().run()

     print("\nRunning total spending by month with date filter ...")
     TestTotalSpendingByMonthWithDateFilter().run()

     print("\nRunning total spending by month ...")
     TestTotalSpendingByMonth().run()

     print("\nRunning total spending by trip ...")
     TestSpendingByTripTypeAndCity().run()


if __name__ == "__main__":
    main()
