with open('/Users/nataliephillips/Documents/GitHub/nataliephillips.github.io/week07/dracula.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace ('Dracula', '<strong>Izbicki</strong>')
text = text.replace(' DRACULA', ' <strong>IZBICKI</strong>')
text = text.replace('Count', 'Professor')
text = text.replace(' count', ' professor')
text = text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A', 'I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I')
text = text.replace('<span class="smcap">Dracula</span>', '<span class="smcap"><strong>Izbicki</strong></span>')

text = text.replace('''Dracula
''', ' Izbicki')
text = text.replace('''<p class="letra">
DRACULA.<br />
</p>''', '''<p class="letra">
<strong>IZBICKI</strong>.<br />
</p>''')

text = text.replace('Bram Stoker', 'Natalie Phillips')
text = text.replace('Bram &nbsp; Stoker', 'Natalie &nbsp; Phillips')
with open('izbicki.html', 'w', encoding='utf-8') as c:
    c.write(text)
