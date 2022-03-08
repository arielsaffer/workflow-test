# Using dominate package 

import dominate
from dominate.tags import *

doc = dominate.document(title='This is a page')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in ['home', 'about', 'contact']:
            li(a(i.title(), href='/%s.html' % i))

    with div():
        attr(cls='body')
        p('Beep boop..')

print(doc)
