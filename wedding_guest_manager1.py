# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
waitlist = ["Ken", "Jack", "Ivy"]
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 4
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 5
is_charlie_in_confirmed_guests ="Charlie" in confirmed_guests
print("\n\nStage 5")
print("is_charlie_in_confirmed_guests: ", is_charlie_in_confirmed_guests)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"is it {is_charlie_in_confirmed_guests} that charlie is in the list")

# Stage 6
confirmed_guests.append(waitlist.pop(0))
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 7
confirmed_guests.append("Jack")
confirmed_guests.append("Ivy")
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 9
last_three_guest_on_the_confirmed_guests = (confirmed_guests[-3::])
print("\n\nStage 9")
print("last_three_guest_on_the_confirmed_guests: ", last_three_guest_on_the_confirmed_guests)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 10
MAX_LEN_OF_CONFIRMED_GUEST = 10 + 5
free_slots_in_guestlist = MAX_LEN_OF_CONFIRMED_GUEST - len(confirmed_guests)
confirmed_guests.extend(waitlist[:free_slots_in_guestlist])
waitlist =waitlist[free_slots_in_guestlist:]
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 11
no_of_confirmed_guest = (len(confirmed_guests))
print("\n\nStage 11")
print("no_of_confirmed_guest: ", no_of_confirmed_guest)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 12
confirmed_guests.sort()
print("\n\nStage 12")
# print(confirmed_guests)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 13
confirmed_guests[3] = "Collins"
confirmed_guests.remove("Noah")
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 14
guests_list_for_caterer = confirmed_guests.copy()
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("guests_list_for_caterer: ", guests_list_for_caterer)

# Stage 15
waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)