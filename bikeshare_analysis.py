import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def choose_city():
    """Ask user to specify a city to analyze
    Returns
    (str) city - name of the city to analyze"""
    city = str(input('choose the city from which you would like to see the data:Chicago,New york or Washington?\n')).lower()
    while city not in ['chicago', 'new york', 'washington']:
        city = input('Invalid input given,Please enter the city Correctly').lower()
    print()
    return city


def choose_month():
    """let's user choose a month for the filter"""
    month = input('Choose month! January, February, March, April, May, or June? Please type the full month name.\n').title()
    while month.title() not in ['January', 'February', 'March', 'April', 'May', 'June']:
        month = input('Well that was something unexpected,Please choose between January, February, March, April, May, or June? Please type the full month name.\n').title()
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = months.index(month) + 1
    print()
    return month


def choose_day():
    """let's user choose a day for the filter"""
    day = str(input('which day?Please type your response as an sunday,monday...\n')).title()
    while day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        day = input('Thats not a day,please make sure you are entering full day name(sunday,monday....)\n').title()
    print()
    return day


def load_data(city):
    """
    Loads data for the specified city and create columns by month,day,hour and common station .

    Args:
        (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data with newly created columns
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['station intersection'] = df['Start Station'] + df['End Station']
    return df


def filter_requirements():
    """Asks user whether about they want to get data filtered
    Return:
    (str)-Filter for the data"""
    time_filter = input('Would you like to filter the data by month, day,by both or not at all? Type "none" for no time filter and both if you want to apply both the options.\n').lower()
    while time_filter not in ['month', 'day', 'both', 'none']:
        time_filter = input('Sorry,enter a valid word that is either month or day or none or both \n').lower()
    print()
    print('-' * 40)
    return time_filter.lower()


def popular_hour(df):
    pop_hour = df['hour'].mode()[0]
    print('Calculating statistics....\n')

    print('The most popular hour of travel is', pop_hour)
    print()


def popular_day(df):
    """Finds and prints the most popular day of travel from """
    day_ofweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    most_popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of week is {}.'.format(most_popular_day))
    print()
    print()


def popular_month(df):
    """prints the most popular month of travel"""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    index_ofmonth = int(df['month'].mode()[0])
    most_popular_month = months[index_ofmonth - 1]
    print('Most popular Month of travel is {}'.format(most_popular_month))
    print()
    print()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('total tarvel trip duration is:', total_duration)

    # display mean travel time
    mean_time = round(df['Trip Duration'].mean())
    print('The average trip duration is:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most popular end station: {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip

    common_start_end = df['station intersection'].mode()[0]
    print('The most popular trip or the most frequent combination of start station and end station trip: {}'.format(common_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays count of females and males on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of different user types is \n', user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def gender_stats(df):
    """Displays statistics on count of gender of Bikeshare users"""
    print('Calculating stats on Gender....\n')
    start_time = time.time()
    gender_count = df['Gender'].value_counts()
    print('count of different genders is\n {}'.format(gender_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def birthyear_stats(df):
    """Display earliest, most recent, and most common year of birth"""
    print('Getting info on Birth year of user .....\n')
    start_time = time.time()
    common_birthyear = df['Birth Year'].mode()[0]
    print('The most common birth year is {}'.format(common_birthyear))
    earliest_birthyear = df['Birth Year'].min()
    print('Oldest user were born on {}'.format(earliest_birthyear))
    recent_birthyear = df['Birth Year'].max()
    print('youngest users were born on {}'.format(recent_birthyear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Prints five lines of data if the user specifies that they would like to.
    After printing five lines,it asks the user if they would like to see five more,
    continuing until they input no."""
    head = 0
    tail = 5
    display = input('Would you like to view individual trip data? Type Yes or No \n').lower()
    while display not in ['yes', 'no']:
        display = input('Sorry, I do not understand your input. Please type yes or no\n').lower()
    if display == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = input('would you like to view more individual trip data? Type Yes or No\n').lower()
        while display_more not in ['yes', 'no']:
            display_more = input('Your input should either yes or no\n').lower()
        while display_more == 'yes':
            head += 5
            tail += 5
            print(df[df.columns[0:-1]].iloc[head:tail])
            display_more = input('would you like to view more individual trip data? Type Yes or No\n').lower()
            while display_more not in ['yes', 'no']:
                display_more = input('Your input should either yes or no\n').lower()
            if display_more == 'no':
                break


def main():

    while True:
        # Asks from user which city they want to choose
        city = choose_city()
        # loads the city file as dataframe
        df = load_data(city)

        preference = filter_requirements()
        if preference == 'none':
            # what is the most popular hour?
            popular_hour(df)
            # what is the most popular day?
            popular_day(df)
            # what is the most popular month?
            popular_month(df)
            # what is count of different types of user?
            user_stats(df)
            # what is stat of most used start and end station?
            station_stats(df)
            # what is total and average duration of trip?
            trip_duration_stats(df)
            if city == 'chicago' or city == 'new york':
                # what is the most recent and earliest birthyear of the user
                birthyear_stats(df)
                # what is male and female user count?
                gender_stats(df)
            # Asks from user whether they want to see individual data
            display_data(df)
        elif preference == 'both':
            day = choose_day()
            month = choose_month()
            df_filtered = df[(df['month'] == month) & (df['day_of_week'] == day.title())]
            # what is the most popular hour?
            popular_hour(df_filtered)
            # what is count of different types of user?
            user_stats(df_filtered)
            # what is stat of most used start and end station?
            station_stats(df_filtered)
            # what is total and average duration of trip?
            trip_duration_stats(df_filtered)
            if city == 'chicago' or city == 'new york':
                # what is the most recent and earliest birthyear of the user
                birthyear_stats(df_filtered)
                # what is male and female user count?
                gender_stats(df_filtered)
            # Asks from user whether they want to see individual data
            display_data(df_filtered)
        elif preference == 'month':
            month = choose_month()
            # filtering the dataframe according to input
            df_filtered = df[(df['month'] == month)]
            # what is the most popular hour?
            popular_hour(df_filtered)
            # what is the most popular day of travel?
            popular_day(df_filtered)
            # what is count of different types of user?
            user_stats(df_filtered)
            # what is stat of most used start and end station?
            station_stats(df_filtered)
            # what is total and average duration of trip?
            trip_duration_stats(df_filtered)
            if city == 'chicago' or city == 'new york':
                 # what is the most recent and earliest birthyear of the user
                birthyear_stats(df_filtered)
                # what is male and female user count?
                gender_stats(df_filtered)
            # Asks from user whether they want to see individual data
            display_data(df_filtered)
        elif preference == 'day':
            day = choose_day()
            # filtering the dataframe according to input
            df_filtered = df[(df['day_of_week'] == day.title())]
            # what is the most popular hour?
            popular_hour(df_filtered)
            # what is the most popular month of travel
            popular_month(df_filtered)
            # what is count of different types of user?
            user_stats(df_filtered)
            # what is stat of most used start and end station?
            station_stats(df_filtered)
            # what is total and average duration of trip?
            trip_duration_stats(df_filtered)
            if city == 'chicago' or city == 'new york':
                # what is the most recent and earliest birthyear of the user
                birthyear_stats(df_filtered)
                # what is male and female user count?
                gender_stats(df_filtered)
            # Asks from user whether they want to see individual data
            display_data(df_filtered)

        # Ask the user whether they want to see five lines or head of the data

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Exiting the program.....')
            break


if __name__ == "__main__":
    main()
