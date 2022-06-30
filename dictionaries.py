month_conversions = {
    "Jan": "January", 
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Oct"])
print(month_conversions["Apr"])
print(month_conversions.get("Dec", "Not a valid key!"))         #get(key, default_value) 
print(month_conversions.get("Be", "Not a valid key!"))



