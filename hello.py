from datetime import date

today = date.today()

print("Today's date is:", today.strftime("%A, %B %d, %Y"))
print("Every expert was once a beginner. Keep going!")

# Christmas countdown
christmas = date(today.year, 12, 25)
if today > christmas:
    christmas = date(today.year + 1, 12, 25)
days_left = (christmas - today).days

if days_left == 0:
    print("It's Christmas today! Merry Christmas!")
else:
    print("Days until Christmas:", days_left)
