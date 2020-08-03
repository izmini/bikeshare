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
    x = input('Which city are you interested in? \n Chicago: 1 \n New York City: 2 \n Washington: 3 \n')
    if x == "1":
        city = "chicago"
    elif x == "2":
        city = "new york city"
    elif x == "3":
        city = "washington"
    #elif x != 

    print(city)

    # TO DO: get user input for month (all, january, february, ... , june)

    y = input('Which month are you interested in? \n All: 0 \n Jan: 1 \n Feb: 2 \n Mar: 3 \n Apr: 4\n May: 5 \n Jun: 6 \n')
    
    if y == "0":
        month = "all"
    elif y == "1":
        month = "january"
    elif y == "2":
        month = "february"
    elif y == "3":
        month = "march"
    elif y == "4":
        month = "april"
    elif y == "5":
        month = "may"
    elif y == "6":
        month = "june"

    print(month)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    z = input('Which day are you interested in? \n All: 0 \n Mon: 1 \n Tue: 2 \n Wed: 3 \n Thu: 4\n Fri: 5 \n Sat: 6 \n Sun: 7 \n')

    if z == "0":
        day = "all"
    elif z == "1":
        day = "monday"
    elif z == "2":
        day = "tuesday"
    elif z == "3":
        day = "wednesday"
    elif z == "4":
        day = "thursday"
    elif z == "5":
        day = "friday"
    elif z == "6":
        day = "saturday"
    elif z == "7":
        day = "sunday"

    print(day)

    #print('-'*40)
    return city, month, day

city, month, day = get_filters()



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
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#df1 = load_data(city, month, day)
#print(df1)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()
    
    type(popular_month)
    print('The most popular month taveled is {}.\n'.format(popular_month))
    
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()
    
    print('The most popular day taveled is {}.\n'.format(popular_day))
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()
    print('The most popular hour to start to travel is {}.\n'.format(popular_hour))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)
    return popular_month, popular_day, popular_hour

#popular_month, popular_day, popular_hour = time_stats(df1)
#print(months[popular_month])


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()

    print('{} is the most commonly used start station.\n'.format(popular_start_station)) #change the sentencce

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()

    print('{} is the most commonly used end station.\n'.format(popular_end_station))



    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('{} are the most commonly used start and end stations.\n'.format(popular_start_end_stations))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return  popular_start_station,  popular_end_station, popular_start_end_stations

#popular_start_station,  popular_end_station, popular_start_end_stations = station_stats(df1)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_dur = df['Trip Duration'].sum()

    print('The total time traveled was {}.\n'.format(total_trip_dur)) #change


    # TO DO: display mean travel time
    avg_trip_dur = df['Trip Duration'].mean() 

    print('The average travel time was {}.\n'.format(avg_trip_dur)) #change


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return total_trip_dur, avg_trip_dur

#total_trip_dur, avg_trip_dur = trip_duration_stats(df1)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:

        user_type = df['User Type'].value_counts()

        print('The total amount of each user type is:\n{}\n'.format(user_type))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()

    print('The total in each gender are:\n{}\n'.format(gender))

    print('There is no gender information for Washington.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = min(df['Birth Year'])

    print('The earliest birth year is {}.\n'.format(earliest_birth_year))

    recent_birth_year = max(df['Birth Year'])

    print('The most recent birth year is {}.\n'.format(recent_birth_year))

    common_birth_year = df['Birth Year'].mode()

    print('The most common birth year is {}.\n'.format(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return user_type, gender, earliest_birth_year, recent_birth_year, common_birth_year

#user_type, gender, earliest_birth_year, recent_birth_year, common_birth_year = user_stats(df1)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
