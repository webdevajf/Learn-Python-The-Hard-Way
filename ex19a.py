def fit (deadlifts, squats):
    print(f"I do {deadlifts} deadlifts in the first two weeks.")
    print(f"I do {squats} squats in the first two weeks.")
    print("I get my swole on!\n")

def fit_month(deadlifts, squats):
    print("After two rotations of each workout I drop two \nreps from each set and add weight.")
    print(f"I do {deadlifts} deadlifts every month.")
    print(f"I do {squats} squats every month.")
    print("I'm so swole dat you 'can't touch dis'!")

print("Three alternating workouts every week for two weeks: ")
fit (12 * 2 + 10, 12 * 2 + 10)

print("34 reps of each exercise every two weeks: ")
fit (34, 34)

deadlifts = 12 * 2 + 10
squats = 12 + 12 + 10
more_deadlifts =  10 + 8 + 8
more_squats = 10 + 8 * 2

print("Week #1 I do workout B twice and workout A once,\nWeek #2 I do workout B once and workout A twice:")
fit (deadlifts, squats)

print("""Week #1 I do 6 sets of 12 deadlifts and 3 sets of 12 squats,
Week #2 I do 3 sets of 12 deadlifts and 3 sets of 12 squats
and 3 sets of 10 squats: """)
fit (deadlifts, squats)


print("In a month I do workout B 6 times and I do workout A 6 times.")
fit_month (deadlifts + more_deadlifts, squats + more_squats)
