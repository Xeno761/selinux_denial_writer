#XenoOP © Copyright
from sys import argv

logs = open(argv[1], "r").readlines()
avc_list = []

for lines in logs:
    if 'avc:' in lines and 'denied' in lines and 'tcontext' in lines:
        avc_list.append(lines)

fix = []

for xeno in avc_list:
    allow1 = xeno.split('scontext=u:r:')[1].split(':')[0]
    allow2 = xeno.split('scontext=u:r:')[1].split(':')[3]
    allow3 = xeno.split('tclass=')[1].split()[0]
    allow4 = xeno.split('denied')[1].split('for')[0].strip()

    tcontext = None
    if 'object_r:' in xeno:
        tcontext = xeno.split('object_r:')[1].split(':s0')[0]
    elif 'tcontext=u:r:' in xeno:
        tcontext = xeno.split('tcontext=u:r:')[1].split(':s0')[0]

    if tcontext:
        fix.append(f'allow {allow1} {tcontext} ({allow3} {allow4})')

fix = list(dict.fromkeys(fix))

for xeno in fix:
    print("(" + xeno.replace("{ ", "(").replace(" }", ")") + ")")
