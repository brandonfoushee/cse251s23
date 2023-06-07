import pickle

with open('../classwork/grades.dat', 'rb') as f:
    person1 = pickle.load(f)
    print(f'{type(person1)}')
    person2 = pickle.load(f)
    print(f'{person2}')
    person3 = pickle.load(f)
    print(f'{person3}')