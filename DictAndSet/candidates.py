required_skills = ['python', 'github', 'linux']

candidates = {
  'anna': {'Java', 'linux', 'windows', 'github', 'python', 'fullstack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'python', 'github',  'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'}
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):   # Checks if skills are a proper
        # superset of required skills.
        interviewees.add(candidate)

print(interviewees)
