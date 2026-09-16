import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
FONT='Nimbus Sans'   # substitute 'Nimbus Sans' at final export
plt.rcParams['font.family']=FONT
plt.rcParams['pdf.fonttype']=42
plt.rcParams['ps.fonttype']=42
plt.rcParams['mathtext.fontset']='custom'
plt.rcParams['mathtext.rm']=FONT
plt.rcParams['mathtext.it']=FONT+':italic'
BLUE=(0.122,0.435,0.706); RED=(0.722,0.122,0.18); GREY='0.45'
# ('R', agent, model, exposure, ref, value, branch, depleted, naprt)
#   naprt: 'Y' measured in that system, '-' not measured
R=[('H','HUMAN SKIN, topical',),
 ('R','Myristyl nicotinate 5%','Forearm','12 wk, 5%','5,6',1.25,'A',False,'\u2014'),
 ('R','Niacinamide 4%','Forearm','8 wk, 4%','5',1.00,'M',False,'\u2014'),
 ('H','MOUSE SKIN, topical',),
 ('R','Myristyl nicotinate','Dorsum','1%, 3 d','70',1.39,'A',False,'\u2014'),
 ('H','CULTURED CELLS, 6 h',),
 ('R','Nicotinic acid','HEK293','5\u201310 \u00b5M','15',2.00,'A',False,'Y'),
 ('R','Nicotinamide','HEK293','20 \u00b5M','15',1.00,'M',False,'Y'),
 ('R','Nicotinamide','HEK293','5 mM','15',1.31,'M',False,'Y'),
 ('R','Nicotinic acid','NHEK','10 \u00b5M','19',1.30,'A',False,'\u2014'),
 ('R','Nicotinic acid + FK866','NHEK','10 \u00b5M','19',1.30,'A',False,'\u2014'),
 ('R','Nicotinic acid mononucleotide','NHEK','30\u2013100 \u00b5M (ns)','19',1.50,'A',False,'\u2014'),
 ('R','Nicotinic acid riboside','NHEK','100 \u00b5M','19',1.10,'A',False,'\u2014'),
 ('R','Nicotinamide','NHEK','100 \u00b5M','19',0.95,'M',False,'\u2014'),
 ('R','Nicotinamide mononucleotide','NHEK','100 \u00b5M','19',1.00,'M',False,'\u2014'),
 ('R','Nicotinamide riboside','NHEK','100 \u00b5M','19',1.00,'M',False,'\u2014'),
 ('H','HUMAN SKELETAL MUSCLE, oral',),
 ('R','Niacin, myopathy patients','Vastus lateralis','750\u20131000 mg/d, 10 mo','22',2.30,'A',True,'\u2014'),
 ('R','Niacin, healthy controls','Vastus lateralis','750\u20131000 mg/d, 4 mo','22',1.00,'A',False,'\u2014'),
 ('R','Nicotinamide riboside','Vastus lateralis','1 g/d, 21 d','23',1.07,'M',False,'\u2014'),
 ('R','Nicotinamide riboside','Vastus lateralis','1 g/d, 6 wk','24',0.91,'M',False,'\u2014'),
 ('H','MOUSE SKELETAL MUSCLE, aged, oral',),
 ('R','Nicotinic acid','Tibialis anterior','5 wk','35',2.70,'A',True,'\u2014'),
 ('R','Nicotinic acid','Soleus','5 wk','35',1.37,'A',True,'\u2014')]
n=len(R); FS=8.0
W=190/25.4; RH=0.205; TOPPAD=0.42; BOTPAD=0.76
SH=0.86                       # strip block height (in)
H=RH*n+SH+TOPPAD+BOTPAD
fig=plt.figure(figsize=(W,H),dpi=300)
XLO,XHI=0.55,2.90
ax=fig.add_axes([0.66,(BOTPAD+SH)/H,0.318,(RH*n)/H])
ax.set_xlim(XLO,XHI); ax.set_ylim(-0.5,n-0.5)
for s in ('top','right','left','bottom'): ax.spines[s].set_visible(False)
ax.set_xticks([]); ax.set_yticks([])

