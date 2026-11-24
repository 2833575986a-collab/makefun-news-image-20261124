from PIL import Image, ImageDraw, ImageFont
W=H=1024
F='/usr/share/fonts/truetype/noto/'
def f(n,s): return ImageFont.truetype(F+n,s)
B=f('NotoSans-Bold.ttf',1); 
img=Image.new('RGB',(W,H),(246,243,236)); d=ImageDraw.Draw(img)
d.rectangle([0,0,W,118],fill=(18,24,38))
d.text((36,18),"THE WORLD ON",font=f('NotoSans-Bold.ttf',26),fill=(200,170,90))
d.text((36,46),"TUESDAY 24 NOVEMBER 2026",font=f('NotoSans-Black.ttf',52),fill=(255,255,255))
stories=[
 ((190,40,40),"UKRAINE / LIBYA","Fallout from Ukraine's drone strike\non Russian warship in Benghazi:\nUN warns Libya must not become\na battleground; east seeks UN probe","ship"),
 ((30,110,70),"MARKETS / TECH","SK hynix jumps ~20% after Nvidia\nreinstates Jensen Huang as CEO;\nTrump says he persuaded the board,\nUS lawmakers push back","chart"),
 ((40,80,160),"ENERGY","Oil falls about 3% as Gulf\nshipping returns to normal and a\nLibyan pipeline reopens; Seoul\nseeks Qatari LNG","barrel"),
 ((200,110,20),"UKRAINE","Drone debris sets fire in central\nKyiv; injured include a foreign\nnational, as Russian strikes\non the capital region continue","drone"),
 ((120,60,140),"INDONESIA","Major factory fire: casualties\nreported and workers missing\nas rescue teams search the site","fire"),
 ((90,90,90),"CLIMATE","Recriminations after COP31 in\nAntalya ended with no deal on\nfossil fuels; Saudi role in the\nfailed talks under scrutiny","globe"),
]
cw,ch=480,272; x0,y0=24,140; gap=16
def icon(kind,cx,cy,c):
    if kind=="ship":
        d.polygon([(cx-60,cy),(cx+60,cy),(cx+40,cy+25),(cx-40,cy+25)],fill=c); d.rectangle([cx-10,cy-30,cx+15,cy],fill=c)
        d.line([(cx+5,cy-30),(cx+5,cy-55)],fill=c,width=4)
        for i in range(3): d.ellipse([cx+20+i*12,cy-50-i*14,cx+44+i*12,cy-26-i*14],fill=(150,150,150))
        d.line([(cx-70,cy+32),(cx+70,cy+32)],fill=(80,130,200),width=4)
    if kind=="chart":
        pts=[(cx-60,cy+30),(cx-30,cy+15),(cx,cy+22),(cx+25,cy-5),(cx+60,cy-40)]
        d.line(pts,fill=c,width=8); d.polygon([(cx+60,cy-40),(cx+38,cy-38),(cx+58,cy-18)],fill=c)
        d.line([(cx-70,cy+40),(cx+70,cy+40)],fill=(60,60,60),width=3)
    if kind=="barrel":
        d.rounded_rectangle([cx-35,cy-40,cx+35,cy+40],radius=10,fill=c)
        for yy in (cy-15,cy+15): d.line([(cx-35,yy),(cx+35,yy)],fill=(246,243,236),width=4)
        d.polygon([(cx+50,cy-20),(cx+70,cy-20),(cx+60,cy+5)],fill=(190,40,40))
    if kind=="drone":
        d.rectangle([cx-20,cy-8,cx+20,cy+8],fill=c)
        for sx in (-45,45): d.line([(cx,cy),(cx+sx,cy-15)],fill=c,width=5); d.ellipse([cx+sx-18,cy-20,cx+sx+18,cy-10],outline=c,width=3)
        d.polygon([(cx-20,cy+45),(cx-5,cy+15),(cx+5,cy+30),(cx+15,cy+12),(cx+25,cy+45)],fill=(230,90,30))
    if kind=="fire":
        d.rectangle([cx-55,cy,cx+55,cy+40],fill=(90,90,90))
        d.polygon([(cx-40,cy),(cx-25,cy-50),(cx-10,cy-20),(cx+5,cy-65),(cx+20,cy-25),(cx+35,cy-45),(cx+45,cy)],fill=(230,90,30))
    if kind=="globe":
        d.ellipse([cx-42,cy-42,cx+42,cy+42],outline=c,width=6); d.line([(cx-42,cy),(cx+42,cy)],fill=c,width=4)
        d.ellipse([cx-18,cy-42,cx+18,cy+42],outline=c,width=4)
        d.line([(cx-50,cy+50),(cx+50,cy-50)],fill=(190,40,40),width=7)
for i,(c,tag,txt,k) in enumerate(stories):
    x=x0+(i%2)*(cw+gap); y=y0+(i//2)*(ch+gap)
    d.rounded_rectangle([x,y,x+cw,y+ch],radius=14,fill=(255,255,255),outline=(220,215,205),width=2)
    d.rectangle([x,y+14,x+8,y+ch-14],fill=c)
    d.text((x+24,y+14),tag,font=f('NotoSans-Bold.ttf',24),fill=c)
    icon(k,x+cw-85,y+80,c)
    d.multiline_text((x+24,y+122),txt,font=f('NotoSans-SemiBold.ttf',24),fill=(25,25,30),spacing=6)
d.text((36,H-28),"Events reported on 24 Nov 2026 (any time zone). Compiled from news-agency and broadcaster reports.",font=f('NotoSans-Regular.ttf',17),fill=(90,90,90))
img.save('entry.png',optimize=True)
print(img.size)
