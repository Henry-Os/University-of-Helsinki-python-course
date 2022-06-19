""" Contains functions for:
1. Converting temperature values from fahrenheit into celsius 
2. Grouping temperature values into 4 classes
"""

def fahr_to_celsius(temp_fahrenheit):
    converted_temp= (temp_fahrenheit - 32)/1.8
    return converted_temp


def temp_classifier(temp_celsius):
    if temp_celsius<-2:
        classifier= 0
    elif temp_celsius>=-2 and temp_celsius< 2:
        classifier= 1
    elif temp_celsius>=2 and temp_celsius< 15:
        classifier= 2
    else:
        classifier= 3
    return classifier