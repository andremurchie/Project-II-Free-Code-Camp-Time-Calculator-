def add_time(start, duration, day_week=False):
    
  start_list = start.split(' ') #("11:06","PM")
  start_list_original = start_list[0].split(':') #("11","06") 
    
  start_hours = int(start_list_original[0]) #(11) 
  start_minutes = int(start_list_original[1]) #(06)

  duration_list_original = duration.split(':') #('2','02')
    
  duration_hours = int(duration_list_original[0]) #(2)
  duration_minutes = int(duration_list_original[1]) #(02)

  am_pm = start_list[1] # AM or PM ... depends

    #calculation of minutes
  if start_minutes + duration_minutes < 60:
    new_time_minutes = start_minutes + duration_minutes
  else:
    new_time_minutes = (start_minutes + duration_minutes) % 60
    start_hours += 1

  # add 0 if minutes less than 9, so insted of 10:9 it will be 11:09    
  if new_time_minutes <= 9:
      new_time_minutes = "0" + str(new_time_minutes)
        
  # calculation of hours    
  if start_hours + duration_hours < 12:
      new_time_hours = start_hours + duration_hours
  else:
    new_time_hours = (start_hours + duration_hours) % 12
    
  # fixing a bug
  if new_time_hours == 0:
    new_time_hours = 12
  else:
    new_time_hours = new_time_hours

   #Calculation of days of the week
  changes_days = int(duration_hours / 24)
  if (am_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
    changes_days += 1

  # calculation of AM or PM  
  changes_am_pm = int((start_hours + duration_hours) / 12)
    
  #logical for AM or PM
  if am_pm == "AM":
    if changes_am_pm % 2 == 1: 
      am_pm = "PM" 
  elif am_pm == "PM":
    if changes_am_pm % 2 == 1:
      am_pm = "AM"

  if changes_days == 1:
    new_time = f'{new_time_hours}:{new_time_minutes} {am_pm} (next day)'
  elif changes_days == 0:
    new_time = f'{new_time_hours}:{new_time_minutes} {am_pm}'
  else:
    new_time = f'{new_time_hours}:{new_time_minutes} {am_pm} ({changes_days} days later)'
    
  #Logical for days of the week
                        
  days = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday']
  days_i ={'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6}
                        
  if (day_week):               
    day_week = day_week.capitalize()
    new_day_week_i = int((days_i[day_week] + changes_days) % 7)
    new_day_week = days[new_day_week_i]

    if changes_days == 0:
       new_time = f'{new_time_hours}:{new_time_minutes} {am_pm}, {new_day_week}'

    elif changes_days == 1:  
      new_time = f'{new_time_hours}:{new_time_minutes} {am_pm}, {new_day_week} (next day)'  
    else: 
      new_time = f'{new_time_hours}:{new_time_minutes} {am_pm}, {new_day_week} ({changes_days} days later)'

        
  return new_time
