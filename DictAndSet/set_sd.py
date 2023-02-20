# The symmetric difference is the opposite of intersection.
#
# It produces the set of items that are in one set, or the other, but
# not in both.

morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses = morning ^ afternoon
print(possible_courses)
# Can also be used for lists.

morning_list = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon_list = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_course = set(morning_list).symmetric_difference(afternoon_list)
# you can pass any iterable to the method.
print(possible_course)