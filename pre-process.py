import os

path = 'Docs'
ignore_files = ['_sidebar.md', 'README.md']
rename_paths = []

os.chdir(path)
for root, dirs, files in os.walk('.'):
    menu = []
    if not root == '.':
        menu.append((f"<i>← 返回上级</i>", '/'.join(root.split('/')[:-1]) + '/'))
        menu.append((f"👉<b><u>{root.split('/')[-1]}</u></b>👈<br/><hr>", root + '/'))

    tmp_number = []
    for file in files:
        if file.endswith('.md') and file not in ignore_files:
            if ' ' in file:
                rename_paths.append(os.path.join(root, file))
            try:
                assert '.' in file.rstrip('.md')
                num = int(file.rstrip('.md').split('.')[0])
                tmp_number.append((num, file))
            except:
                menu.append(('▶ ' + file.rstrip('.md').replace(' ', '&nbsp;'),
                             os.path.join(root, file.rstrip('.md').replace(' ', '_'))))
    tmp_number.sort()
    for file in tmp_number:
        name = "".join(file[1].rstrip('.md').split('.')[1:]).strip()
        menu.append(('▶ ' + name.replace(' ', '&nbsp;'),
                     os.path.join(root, file[1].rstrip('.md').replace(' ', '_'))))

    tmp_number = []
    for dir_ in dirs:
        if ' ' in dir_:
            rename_paths.append(os.path.join(root, dir_))
        try:
            assert '.' in dir_
            num = int(dir_.split('.')[0])
            tmp_number.append((num, dir_))
        except:
            menu.append((dir_.replace(' ', '&nbsp;') + '/',
                         os.path.join(root, dir_.replace(' ', '_')) + '/'))
    tmp_number.sort()
    for dir_ in tmp_number:
        name = "".join(dir_[1].split('.')[1:]).strip()
        menu.append((name.replace(' ', '&nbsp;') + '/',
                     os.path.join(root, dir_[1].replace(' ', '_')) + '/'))

    with open(os.path.join(root, '_sidebar.md'), 'w', encoding='utf-8') as f:
        for menu in menu:
            f.write(f'* [{menu[0]}]({menu[1]})\n')

for path in rename_paths:
    os.rename(path, path.replace(' ', '_'))
