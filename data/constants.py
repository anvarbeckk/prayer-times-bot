import csv

with open("./data/cities.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    DATA = list(reader)


cities = [row['name'] for row in DATA]


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


PRAYERS = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]


# api url
GET_TIMES_URL = "http://api.aladhan.com/v1/calendarByCity"


introduction = (
    "As-salamu alaykum! I will remind you when it's time to pray so you "
    "never miss a prayer again!"
    "click <i>/prayer_times</i> to find out prayer times"
)

FIRST_TIME_USER = (
    "Looks like you are a first-time user.\nTo get started, can you "
    "please send me your city name?"
)

see_help = (
    "<b>See /help for more information.</b>"
)

help_message = (
    f"<b>Never miss a prayer again!</b>\nI will remind "
    "you when it's time to pray and can help you keep track of your prayers.\n"
    f"\n<b>Commands</b>\n"
    "<i>/start</i> - initial setup process\n"
    "<i>/help</i> - detailed info on commands and extra notes\n"
    "<i>/prayer_times</i> - get prayer times for the day (will send tomorrow's"
    " prayer times if there are no prayers left for today)\n"
    "is frozen, try running this command)\n\n"
    "If you encounter any issues, please reach out to @anvar1234\n"
)


several_matches = "Which one of these did you mean?"
spelling_mistake = "Did you mean one of these cities: {}?"
pick_option = "Please choose one of the options above."

setup_done = (
    "Great, you are now to set to receive reminders. You can get prayer times "
    "using <b>/prayer_times</b> command."
)
something_wrong = (
    "Something went wrong!. Please try /start again later>"
)

prayer_times = "<b>{}</b>\nHere are your prayer times for today:\n\n{}"
time_to_pray = "Time to pray {}"
sunsire = "Make sure that you pray before sunrise, which is at {}."

registered_first = (
    "You have not set anything up. Please use <b>/start</b> to register now."
)

pie_coordinates = {
    "Fajr": (250, 100),
    "Dhuhr": (250, 240),
    "Asr": (175, 240),
    "Maghrib": (100, 240),
    "Isha": (100, 100),
}

# surah_fatiha = "Bismillah hir rahman nir raheem. Alhamdu lillaahi Rabbil ‘aalameen. Ar-Rahmaanir-Raheem. Maaliki Yawmid-Deen. Iyyaaka na’budu wa lyyaaka nasta’een. Ihdinas-Siraatal-Mustaqeem. Siraatal-lazeena an’amta ‘alaihim ghayril-maghdoobi ‘alaihim wa lad-daaalleen"
