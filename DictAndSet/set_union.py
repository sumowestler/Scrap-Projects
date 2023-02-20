# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)  # .union method returns a set with all elements
# # of both sets
#
# all_animals_2 = wild_animals.union(farm_animals)  # Can be used both
# # ways.
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals  # another way of using the
# # .union method
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
# meds_to_watch = meds_to_watch.union(interaction)
# meds_to_watch.update(interaction)   # Update allows you to add
# # elements to a set.
# meds_to_watch |= interaction    # another way to use .update.

meds_to_watch.update(*adverse_interactions)  # * can be used before an
# argument to unpack the list or tuple being added to a set.

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
