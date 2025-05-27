def replacer(table: str, input_file: str = './tmp/README.md', output_file: str = 'README.md', reg: str = '<!-- URL -->'):
    with open(input_file, 'r') as f:
        data = f.read()
    data = data.replace(reg, table)
    with open(output_file, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    from script.main import *
    replacer(parser(reader('https://www.idevkit.com/live/1069')))
