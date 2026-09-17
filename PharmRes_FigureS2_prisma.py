import _fontreg  # register Nimbus Sans
#!/usr/bin/env python3
"""PRISMA-ScR flow of records for the scoping audit of section 3 (Figure S2)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
FONT='Nimbus Sans'; FS=8.0
plt.rcParams.update({'font.family':FONT,'font.size':FS,
                     'pdf.fonttype':42,'ps.fonttype':42})
W=150/25.4; H=118/25.4
fig=plt.figure(figsize=(W,H),dpi=300)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
INK='0.15'; LINE='0.45'; SIDE='0.35'
def box(x,y,w,h,lines,fc='white',ec=LINE,bold0=True,fs=FS):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.6,rounding_size=1.2',
                 fc=fc,ec=ec,lw=0.8,zorder=2))
    n=len(lines); step=h/(n+1)
    for i,t in enumerate(lines):
        ax.text(x+w/2,y+h-step*(i+1),t,ha='center',va='center',fontsize=fs,
                color=INK,zorder=3,fontweight=('bold' if (i==0 and bold0) else 'normal'))
def arrow(x1,y1,x2,y2,style='-|>'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=9,
                 lw=0.8,color=LINE,shrinkA=0,shrinkB=0,zorder=1))
def phase(y,label):
    ax.text(1.5,y,label,rotation=90,ha='center',va='center',fontsize=FS-0.5,
            color=SIDE,fontweight='bold')
CX,CW=20,52
phase(88,'Identification'); phase(56,'Retrieval'); phase(24,'Coding')
box(CX,82,CW,12,['Reviews identified by the primary search','PubMed 2020\u20132026, NAD in title','with any vitamin B3 precursor term   n = 236'])
arrow(CX+CW/2,82,CX+CW/2,74)
box(CX,62,CW,12,['Full text obtained','from PubMed Central  n = 150','by other means  n = 26            total  n = 176'])
box(CX+CW+6,64,20,8,['Full text not','obtainable','n = 60'],fc='0.965',bold0=False,fs=FS-0.5)
arrow(CX+CW,68,CX+CW+6,68)
arrow(CX+CW/2,62,CX+CW/2,54)
box(CX,42,CW,12,['Coded on two axes and one secondary axis','inhibitor named \u00d7 enzyme said to be inhibited','denominator for Table 1   n = 176'])
box(CX+CW+6,43,22,10,['Coded ineligible','on subject  n = 7','(retained in the','denominator)'],fc='0.965',bold0=False,fs=FS-1)
arrow(CX+CW,48,CX+CW+6,48)
arrow(CX+CW/2,42,CX+CW/2,34)
box(CX,22,CW,12,['State the constraint  n = 5  (2.8%)',
                 'Place it on the consuming enzymes  n = 12  (6.8%)',
                 'Convert it into a threshold or criterion  n = 0'],fc='0.965')
arrow(CX+CW/2,22,CX+CW/2,14)
box(CX-9,1,CW+18,11,['Sensitivity analysis: the title restriction reversed',
  'second search 191 reviews, full text 121; five state the constraint, none converts it',
  'across 297 full-text reviews, ten state it and none converts it'],fc='white',fs=FS-0.5)
fig.savefig('figures/PharmRes_FigureS2.eps',format='eps')
fig.savefig('figures/PharmRes_FigureS2.png',dpi=600)
print('mm',round(W*25.4,1),'x',round(H*25.4,1))
