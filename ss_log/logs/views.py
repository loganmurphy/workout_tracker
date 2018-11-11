from django.shortcuts import render

# calculates the next workout based on most recent workout
def gen_next_workout():
    pass

def index(request):
    # do a db lookup for the users workouts
    # hard-coding values temporarily
    context = {
        'user_name': 'Logan',
        'last_three_workouts': [
            {'squat': 'Squat: 3 x 5 @ 240lbs', 'press': 'Press: 3 x 5 @ 112.5lbs'},
            {'squat': 'Squat: 3 x 5 @ 245lbs', 'bench': 'Bench: 3 x 5 @ 170lbs'},
            {'squat': 'Squat: 3 x 5 @ 250lbs', 'press': 'Press: 3 x 5 @ 115lbs'}
        ],
        'next_workout': {'squat': 'Squat: 3 x 5 @ 255lbs', 'bench': 'Bench: 3 x 5 @ 175lbs'}
    }
    return render(request, 'logs/index.html', context)