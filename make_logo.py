from PIL import Image, ImageDraw, ImageFilter
src=Image.open('logo-infranettone.png').convert('RGB')
W,H=src.size
px=src.load()
# mask: cavity = everything inside box that is not bread (bread is warm/bright)
mask=Image.new('L',(W,H),0); m=mask.load()
for y in range(125,330):
    for x in range(100,300):
        r,g,b=px[x,y]
        warm = r>120 and r-b>60
        if not warm: m[x,y]=255
# re-mask warm specks (LEDs/cable) not connected to the bread border
from collections import deque
seen=set(); q=deque()
X0,X1,Y0,Y1=100,299,125,329
for x in range(X0,X1+1):
    for y in (Y0,Y1): q.append((x,y))
for y in range(Y0,Y1+1):
    for x in (X0,X1): q.append((x,y))
while q:
    x,y=q.popleft()
    if (x,y) in seen or not(X0<=x<=X1 and Y0<=y<=Y1) or m[x,y]: continue
    seen.add((x,y))
    q.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
for y in range(Y0,Y1+1):
    for x in range(X0,X1+1):
        if (x,y) not in seen: m[x,y]=255
mask=mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
# dark interior fill with slight vertical gradient
fill=Image.new('RGB',(W,H))
d=ImageDraw.Draw(fill)
for y in range(H):
    t=min(max((y-125)/200,0),1)
    d.line([(0,y),(W,y)],fill=(int(38-14*t),int(30-12*t),int(26-10*t)))
out=Image.composite(fill,src,mask.filter(ImageFilter.GaussianBlur(0.8)))
# controller at 4x
S=4
L=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); g=ImageDraw.Draw(L)
def s(*v): return [a*S for a in v]
cx,cy=200,228
body=(38,38,44); edge=(10,10,12); hi=(80,80,92)
# shadow
g.ellipse(s(118,272,282,300),fill=(0,0,0,110))
# grips + body
for dx in (-1,1):
    g.ellipse(s(cx+dx*62-30,cy-28,cx+dx*62+30,cy+52),fill=edge)
g.rounded_rectangle(s(cx-80,cy-40,cx+80,cy+22),radius=34*S,fill=edge)
for dx in (-1,1):
    g.ellipse(s(cx+dx*62-26,cy-24,cx+dx*62+26,cy+48),fill=body)
g.rounded_rectangle(s(cx-76,cy-36,cx+76,cy+18),radius=31*S,fill=body)
# top highlight
g.rounded_rectangle(s(cx-66,cy-32,cx+66,cy-26),radius=3*S,fill=hi)
# d-pad
lx,ly=cx-46,cy-8
g.rounded_rectangle(s(lx-17,ly-6,lx+17,ly+6),radius=2*S,fill=edge)
g.rounded_rectangle(s(lx-6,ly-17,lx+6,ly+17),radius=2*S,fill=edge)
g.rounded_rectangle(s(lx-15,ly-4,lx+15,ly+4),radius=2*S,fill=(62,62,70))
g.rounded_rectangle(s(lx-4,ly-15,lx+4,ly+15),radius=2*S,fill=(62,62,70))
# buttons (colored LEDs like the servers)
rx,ry=cx+46,cy-8
for (bx,by,c) in [(0,-12,(250,200,40)),(12,0,(235,60,50)),(0,12,(70,200,80)),(-12,0,(60,140,240))]:
    g.ellipse(s(rx+bx-7,ry+by-7,rx+bx+7,ry+by+7),fill=edge)
    g.ellipse(s(rx+bx-6,ry+by-6,rx+bx+6,ry+by+6),fill=c)
    g.ellipse(s(rx+bx-4,ry+by-5,rx+bx,ry+by-2),fill=(255,255,255,150))
# sticks
for sx in (cx-20,cx+20):
    g.ellipse(s(sx-12,cy+10-12,sx+12,cy+10+12),fill=edge)
    g.ellipse(s(sx-10,cy+10-10,sx+10,cy+10+10),fill=(55,55,62))
    g.ellipse(s(sx-6,cy+10-6,sx+6,cy+10+6),fill=(30,30,34))
# center: start/select + orange power LED
g.rounded_rectangle(s(cx-16,cy-14,cx-6,cy-10),radius=2*S,fill=(90,90,100))
g.rounded_rectangle(s(cx+6,cy-14,cx+16,cy-10),radius=2*S,fill=(90,90,100))
g.ellipse(s(cx-5,cy-28,cx+5,cy-18),fill=(255,150,30))
L=L.resize((W,H),Image.LANCZOS)
# glow for LED
glow=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(glow).ellipse((cx-9,cy-32,cx+9,cy-14),fill=(255,150,30,120))
out=out.convert('RGBA'); out.alpha_composite(glow.filter(ImageFilter.GaussianBlur(4))); out.alpha_composite(L)
# cable from controller to bottom (like original)
out.convert('RGB').save('logo-gamettone-python-pil.png')
