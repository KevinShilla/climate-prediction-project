import pycountry

def country_to_flag_code(country_name):
    country = pycountry.countries.get(name=country_name)
    if country:
        # Convert to Streamlit flag format :flag-xx:
        return f":flag-{country.alpha_2.lower()}:"
    return None  # Return None if the country is not found

# List of country names from your dataset
countries = ['World', 'Afghanistan', 'Albania', 'Algeria', 'American Samoa',
       'Angola', 'Antarctica', 'Antigua and Barbuda', 'Argentina',
       'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
       'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
       'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso',
       'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
       'Cayman Islands', 'Central African Republic', 'Chad', 'Chile',
       'China', 'Colombia', 'Comoros', 'Congo-Brazzaville',
       'Congo-Kinshasa', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba',
       'Cyprus', 'Czech Republic', 'Côte d’Ivoire', 'Denmark', 'Djibouti',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Eswatini', 'Ethiopia', 'Falkland Islands', 'Faroe Islands',
       'Fiji', 'Finland', 'Former Czechoslovakia',
       'Former Serbia and Montenegro', 'Former U.S.S.R.',
       'Former Yugoslavia', 'France', 'French Guiana', 'French Polynesia',
       'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Germany, East',
       'Germany, West', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
       'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea',
       'Guinea-Bissau', 'Guyana', 'Haiti', 'Hawaiian Trade Zone',
       'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India',
       'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
       'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
       'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Macau',
       'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia',
       'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco',
       'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
       'Netherlands Antilles', 'New Caledonia', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea',
       'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman',
       'Pakistan', 'Palestinian Territories', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
       'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia',
       'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Pierre and Miquelon', 'Saint Vincent/Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
       'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden',
       'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
       'Thailand', 'The Bahamas', 'Timor-Leste', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
       'Turks and Caicos Islands', 'Tuvalu', 'U.S. Pacific Islands',
       'U.S. Territories', 'U.S. Virgin Islands', 'Uganda', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States',
       'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
       'Wake Island', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

# Generate the dictionary
country_flag_emoji = {country: country_to_flag_code(country) for country in countries}

# For custom entries or unmapped countries, manually add placeholders (optional)
custom_flags = {
    'World': ':earth_africa:',  # Example for "World"
    'Former Yugoslavia': None,
    'Hawaiian Trade Zone': None,
    'Palestinian Territories': ':flag-ps:',
}
country_flag_emoji.update(custom_flags)
country_flag_emoji["Bolivia"] = ":flag-bo:"
country_flag_emoji["British Virgin Islands"] = ":flag-vg:"
country_flag_emoji["Brunei"] = ":flag-bn:"
country_flag_emoji["Burma"] = ":flag-mm:"
country_flag_emoji["Congo-Brazzaville"] = ":flag-cg:"
country_flag_emoji["Congo-Kinshasa"] = ":flag-cd:"
country_flag_emoji["Czech Republic"] = ":flag-cz:"
country_flag_emoji["Côte d’Ivoire"] = ":flag-ci:"
country_flag_emoji["Falkland Islands"] = ":flag-fk:"
country_flag_emoji["Former Czechoslovakia"] = ":flag-cz:"
country_flag_emoji["Former Serbia and Montenegro"] = ":flag-rs:" 
country_flag_emoji["Former U.S.S.R."] = ":flag-ru:"  
country_flag_emoji["Former Yugoslavia"] = ":flag-rs:" 
country_flag_emoji["Gambia, The"] = ":flag-gm:"
country_flag_emoji["Germany, East"] = ":flag-de:" 
country_flag_emoji["Germany, West"] = ":flag-de:" 
country_flag_emoji["Iran"] = ":flag-ir:"
country_flag_emoji["Kosovo"] = ":flag-xk:"
country_flag_emoji["Laos"] = ":flag-la:"
country_flag_emoji["Macau"] = ":flag-mo:"
country_flag_emoji["Micronesia"] = ":flag-fm:"
country_flag_emoji["Moldova"] = ":flag-md:"
country_flag_emoji["Netherlands Antilles"] = ":flag-nl:"
country_flag_emoji["North Korea"] = ":flag-kp:"
country_flag_emoji["Reunion"] = ":flag-re:"
country_flag_emoji["Russia"] = ":flag-ru:"
country_flag_emoji["Saint Helena"] = ":flag-sh:"
country_flag_emoji["Saint Vincent/Grenadines"] = ":flag-vc:"
country_flag_emoji["South Korea"] = ":flag-kr:"
country_flag_emoji["Syria"] = ":flag-sy:"
country_flag_emoji["Taiwan"] = ":flag-tw:"
country_flag_emoji["Tanzania"] = ":flag-tz:"
country_flag_emoji["The Bahamas"] = ":flag-bs:"
country_flag_emoji["Turkey"] = ":flag-tr:"
country_flag_emoji["U.S. Pacific Islands"] = ":flag-us:"
country_flag_emoji["U.S. Territories"] = ":flag-us:"
country_flag_emoji["U.S. Virgin Islands"] = ":flag-us:"
country_flag_emoji["Venezuela"] = ":flag-ve:"
country_flag_emoji["Vietnam"] = ":flag-vn:"
country_flag_emoji["Wake Island"] = ":flag-us:"

import pickle

# Save the dictionary to a pickle file
with open("SK/country_flag_emoji.pkl", "wb") as f:
    pickle.dump(country_flag_emoji, f)


# # Example usage in Streamlit
# import streamlit as st

# # Country selection
# selected_country = st.selectbox("Select a country:", list(country_flag_emoji.keys()))

# # Display the flag
# flag = country_flag_emoji[selected_country]
# if flag:
#     st.write(f"The flag of {selected_country} is {flag}")
# else:
#     st.write(f"No flag available for {selected_country}")