_r=fig.canvas.get_renderer()
def _w(txt,bold=False):
    t=fig.text(0,0,txt,fontsize=FS,fontweight='bold' if bold else 'normal')
    bb=t.get_window_extent(renderer=_r); t.remove()
    return bb.width/(W*fig.dpi)
GAP=0.018; CA=0.010
CM=CA+max(_w('Nicotinic acid mononucleotide'),_w('Niacin, myopathy patients'),_w('Agent',True))+GAP
wM=max([_w(x[2]) for x in R if x[0]=='R']+[_w('Model',True)])
wE=max([_w(x[3]) for x in R if x[0]=='R']+[_w('Exposure',True)])
CE=CM+wM+GAP+wE
CR=CE+GAP+max([_w(x[4]) for x in R if x[0]=='R']+[_w('Ref.',True)])
CN=CR+GAP+max(_w('NAPRT',True),_w('\u2014'))
PL=CN+GAP*1.4
ax.set_position([PL,(BOTPAD+SH)/H,0.978-PL,(RH*n)/H])
def fy(row): return fig.transFigure.inverted().transform(ax.transData.transform((1.0,n-1-row)))[1]
ax.axvline(1.0,color='0.25',lw=1.0,zorder=1)
for i,it in enumerate(R):
    y=fy(i)
    if it[0]=='H':
        fig.text(CA,y,it[1],fontsize=FS,fontweight='bold',va='center'); continue
    _,ag,mo,ex,rf,val,br,dep,nap=it
    col=BLUE if br=='A' else RED
    fig.text(CA,y,ag,fontsize=FS,color=col,va='center')
    fig.text(CM,y,mo,fontsize=FS,color='0.15',va='center')
    fig.text(CE,y,ex,fontsize=FS,color='0.15',va='center',ha='right')
    fig.text(CR,y,rf,fontsize=FS,color='0.15',va='center',ha='right')
    if nap=='Y':
        from matplotlib.lines import Line2D as _L
        fig.add_artist(_L([CN-_w('\u2014')/2],[y],marker='D',ms=3.0,mfc='0.15',mec='0.15',
                          ls='none',transform=fig.transFigure))
    else:
        fig.text(CN,y,nap,fontsize=FS,color='0.55',va='center',ha='right')
    ax.plot(val,n-1-i,marker=('s' if br=='A' else 'o'),ms=4.2,
            mfc=('white' if dep else col),mec=col,mew=1.1,zorder=3)
hy=fy(-1.0)
for lab,cx in (('Agent',CA),('Model',CM)):
    fig.text(cx,hy,lab,fontsize=FS,fontweight='bold',va='center')
for lab,cx in (('Exposure',CE),('Ref.',CR),('NAPRT',CN)):
    fig.text(cx,hy,lab,fontsize=FS,fontweight='bold',va='center',ha='right')
# bracket: the one same-cell, same-day comparison (HEK293 rows 6 and 8)
i1,i2=6,8; xb=2.80
ax.plot([xb-0.06,xb,xb,xb-0.06],[n-1-i1,n-1-i1,n-1-i2,n-1-i2],color=GREY,lw=0.8,
        clip_on=False,zorder=2)
# the bracket is explained in the legend; no inline label
fig.text(PL+(0.978-PL)*((0.80-XLO)/(XHI-XLO)),fy(-0.12),'no change',
         fontsize=FS-0.5,color='0.35',ha='center',va='center')

