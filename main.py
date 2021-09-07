import datetime

current_time = datetime.date.today().strftime('%Y-%m-%d')
current_date_list = current_time.split('-')

b_date = input('enter you birthday date in yyyy-mm-dd format: ')
name = input('enter your name legend:  ')

b_date = b_date.split('-')

if current_date_list[1] == b_date[1] and current_date_list[2] == b_date[2]:
    age = int(current_date_list[0]) - int(b_date[0])
    ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th',12: 'th', 13: 'th'}.get(age %10 if not 10 < age <=13 else age %14, 'th')

    print(f"It's {name}'s {age}{ordinal_suffix} Birthday")

else:
    print("today is not your birthday")

