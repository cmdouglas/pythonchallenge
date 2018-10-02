from zipfile import ZipFile
import re

with ZipFile('data/channel.zip') as z:

    pattern = r'Next nothing is ([\d]+)'
    comments = []

    # from readme.txt in the zipfile
    nothing = '90052'

    while True:
        info = z.getinfo(nothing + '.txt')
        comments.append(info.comment.decode('utf-8'))
    
        txt = z.read(nothing + '.txt').decode('utf-8')
    
        matches = re.findall(pattern, txt)
    
        if matches:
            nothing = matches[0]    
    
        else:
            break
    
    print(''.join(comments))
