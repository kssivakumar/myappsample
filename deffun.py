def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)



def print_seconds(hours, minutes, seconds):
    print(60*60 + 3*60 + seconds)

print_seconds(1,2,3)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, remaining_seconds = convert_seconds( 5000)

print(hours, minutes, remaining_seconds)
