# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]

# update recorded damages
conversion = {"M": 1000000, "B": 1000000000}

# This function parses the damages to int.
def update_damages():
    updated_damages = []
    for info in damages:
        if info == "Damages not recorded":
            updated_damages.append(info)
            continue
        unit = info[-1]
        number = info[:-1]
        unit_substitute = conversion[unit]
        updated_damages.append(int(float(number) * unit_substitute))
    return updated_damages


# Aggregated hurricanes data:
hurricanes_list_of_data = list(
    zip(
        names,
        months,
        years,
        max_sustained_winds,
        areas_affected,
        update_damages(),
        deaths,
    )
)

# This function builds a dict of hurricanes data by name:
def build_hurricanes_info():
    hurricanes_information = {}
    for hurricane_data in hurricanes_list_of_data:
        hurricanes_information[hurricane_data[0]] = {
            "Name": hurricane_data[0],
            "Month": hurricane_data[1],
            "Year": hurricane_data[2],
            "Max Sustained Wind": hurricane_data[3],
            "Areas Affected": hurricane_data[4],
            "Damages": hurricane_data[5],
            "Deaths": hurricane_data[6],
        }
    return hurricanes_information


# This function builds a dict of hurricanes by year:
def group_hurricane_info_by_year():
    hurricane_data = build_hurricanes_info()
    hurricanes_information_by_year = {}
    for hurricane_key in hurricane_data:
        hurricane_value = hurricane_data[hurricane_key]
        current_year = hurricane_value["Year"]
        if current_year not in hurricanes_information_by_year:
            hurricanes_information_by_year[current_year] = [hurricane_value]
        else:
            hurricanes_information_by_year[current_year].append(hurricane_value)
    return hurricanes_information_by_year


# This function returns hurricane occurances by area:
def count_area_occurance():
    area_occurances = {}
    for areas_list in areas_affected:
        for area in areas_list:
            if area not in area_occurances:
                area_occurances[area] = 1
            else:
                area_occurances[area] += 1
    return area_occurances


# This function finds the most affected area:
def find_area_most_affected():
    area_occurances = count_area_occurance()
    most_affected_area = ""
    most_affected_area_counter = 0
    for area in area_occurances:
        area_count = area_occurances[area]
        if area_count > most_affected_area_counter:
            most_affected_area = area
            most_affected_area_counter += area_count
    return most_affected_area

# This function finds the hurricane that caused most deaths:
def find_most_deaths():
    hurricanes_data = build_hurricanes_info()
    deaths_counter = 0
    hurricane = ""
    most_deaths = {}
    for hurricane_key in hurricanes_data:
        hurricane_value = hurricanes_data[hurricane_key]
        number_of_deaths = hurricane_value["Deaths"]
        if number_of_deaths > deaths_counter:
            hurricane = hurricane_key
            deaths_counter = number_of_deaths
    most_deaths[hurricane] = deaths_counter
    return most_deaths

mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

# This function categorizes hurricanes by mortality:
def build_hurricane_by_mortality_rating():
    hurricanes_by_mortality_rating = {}
    hurricanes_data = build_hurricanes_info()
    for hurricane_key in hurricanes_data:
        hurricane_value = hurricanes_data[hurricane_key]
        number_of_deaths = hurricane_value["Deaths"]
        for rating in mortality_scale:
            upper_bound = mortality_scale[rating]
            if number_of_deaths <= upper_bound:
                if rating in hurricanes_by_mortality_rating:
                    hurricanes_by_mortality_rating[rating].append(hurricane_value)
                else:
                    hurricanes_by_mortality_rating[rating] = [hurricane_value]
                break
        if number_of_deaths > 10000:
            if 5 in hurricanes_by_mortality_rating:
                hurricanes_by_mortality_rating[5].append(hurricane_value)
            else:
                hurricanes_by_mortality_rating[5] = [hurricane_value]

    return hurricanes_by_mortality_rating

# This function finds the hurricane that caused the greatest damages:
def find_greatest_damage():
    hurricanes_data = build_hurricanes_info()
    greatest_hurricane_damage = {}
    greatest_hurricane = ""
    greatest_cost = 0
    for hurricane_key in hurricanes_data:
        hurricane_value = hurricanes_data[hurricane_key]
        damage = hurricane_value["Damages"]
        if damage != "Damages not recorded" and damage > greatest_cost:
            greatest_cost = damage
            greatest_hurricane = hurricane_value["Name"]
    greatest_hurricane_damage[greatest_hurricane] = greatest_cost
    return greatest_hurricane_damage

damages_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

# This function categorizes hurricanes by damages rating but only those with damages recorded:
def build_hurricane_by_damage_rating():
    hurricanes_by_damage_rating = {}
    hurricanes_data = build_hurricanes_info()
    for hurricane_key in hurricanes_data:
        hurricane_value = hurricanes_data[hurricane_key]
        damages = hurricane_value["Damages"]
        for rating in damages_scale:
            upper_bound = damages_scale[rating]
            if damages != "Damages not recorded" and damages <= upper_bound:
                if rating in hurricanes_by_damage_rating:
                    hurricanes_by_damage_rating[rating].append(hurricane_value)
                else:
                    hurricanes_by_damage_rating[rating] = [hurricane_value]
                break
        if damages != "Damages not recorded" and damages > 50000000000:
            if 5 in hurricanes_by_damage_rating:
                hurricanes_by_damage_rating[5].append(hurricane_value)
            else:
                hurricanes_by_damage_rating[5] = [hurricane_value]

    return hurricanes_by_damage_rating