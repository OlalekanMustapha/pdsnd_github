import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('ENTER THE CITY TO EXPLORE: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
         print('You have entered an invalid city name!')
         city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('ENTER THE MONTH: ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print('You have provided an invalid month')
        month = input('ENTER THE MONTH january, february, ... , june : ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('ENTER THE DAY OF THE WEEK : ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('You have provided an invalid day')
            day = input('ENTER THE DAY OF THE WEEK : ').lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by pd.to_datetime(df['Start Time'])month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('The most common month is: ', months[month-1])

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', day)                    


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_hour)                    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df.mode()['Start Station'][0]
    print('The most commonly used start station: ', commonly_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df.mode()['End Station'][0]
    print('The most commonly used end station: ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print('The most popular trip is from: ', popular_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print("total travel time in hours is: ", total_drip_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean() 
    print("mean travel time in hours is: ", mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try: 
        user_types = df['User Type'].value_counts()
        print("\nUser Type Breakdown:")
        print(user_types)
    except: 
        print("\nNo User type data to display.")

    # TO DO: Display counts of gender
    try:
        user_gender_count = df['Gender'].value_counts()
        print("\nUser Gender Breakdown:")
        print(user_gender_count)
    except:
        print("\nNo Gender data to display.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        year_of_birth_min = df['Birth Year'].min()
        earliest_year_of_birth = int(year_of_birth_min)
        print("\nEarliest Year of Birth: ",earliest_year_of_birth)
        year_of_birth_max = df['Birth Year'].max()
        latest_year_of_birth = int(year_of_birth_max)
        print("Most Recent Year of Birth: ",latest_year_of_birth)
        year_of_birth_mode = df['Birth Year'].mode()
        most_common_year_of_birth = int(year_of_birth_mode )
        print("Most Common Year of Birth: ",most_common_year_of_birth)
    except:
        print("\nNo Birth Year data to display.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at a time"""
    raw = input('\nWould you like to diplay raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break

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
