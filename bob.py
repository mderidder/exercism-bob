#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    responses = {'': 'Whatever.',
                 'silence': 'Fine. Be that way!',
                 'upper': 'Whoa, chill out!'}
    what = what.strip()
    state = ''
    if what.isupper():
        state = 'upper'
    if what == '':
        state = 'silence'

    return responses[state]
