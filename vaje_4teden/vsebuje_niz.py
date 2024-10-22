xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']

for ime in xs:
    if ime == "Waldo":
        iscemo_waldota = True
        break
    else:
        iscemo_waldota = False

print(iscemo_waldota)