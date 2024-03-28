T = int(input("Donner le temps en seconds: "))

hours = T // 3600
minutes = (T - hours * 3600) // 60
secs = (T - hours * 3600 - minutes * 60)

print(f"T = {T} seconds = {hours} heures {minutes} minutes {secs} seconds")