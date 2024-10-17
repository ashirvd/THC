# test_suite.py
import pytest
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


@pytest.mark.run(1)
def test_alomosafer_id_count():
    Almosafer.alomosafer_id_count_test()

@pytest.mark.run(2)
def test_alomosafer_id_count_with_date_filter():
    Almosafer.alomosafer_id_count_test_with_date_filter()


@pytest.mark.run(3)
def test_total_cost():
    TotalCost.total_cost_test()

@pytest.mark.run(4)
def test_total_cost_with_date_filter():
    TotalCost.total_cost_test_with_date_filter()


@pytest.mark.run(5)
def test_avg_lead_time_days():
    AvgLeadTimeDays.avg_lead_time_days_test()

@pytest.mark.run(6)
def test_avg_lead_time_days_with_date_filter():
    AvgLeadTimeDays.avg_lead_time_days_test_with_date_filter()


@pytest.mark.run(7)
def test_avg_layover_hours():
    AvgLayoverHours.avg_layover_hours_test()

@pytest.mark.run(8)
def test_avg_layover_hours_with_date_filter():
    AvgLayoverHours.avg_layover_hours_test_with_date_filter()


@pytest.mark.run(9)
def test_avg_one_way_cost():
    OneWayCost.avg_one_way_cost_test()

@pytest.mark.run(10)
def test_avg_one_way_cost_with_date_filter():
    OneWayCost.avg_one_way_cost_test_with_date_filter()


@pytest.mark.run(11)
def test_avg_round_trip_cost():
    AvgRoundTripCost.avg_round_trip_cost_test()

@pytest.mark.run(12)
def test_avg_round_trip_cost_with_date_filter():
    AvgRoundTripCost.avg_round_trip_cost_test_with_date_filter()


@pytest.mark.run(13)
def test_avg_lead_time_from_work_base_top_10():
    AvgLeadTimeFromWorkBaseTop10.avg_lead_time_from_work_base_top_10_test()

@pytest.mark.run(14)
def test_avg_lead_time_from_work_base_top_10_with_date_filter():
    AvgLeadTimeFromWorkBaseTop10.avg_lead_time_from_work_base_top_10_test_with_date_filter()


@pytest.mark.run(15)
def test_avg_cost_by_trip():
    AvgCostByTrip.avg_cost_by_trip_test()

@pytest.mark.run(16)
def test_avg_cost_by_trip_with_date_filter():
    AvgCostByTrip.avg_cost_by_trip_test_with_date_filter()


@pytest.mark.run(17)
def test_spending_by_trip_type_and_city():
    SpendingByTripTypeAndCity.spending_by_trip_type_and_city_test()

@pytest.mark.run(18)
def test_spending_by_trip_type_and_city_with_date_filter():
    SpendingByTripTypeAndCity.spending_by_trip_type_and_city_test_with_date_filter()


@pytest.mark.run(19)
def test_spending_by_month():
    TotalSpendingByMonth.spending_by_month()

@pytest.mark.run(20)
def test_spending_by_month_with_date_filter():
    TotalSpendingByMonth.spending_by_month_with_date_filter()
