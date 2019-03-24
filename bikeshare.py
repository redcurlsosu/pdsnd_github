import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = [ 'chicago','new york city','washington']
MONTHS = ['january', 'february','march','april','may','june']
DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s take a look at some US bikeshare data!')
    #get user input for city (chicago, new york city, washington).
    while True:
        city = input('What city would you like to see data for? Choose Chicago, New York City, or Washington:  ').lower()
        if city in CITIES:
            break
    #get user input for month (january, february, ... , june)
    print()
    while True:
        month = input('What month would you like to see data for? Choose January, February, March, April, May,  or June:  ').lower()
        if month in MONTHS:
            break
    print()

    # get user input for day of week (monday, tuesday,)
    while True:
        day = input('What day would you like to see data for? Choose Monday, Tuesday, Wednesday, Thursday, or Friday:  ').lower()
        if day in DAYS:
            break
    print()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load data file
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract detail from Start Time, create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    common_month= df['month'].mode()[0]
    print("Most popular start month: ", common_month)

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("Most popular start day: ", common_day)

    #  display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("Most popular start hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most popular start station: ", most_common_start_station)

    #  display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("Most popular end station: ", most_common_end_station)

    #  display most frequent combination of start station and end station trip
    most_comon_start_start_station = df[['Start Station','End Station']].mode()
    print("Most popular start & end station: ",most_common_end_station, " and ", most_common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration_sum = df['Trip Duration'].sum()
    print("Total trip duration: ", duration_sum)

    # display mean travel time
    duration_mean = df['Trip Duration'].mean()
    print("Most common trip duration: ", duration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print("Customers vs. Subscribers:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
        print()

    if 'Gender' in df.columns:
        print("Users by gender:")
        gender_counts = df['Gender'].value_counts()
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
            print()

    # Display earliest, most recent, and most common year of birth
    print("Users by birth year:\n")
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        #earliest birth year
        earliest_birth_year = birth_year.min()
        print('The earliest birth year is: ', earliest_birth_year)
        #most recent birth year
        most_recent_birth_year = birth_year.max()
        print('The most recent birth year is: ', most_recent_birth_year)
        #most common birth year
        most_common_birth_year = birth_year.mode()[0]
        print('The most common birth year is: ', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    # displays raw data at user request
    r=0
    # initial user input
    raw_data = input('\nWould you like see 10 rows of raw data? Enter yes or no.\n')
    while raw_data.lower() =='yes':
        print(df.iloc[r:r+10])
        # advance to next 5 rows
        r += 10
        # continue by user?
        raw_data = input('\nWould you like see 10 more rows of raw data? Enter yes or no.\n')
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
