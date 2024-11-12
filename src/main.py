from yaml import load, SafeLoader
from yaml.constructor import ConstructorError

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        try:
            data = load(data, Loader=SafeLoader)
        except ConstructorError:
            # This is the default file still which won't load correctly
            data = data.replace("{{ digitalforge('var1') }}", "1") \
                .replace("{{ digitalforge('var2') }}", "2")
            data = load(data, Loader=SafeLoader)

    if data['var1type'] == 'file':
        with open(data['var1'], 'r') as f:
            file_value = float(f.read())
        data['var1'] = file_value

    if data['var2type'] == 'file':
        with open(data['var2'], 'r') as f:
            file_value = float(f.read())
        data['var2'] = file_value

    with open('output.txt', 'w') as f:
        if data['var1'] > data['var2']:
            f.write('True')
            print('True')
        else:
            f.write('False')
            print('False')

if __name__ == '__main__':
    main()
