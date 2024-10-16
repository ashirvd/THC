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
        # Replace invalid values with NaN (ensure numeric conversion handles these correctly)
        df.loc[:, 'layover_hours'] = df['layover_hours'].replace(['NULL', 'NaN', 'None', ''], pd.NA)

        # Convert the column to numeric, coercing invalid values to NaN
        df.loc[:, 'layover_hours'] = pd.to_numeric(df['layover_hours'], errors='coerce')

        # Drop NaN values and calculate the average
        valid_layover_hours = df['layover_hours'].dropna()
        if not valid_layover_hours.empty:
            avg_layover = valid_layover_hours.mean()
        else:
            avg_layover = 0  # Return 0 if no valid layover hours exist

        return round(avg_layover)

    @staticmethod
    def spending_by_trip_type_and_city(df):
        # Ensure the 'total' column is numeric and round the values
        df.loc[:, 'total'] = pd.to_numeric(df['total'], errors='coerce').round()

        # Normalize city names to uppercase to avoid case mismatch
        df.loc[:, 'city'] = df['city'].str.strip().str.upper()

        # Process W2H trips
        print("W2H Trips:")
        for city, city_group in df[df['trip_tag'].str.strip().str.upper() == 'W2H'].groupby('city'):
            total_average_city = 0  # Initialize the total average for the city

            # Calculate work base-level totals and averages for the city
            for work_base, group in city_group.groupby('work_base'):
                total_spending = group['total'].sum()
                record_count = group.shape[0]
                average_spending = total_spending / record_count if record_count > 0 else 0

                # Add to the total average of the city
                total_average_city += average_spending

                # Format and print each work base result
                formatted_total = f"{round(total_spending / 1000, 2)}K" if total_spending >= 1000 else f"{round(total_spending / 1000, 1)}K"
                formatted_average = f"{round(average_spending / 1000, 2)}K" if average_spending >= 1000 else f"{round(average_spending / 1000, 1)}K"
                print(
                    f"    {city.title()} ({work_base}) ({record_count} record{'s' if record_count > 1 else ''}) total is {formatted_total} average is {formatted_average}")

            # Print the Total Average for the city (sum of all work base averages), rounded to 1 decimal place
            formatted_total_average_city = f"{round(total_average_city / 1000, 1)}K" if total_average_city >= 1000 else f"{round(total_average_city / 1000, 1)}K"
            print(f"{city.title()} Total Average is {formatted_total_average_city}")
            print("--------------------------------")

        print("\n========== H2W Trips ==========")

        # Process H2W trips
        for city, city_group in df[df['trip_tag'].str.strip().str.upper() == 'H2W'].groupby('city'):
            total_average_city = 0  # Initialize the total average for the city

            # Calculate work base-level totals and averages for the city
            for work_base, group in city_group.groupby('work_base'):
                total_spending = group['total'].sum()
                record_count = group.shape[0]
                average_spending = total_spending / record_count if record_count > 0 else 0

                # Add to the total average of the city
                total_average_city += average_spending

                # Format and print each work base result
                formatted_total = f"{round(total_spending / 1000, 2)}K" if total_spending >= 1000 else f"{round(total_spending / 1000, 1)}K"
                formatted_average = f"{round(average_spending / 1000, 2)}K" if average_spending >= 1000 else f"{round(average_spending / 1000, 1)}K"
                print(
                    f"    {city.title()} ({work_base}) ({record_count} record{'s' if record_count > 1 else ''}) total is {formatted_total} average is {formatted_average}")

            # Print the Total Average for the city (sum of all work base averages), rounded to 1 decimal place
            formatted_total_average_city = f"{round(total_average_city / 1000, 1)}K" if total_average_city >= 1000 else f"{round(total_average_city / 1000, 1)}K"
            print(f"{city.title()} Total Average is {formatted_total_average_city}")
            print("--------------------------------")

    @staticmethod
    def avg_lead_time_from_work_base_top_10(df):
        """
        Calculates the average lead time in days for each work base,
        excluding 'Annual team' and considering only values greater than 0 and non-null values.
        Returns the top 10 work bases by average lead time.

        Args:
        df (DataFrame): DataFrame containing 'Lead_time_days' and 'work_base' columns.

        Returns:
        DataFrame: A DataFrame summarizing the top 10 work bases by average lead time.
        """
        # Ensure 'Lead_time_days' is numeric and handle non-numeric values
        df.loc[:, 'Lead_time_days'] = pd.to_numeric(df['Lead_time_days'], errors='coerce')

        # Filter out rows where 'work_base' is 'Annual team'
        filtered_df = df[df['work_base'] != 'Annual team']

        # Filter 'Lead_time_days' to include only values greater than 0 and non-null
        valid_lead_times = filtered_df[filtered_df['Lead_time_days'] > 0]

        # Group by 'work_base' and calculate the average lead time
        avg_lead_time = valid_lead_times.groupby('work_base')['Lead_time_days'].mean().reset_index()

        # Round the average lead time to the nearest integer
        avg_lead_time['Lead_time_days'] = avg_lead_time['Lead_time_days'].round().astype(int)

        # Sort the results by average lead time in descending order and take the top 10
        top_10_work_bases = avg_lead_time.sort_values(by='Lead_time_days', ascending=False).head(10)

        return top_10_work_bases