# ---- strip: the same measurements regrouped by branch and state ----
sx=fig.add_axes([PL,(BOTPAD+0.16)/H,0.978-PL,(SH-0.30)/H])
sx.set_xlim(XLO,XHI); sx.set_ylim(-0.6,2.6)
for s in ('top','right','left'): sx.spines[s].set_visible(False)
sx.spines['bottom'].set_color('0.4')
sx.set_yticks([]); sx.set_xticks([0.6,1.0,1.5,2.0,2.5])
sx.set_xticklabels(['0.6','1.0','1.5','2.0','2.5'],fontsize=FS-0.5,color='0.15')
sx.tick_params(axis='x',length=3,pad=2,color='0.4')
sx.set_xlabel('NAD$^{+}$, fold of control',fontsize=FS-0.5,labelpad=3,color='0.15')
sx.axvline(1.0,color='0.25',lw=1.0,zorder=1)
acid_un=[v for _,*_r2 in [] ] # placeholder
rows=[x for x in R if x[0]=='R']
AU=[x[5] for x in rows if x[6]=='A' and not x[7]]
AD=[x[5] for x in rows if x[6]=='A' and x[7]]
AM=[x[5] for x in rows if x[6]=='M']
BANDS=[('acid branch, unstressed',AU,BLUE,False,2),
       ('acid branch, into a deficit',AD,BLUE,True,1),
       ('amide branch, any state',AM,RED,False,0)]
for lab,vals,col,open_,yy in BANDS:
    tint=tuple(1-(1-c)*0.22 for c in col)
    sx.plot([min(vals),max(vals)],[yy,yy],color=tint,lw=5,solid_capstyle='round',zorder=2)
    for v in vals:
        sx.plot(v,yy,marker=('s' if col is BLUE else 'o'),ms=4.2,
                mfc=('white' if open_ else col),mec=col,mew=1.1,zorder=3)
    fig.text(CA,fig.transFigure.inverted().transform(sx.transData.transform((1.0,yy)))[1],
             lab,fontsize=FS,color=col,va='center')
    fig.text(CE,fig.transFigure.inverted().transform(sx.transData.transform((1.0,yy)))[1],
             f'n = {len(vals)}',fontsize=FS,color='0.15',va='center',ha='right')
    fig.text(CN,fig.transFigure.inverted().transform(sx.transData.transform((1.0,yy)))[1],
             f'{min(vals):.2f}\u2013{max(vals):.2f}',fontsize=FS,color='0.15',va='center',ha='right')
sy=fig.transFigure.inverted().transform(sx.transData.transform((1.0,2.6)))[1]
fig.text(CA,sy,'The same measurements, by branch and state',fontsize=FS,fontweight='bold',va='center')
from matplotlib.lines import Line2D
ky1=0.060; ky2=0.024
def key(x,y,mk,col,fillw,label,lcol='0.25',ms=4.2):
    fig.add_artist(Line2D([x],[y],marker=mk,ms=ms,mfc=('white' if fillw else col),
                          mec=col,mew=1.1,ls='none',transform=fig.transFigure))
    fig.text(x+0.011,y,label,fontsize=FS-0.5,color=lcol,va='center',ha='left')
    return x+0.011+_w(label)+0.028
x=key(CA+0.004,ky1,'s',BLUE,False,'acid branch',BLUE)
x=key(x,ky1,'o',RED,False,'amide branch',RED)
x=key(x,ky1,'s',BLUE,True,'open marker = depleted baseline')
xx=key(CA+0.004,ky2,'D','0.15',False,
       'NAPRT column: the enzyme that decides the branch was measured in that system;',ms=3.0)
fig.text(xx-0.021,ky2,'\u2014, it was not',fontsize=FS-0.5,color='0.25',va='center',ha='left')
import os; os.makedirs('figures',exist_ok=True)
fig.savefig('figures/PharmRes_Figure1.png',dpi=600)
fig.savefig('figures/PharmRes_Figure1.eps',format='eps')
print('Figure 1 |','mm',round(W*25.4,1),'x',round(H*25.4,1),'| rows',n,'| AU',len(AU),'AD',len(AD),'AM',len(AM))
print('ranges',f'{min(AU):.2f}-{max(AU):.2f}',f'{min(AD):.2f}-{max(AD):.2f}',f'{min(AM):.2f}-{max(AM):.2f}')
