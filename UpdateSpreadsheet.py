import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


# google drive api config
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('[KEYFILE].json', scope)
client = gspread.authorize(creds)
sheet = client.open("[SHEET TITLE]").sheet1

# addon configure
data = "C:/Program Files (x86)/World of Warcraft/_retail_/WTF/Account/[ACCOUNT_NAME]/SavedVariables/GoldRecorder.lua"
# faction = "Horde"
# server = "Hyjal"

# sheet configure
row = 12
column = 4

# read the file
file = open(data, "r")
lines = file.readlines()
file.close()

# sum the gold and format
total_copper = 0
for line in lines:
	line = line.strip()
	temp_value = re.findall(r'\d+', line)
	for copper in temp_value:
		total_copper += int(copper)

gold = total_copper / 10000

# update the sheet
print("Updating sheet with: " + str(gold))
sheet.update_cell(row, column, gold)