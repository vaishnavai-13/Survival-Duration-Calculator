#!/usr/bin/env python
# coding: utf-8

# In[3]:


def cal_survival_duration(age, duration_unit):
    if duration_unit.lower() in ['year', 'years', 'y']:
        return f"You lived for {age} years"
    elif duration_unit.lower() in ['month', 'months', 'm']:
        return f"You lived for {age * 12} months"
    elif duration_unit.lower() in ['week', 'weeks', 'w']:
        return f"You lived for {age * 52} weeks"
    elif duration_unit.lower() in ['day', 'days', 'd']:
        return f"You lived for {age * 365} days"
    elif duration_unit.lower() in ['hour', 'hours', 'h']:
        return f"You lived for {age * 365 * 24} hours"
    elif duration_unit.lower() in ['minute', 'minutes', 'min', 'mins']:
        return f"You lived for {age * 365 * 24 * 60} minutes"
    elif duration_unit.lower() in ['second', 'seconds', 's']:
        return f"You lived for {age * 365 * 24 * 60 * 60} seconds"
    else:
        return "Invalid duration unit"
age = int(input("What's your age?:"))
duration_unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds: ")
survival_duration = cal_survival_duration(age, duration_unit)
print(survival_duration)


# In[ ]:




