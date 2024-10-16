# utils.py

import pandas as pd

class DataUtils:
    @staticmethod
    def load_excel(file_path, sheet_name):
        """Loads an Excel file and returns a DataFrame for a specified sheet."""
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Remove leading/trailing spaces and ensure consistent case
        df['Department'] = df['Department'].str.strip().str.lower()
        df['account_name'] = df['account_name'].str.strip().str.lower()
        df['record_flag'] = df['record_flag'].str.strip().str.lower()

        # print("All Records: ", len(df))
        return df

    @staticmethod
    def filter_department(df, departments):
        """Filters the DataFrame for specified department values."""
        departments = [d.lower() for d in departments]
        filtered_df = df[df['Department'].isin(departments)]
        # print("Total Records after Department Filters: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_account_name(df, account_names):
        """Filters the DataFrame for specified account name values."""
        account_names = [d.lower() for d in account_names]
        filtered_df = df[df['account_name'].isin(account_names)]
        # print("Total Records after Account Names Filters: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_record_flag(df, record_flag):
        """Filters the DataFrame for the 'record_flag' column with a specified value."""
        filtered_df = df[df['record_flag'] == record_flag.lower()]
        # print("Total Records after Record Flag Filter: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_steps_count(df, steps_count):
        """Filters the DataFrame for the 'steps_count' column with a specified value."""
        filtered_df = df[df['steps_count'] == steps_count]
        # print("Total Records after Steps Count Filter: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def combine_filters(department_filtered_df, account_filtered_df):
        """Combines department and account name filters."""
        combined_df = department_filtered_df.merge(account_filtered_df, how='inner')
        # print("Combined Records after Department, Account Name, Record Flag and Steps Count Filters: ",len(combined_df))
        return combined_df

    @staticmethod
    def filter_booking_date(df, from_date, to_date):
        """Applies both 'from' and 'to' date filters on 'booking_date' column.
            This line converts the booking_date column to datetime format. The errors='coerce' argument ensures that any invalid or non-parsable date entries will be converted to
            NaT (Not a Time), avoiding potential errors. The use of .loc[:, 'booking_date'] ensures that we modify the DataFrame directly rather than a copy, which helps avoid the
            SettingWithCopyWarning.
            Ensure the booking_date column is in datetime format using .loc
            """
        df.loc[:, 'booking_date'] = pd.to_datetime(df['booking_date'].dt.date, errors='coerce')
        # df.loc[:, 'booking_date'] = pd.to_datetime(df['booking_date'], errors='coerce')
        # print("Records with Date Filters: ", df.to_dict(orient="records"))  # Updated to be JSON-serializable
        # print("Records with Date Filters: ", df['booking_date'].to_dict())
        # print(json.dumps(df, indent=4))
        # print("NAT Records: ", df['booking_date'].isna().sum())  # Shows count of NaT values

        # Filter for 'from' and 'to' dates
        combined_date_filtered = df[(df['booking_date'] >= from_date) & (df['booking_date'] <= to_date)]

        # print("Total Records after Date Filters: ", len(combined_date_filtered))
        return combined_date_filtered

    @staticmethod
    def count_unique_alomosafer_ids(df):
        """Counts distinct Alomosafer IDs in the filtered data."""
        unique_count = df['almosafer_order_ID'].nunique()
        # print(f"Total Distinct Alomosafer IDs: {unique_count}")
        return unique_count

    @staticmethod
    def calculate_total_cost(df):
        """
            Rounds off each value in the 'total' column, sums all values, and rounds the final sum.
            Args:
            df (DataFrame): DataFrame containing the 'total' column.
            Returns:
            float: The rounded final sum of the 'total' column values.
            """
        # Round each value in the 'total' column
        df.loc[:, 'total'] = df['total'].round()

        # Sum the rounded values and then round the final sum
        total_cost = round(df['total'].sum())

        # print(f"Rounded Total Cost: {total_cost}")

        # total_cost = round(df['total'].round().sum())

        # Determine the suffix based on the magnitude of total_cost
        if total_cost >= 1_000_000_000:
            formatted_total = f"{round(total_cost / 1_000_000_000)}B"
        elif total_cost >= 1_000_000:
            formatted_total = f"{round(total_cost / 1_000_000)}M"
        elif total_cost >= 1_000:
            formatted_total = f"{round(total_cost / 1_000)}K"
        else:
            formatted_total = str(total_cost)  # No suffix for values less than 1,000

        return total_cost, formatted_total

    @staticmethod
    def avg_one_way_cost(df):
        """Calculates the average cost for trips with trip_type 'ONEWAY' and formats it with 'K' for values >= 1000."""
        # Filter rows where trip_type is 'ONEWAY'
        oneway_trips = df[df['trip_type'].str.strip().str.upper() == 'ONEWAY']
        # Sum and calculate the average of the 'total' column for ONEWAY trips
        if not oneway_trips.empty:
            avg_cost = oneway_trips['total'].mean()
        else:
            avg_cost = 0  # In case there are no 'ONEWAY' trips
        # Format the average cost
        avg_cost = round(avg_cost, 2)
        if avg_cost >= 1000:
            formatted_avg = f"{round(avg_cost / 1000, 2)}K"
        else:
            formatted_avg = str(avg_cost)
        return formatted_avg

    @staticmethod
    def avg_round_trip_cost(df):
        """Calculates the average cost for trips with trip_type 'ROUNDTRIP' and formats it with 'K' for values >= 1000."""
        # Filter rows where trip_type is 'ROUNDTRIP'
        oneway_trips = df[df['trip_type'].str.strip().str.upper() == 'ROUNDTRIP']

        # Sum and calculate the average of the 'total' column for ROUNDTRIP trips
        if not oneway_trips.empty:
            avg_cost = oneway_trips['total'].mean()
        else:
            avg_cost = 0  # In case there are no 'ROUNDTRIP' trips
        # Format the average cost
        avg_cost = round(avg_cost, 2)
        if avg_cost >= 1000:
            formatted_avg = f"{round(avg_cost / 1000, 2)}K"
        else:
            formatted_avg = str(avg_cost)
        return formatted_avg

    @staticmethod
    def avg_cost_by_trip(df):
        """Calculates the average cost for one-way and round-trip trips and shows the percentage of each."""

        # Filter rows for ONEWAY trips
        oneway_trips = df[df['trip_type'].str.strip().str.upper() == 'ONEWAY']
        # Calculate average cost for ONEWAY trips
        avg_one_way_cost = oneway_trips['total'].mean() if not oneway_trips.empty else 0

        # Filter rows for ROUNDTRIP trips
        round_trip_trips = df[df['trip_type'].str.strip().str.upper() == 'ROUNDTRIP']
        # Calculate average cost for ROUNDTRIP trips
        avg_round_trip_cost = round_trip_trips['total'].mean() if not round_trip_trips.empty else 0

        # Calculate total costs for percentages
        total_cost = avg_one_way_cost + avg_round_trip_cost
        percentage_one_way = (avg_one_way_cost / total_cost * 100) if total_cost > 0 else 0
        percentage_round_trip = (avg_round_trip_cost / total_cost * 100) if total_cost > 0 else 0

        # Round the average costs and percentages
        avg_one_way_cost = round(avg_one_way_cost, 2)
        avg_round_trip_cost = round(avg_round_trip_cost, 2)

        # Format the percentages to whole numbers
        percentage_one_way = round(percentage_one_way)
        percentage_round_trip = round(percentage_round_trip)

        # Format the average costs to one decimal place
        if avg_one_way_cost >= 1000:
            avg_one_way_cost_formatted = f"{avg_one_way_cost / 1000:.2f}K"
        else:
            avg_one_way_cost_formatted = f"{avg_one_way_cost:.2f}"

        if avg_round_trip_cost >= 1000:
            avg_round_trip_cost_formatted = f"{avg_round_trip_cost / 1000:.2f}K"
        else:
            avg_round_trip_cost_formatted = f"{avg_round_trip_cost:.2f}"

        return {
            "avg_one_way_cost": avg_one_way_cost_formatted,
            "avg_round_trip_cost": avg_round_trip_cost_formatted,
            "percentage_one_way": f"{percentage_one_way}",
            "percentage_round_trip": f"{percentage_round_trip}",
        }

    @staticmethod
    def avg_lead_time_days(df):
        """
        Calculates the average lead time in days from the 'Lead_time_days' column,
        considering only values greater than 0 and non-null values.

        Args:
        df (DataFrame): DataFrame containing the 'Lead_time_days' column.

        Returns:
        int: The average lead time in days, rounded to the nearest integer.
        Returns 0 if no valid values exist.
        """
        # Ensure 'Lead_time_days' column is numeric and handle any non-numeric values
        df.loc[:, 'Lead_time_days'] = pd.to_numeric(df['Lead_time_days'], errors='coerce')

        # Filter the column to include only values greater than 0 and non-null
        valid_lead_times = df['Lead_time_days'][(df['Lead_time_days'] > 0) & (df['Lead_time_days'].notnull())]

        # Calculate the average if there are valid lead times
        if not valid_lead_times.empty:
            avg_lead_time = valid_lead_times.mean()
        else:
            avg_lead_time = 0  # Return 0 if no valid lead times exist

        # Return the rounded average lead time as an integer
        return round(avg_lead_time)

    @staticmethod
    def avg_layover_hours(df):
        """Calculates the average layover hours, excluding null values."""
        # Debug: Show raw data for 'layover_hours' before processing
        print(f"Raw Layover Hours (Before Processing):\n{df['layover_hours']}\n")

        # Replace invalid values with NaN (ensure numeric conversion handles these correctly)
        df['layover_hours'] = df['layover_hours'].replace(['NULL', 'NaN', 'None', ''], pd.NA)

        # Convert the column to numeric, coercing invalid values to NaN
        df['layover_hours'] = pd.to_numeric(df['layover_hours'], errors='coerce')

        # Debug: Show processed values for 'layover_hours' after cleaning
        print(f"Processed Layover Hours (After Cleaning):\n{df['layover_hours']}\n")

        # Drop NaN values and calculate the average
        valid_layover_hours = df['layover_hours'].dropna()
        if not valid_layover_hours.empty:
            avg_layover = valid_layover_hours.mean()
        else:
            avg_layover = 0  # Return 0 if no valid layover hours exist

        return round(avg_layover, 2)

    @staticmethod
    def total_spending_by_month(df):
        # Create a copy of the DataFrame to avoid SettingWithCopyWarning
        df = df.copy()

        # Ensure 'booking_date' is in datetime format
        df.loc[:, 'booking_date'] = pd.to_datetime(df['booking_date'], errors='coerce')

        # Extract month and year from 'booking_date' for grouping using .loc[] to avoid SettingWithCopyWarning
        df.loc[:, 'month_year'] = df['booking_date'].dt.to_period('M')

        # Initialize a dictionary to hold total costs by month and trip type
        spending_summary = {
            'month_year': [],
            'oneway_total': [],
            'roundtrip_total': [],
            'total': []  # Add a 'total' key for combined spending
        }

        # Group by 'month_year' and 'trip_type' and sum the 'total' column
        for month, group in df.groupby('month_year'):
            oneway_total = group[group['trip_type'].str.strip().str.upper() == 'ONEWAY']['total'].sum()
            roundtrip_total = group[group['trip_type'].str.strip().str.upper() == 'ROUNDTRIP']['total'].sum()

            # Calculate total spending for the month (oneway + roundtrip)
            total_spending = oneway_total + roundtrip_total

            spending_summary['month_year'].append(month)
            spending_summary['oneway_total'].append(oneway_total)
            spending_summary['roundtrip_total'].append(roundtrip_total)
            spending_summary['total'].append(total_spending)  # Append the total spending

        # Create a summary DataFrame from the spending summary dictionary
        summary_df = pd.DataFrame(spending_summary)

        # Round the totals for 'oneway_total' and 'roundtrip_total'
        summary_df['oneway_total'] = summary_df['oneway_total'].round()
        summary_df['roundtrip_total'] = summary_df['roundtrip_total'].round()

        # Convert the 'total' column to millions and round to 1 decimal place, then append 'M' for millions
        summary_df['total'] = (summary_df['total'] / 1_000_000).round(1).astype(str) + 'M'

        # Remove the DataFrame index for a clean output
        summary_df.reset_index(drop=True, inplace=True)

        return summary_df

    @staticmethod
    def spending_by_trip_type_and_city(df):

        # Ensure the 'total' column is numeric and round the values
        df.loc[:, 'total'] = pd.to_numeric(df['total'], errors='coerce').round()

        # Initialize dictionaries to store results for W2H and H2W
        w2h_summary = {}
        h2w_summary = {}

        # Filter rows for 'W2H' and 'H2W' trips
        w2h_trips = df[df['trip_tag'].str.strip().str.upper() == 'W2H']
        h2w_trips = df[df['trip_tag'].str.strip().str.upper() == 'H2W']

        # Group by city and calculate total spending and count for W2H trips
        for city, group in w2h_trips.groupby('city'):
            total_spending = group['total'].sum()
            record_count = group.shape[0]
            w2h_summary[city] = (total_spending, record_count)

        # Group by city and calculate total spending and count for H2W trips
        for city, group in h2w_trips.groupby('city'):
            total_spending = group['total'].sum()
            record_count = group.shape[0]
            h2w_summary[city] = (total_spending, record_count)

        # Print the results for W2H trips
        print("W2H Trips:")
        for city, (total, count) in w2h_summary.items():
            formatted_total = f"{round(total / 1000, 2)}K" if total >= 1000 else str(total)
            print(f"{city} ({count} record{'s' if count > 1 else ''}) total is {formatted_total}")

        # Print the results for H2W trips
        print("\nH2W Trips:")
        for city, (total, count) in h2w_summary.items():
            formatted_total = f"{round(total / 1000, 2)}K" if total >= 1000 else str(total)
            print(f"{city} ({count} record{'s' if count > 1 else ''}) total is {formatted_total}")
