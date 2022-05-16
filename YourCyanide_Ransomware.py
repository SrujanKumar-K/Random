import re
import sys

def fun_deobfucation(match):
    vJXgS="9576308241"
    cFeBw="cqbjytaesfvgnxpdurzlomiwkh"
    XhUeL="MBHIZACLPGOTEQVWSURDYKXNJF"
    index=(match.group(1).split(":"))
    for i in index:
        if i in "cFeBw":
           return (cFeBw[int((index[1].split(",")[0][1::]))])
        if i in "XhUeL":
            return (XhUeL[int((index[1].split(",")[0][1::]))])
        if i in "vJXgS":
            return (vJXgS[int((index[1].split(",")[0][1::]))])


with open(sys.argv[1],"rt") as f:
    code=f.read()

pattern=r"(?<=\%)(\w+\:\~\d+\,\d+)(?=\%)"
de_obfucated=re.sub(pattern,fun_deobfucation,code)

output= de_obfucated.replace("%","")

with open(sys.argv[1]+"_decoded.bin", "wt") as f:
    f.write(output)
