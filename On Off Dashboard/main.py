# main.py
from Test.test_Almosafer_ID_count import AlomosaferIDCountTest, AlomosaferIDDateCountTest
from Test.test_total_cost import TotalCostTest, TotalCostTestWithDateFilter
from Test.test_avg_one_way_cost import TestAvgOneWayCost, TestAvgOneWayCostWithDateFilter
from Test.test_avg_round_trip_cost import TestAvgRoundTripCost, TestAvgRoundTripCostWithDateFilter
from Test.test_avg_lead_time_days import TestAvgLeadTimeDays, TestAvgLeadTimeDaysWithDateFilter
from Test.test_avg_layover_hours import TestAvgLayoverHours, TestAvgLayoverHoursWithDateFilter
from Test.test_avg_cost_by_trip import TestAvgCostByTrip, TestAvgCostByTripWithDateFilter
from Test.test_spending_by_month import TestTotalSpendingByMonth, TestTotalSpendingByMonthWithDateFilter
from Test.test_spending_by_trip_type_city import TestSpendingByTripTypeAndCity, TestSpendingByTripTypeAndCityWithDateFilter
from Test.test_avg_lead_time_from_work_base_top_10 import TestAvgLeadTimeFromWorkBaseTop10, TestAvgLeadTimeFromWorkBaseTop10WithDateFilter

def main():
     print("Running Alomosafer ID Count Test...")
     AlomosaferIDCountTest().run()
     print("\nRunning Alomosafer ID Count with Date Filter Test...")
     AlomosaferIDDateCountTest().run()

     print("\nRunning Total Cost Test...")
     TotalCostTest().run()
     print("\nRunning Total Cost with Date Filter Test...")
     TotalCostTestWithDateFilter().run()

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

     print("\nRunning Average Lead Time From Work Base - Top 10 ...")
     TestAvgLeadTimeFromWorkBaseTop10().run()
     print("\nRunning Average Lead Time From Work Base With Date Filter - Top 10 ...")
     TestAvgLeadTimeFromWorkBaseTop10WithDateFilter().run()

     print("\nRunning Total Spending By Trip ...")
     TestSpendingByTripTypeAndCity().run()
     print("\nRunning Total Spending By Trip With Date Filter ...")
     TestSpendingByTripTypeAndCityWithDateFilter().run()

if __name__ == "__main__":
    main()
