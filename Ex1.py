def get_input(notes):
    num = 1
    while num <= 3:
        note = float(input(f"Donner note {num}: "))
        if note >= 0 and note <= 20:
            notes.append(note)
            num += 1
        else:
            print("note invalid")


def average(notes):
    return sum(notes) / 3

notes = []
get_input(notes)
avg = average(notes)

if avg >= 16:
    print("Tres bien")
elif avg >= 14:
    print("Bien")
elif avg >= 12:
    print("Passable")
elif avg < 10:
    print("Insuffisant")   