def drawline(tick_length,marker=''):
    tick='-'
    line=tick*tick_length
    line=line+""+marker
    print(line)


def drawinterval(center_length):
    if center_length>0:
        print(drawline(center_length-1))
        print(drawline(center_length))
        print(drawline(center_length-1))

def drawruler(inches,rule_len):
        drawline(rule_len,'0')
        for i in range(1,inches+1):
            drawinterval(rule_len-1)
            drawline(rule_len,str(i))

        
    
print(drawruler(3,4))
        
