# -*- coding: utf-8 -*-
# email/index.html (nisbiy) -> email-test.html (barcha rasm yo'llari mutloq URL)
base = 'https://yokubjanovichh.github.io/ip2026-email-test/'
h = open('index.html', encoding='utf-8').read()
for old, new in [
    ('src="img/',         'src="' + base + 'img/'),
    ('background="img/',   'background="' + base + 'img/'),
    ("url('img/",          "url('" + base + "img/"),
    ('href="invite.ics"',  'href="' + base + 'invite.ics"'),
]:
    h = h.replace(old, new)
open('email-test.html', 'w', encoding='utf-8').write(h)
print('email-test.html qayta yaratildi')
print('hero-bg mutloq nusxalar:', h.count(base + 'img/hero-bg.jpg'))
print("qolgan nisbiy img/ :", h.count('"img/') + h.count("'img/"))
