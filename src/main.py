from yaml import load, SafeLoader
from yaml.constructor import ConstructorError

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        try:
            data = load(data, Loader=SafeLoader)
        except ConstructorError:
            # This is the default file still which won't load correctly
            data = data.replace("{{ digitalforge('var1') }}", "1") \
                .replace("{{ digitalforge('var2') }}", "2")
            data = load(data, Loader=SafeLoader)



    with open('output.txt', 'w') as f:
        if data['var1'] > data['var2']:
            f.write('True')
            print('True')
        else:
            f.write('False')
            print('False')
