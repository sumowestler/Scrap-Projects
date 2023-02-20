from prescription_data import *

trial_patient = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxoban.
for patient in trial_patient:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print("Patient {} is not taking Warfarin".format(patient))
        print("Please remove {} from the trial".format(patient))
    print(patient, prescription)
