age = int(input('Enter your age: '))
voter_id=True

if age >=18:
    if voter_id:
        print('Right to vote')
    else:
        ('Apply voter ID first')
else:
    print('You cannot vote')