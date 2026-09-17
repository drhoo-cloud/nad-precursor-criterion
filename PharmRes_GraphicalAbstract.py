import _fontreg  # register Nimbus Sans
# -*- coding: utf-8 -*-
"""Graphical abstract, rebuilt on the new title and abstract.
   Elsevier spec: 13 x 5 cm landscape, >= 531 x 1328 px."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.family'] = 'Nimbus Sans'   # substitute Arial at final export
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Nimbus Sans'
plt.rcParams['mathtext.it'] = 'Nimbus Sans:italic'
plt.rcParams['mathtext.bf'] = 'Nimbus Sans:bold'
plt.rcParams['mathtext.default'] = 'regular'

BLUE='#1F6FB4'; RED='#B81F2E'; GREEN='#1E7A4C'; GREY='#5A5A5A'; LGREY='#9A9A9A'
BLUEBG='#EAF2FA'; REDBG='#FBEDEC'; GREENBG='#E8F3EC'; NEUT='#F4F4F4'

W, H = 13/2.54, 5/2.54
fig = plt.figure(figsize=(W, H), dpi=300)
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,130); ax.set_ylim(0,50); ax.axis('off')

def box(x,y,w,h,fc,ec,lw=0.8,r=1.0):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle=f'round,pad=0,rounding_size={r}',facecolor=fc,edgecolor=ec,linewidth=lw))
def t(x,y,s,size=5.4,color='black',weight='normal',ha='center',va='center',style='normal'):
    ax.text(x,y,s,fontsize=size,color=color,ha=ha,va=va,fontweight=weight,style=style)

# ---------- headline ----------
t(65,47.0,'What raises tissue NAD$^{+}$ \u2014 a criterion, and the record against it',
  size=8.0, weight='bold')

Y0, Y1 = 9.5, 43.0            # block band
def header(x, n, label):
    t(x, Y1-2.4, f'{n}  {label}', size=5.9, weight='bold', color=GREY)

# ================= 1. the constraint =================
X0, X1 = 2, 41
box(X0, Y0, X1-X0, Y1-Y0, 'white', LGREY, 0.7)
header((X0+X1)/2, '1', 'The constraint')

box(X0+2, 27.5, X1-X0-4, 8.2, BLUEBG, BLUE, 0.7)
t((X0+X1)/2, 33.2, 'ACID branch  \u2192  NAPRT', size=5.7, color=BLUE, weight='bold')
t((X0+X1)/2, 29.6, 'not inhibited', size=5.3, color=BLUE)

box(X0+2, 17.5, X1-X0-4, 8.2, REDBG, RED, 0.7)
t((X0+X1)/2, 23.2, 'AMIDE branch  \u2192  NAMPT', size=5.7, color=RED, weight='bold')
t((X0+X1)/2, 19.6, 'shut off by NAD$^{+}$ \u2014 efficiency \u00f7 46.5', size=5.3, color=RED)

t((X0+X1)/2, 13.2, 'Known, and never costed:', size=5.0, color=GREY)
t((X0+X1)/2, 11.0, 'stated in 10 of 297 reviews, converted in 0',
  size=5.0, color=GREY, weight='bold')

# ================= 2. the conversion =================
X0, X1 = 45.5, 84.5
box(X0, Y0, X1-X0, Y1-Y0, 'white', LGREY, 0.7)
header((X0+X1)/2, '2', 'The conversion')

box(X0+2, 30.0, X1-X0-4, 6.4, NEUT, LGREY, 0.6)
t((X0+X1)/2, 34.4, 'gain has a ceiling the tissue sets', size=5.2, color=GREY)
t((X0+X1)/2, 31.5, '1.29    \u2192  2.16 only when depleted', size=5.6, weight='bold')

box(X0+2, 22.0, X1-X0-4, 6.4, NEUT, LGREY, 0.6)
t((X0+X1)/2, 26.4, 'penalty has no lower bound', size=5.2, color=GREY)
t((X0+X1)/2, 23.5, 'nicotinamide inhibits the effector', size=5.6, weight='bold')

ax.annotate('', xy=((X0+X1)/2, 16.6), xytext=((X0+X1)/2, 20.6),
            arrowprops=dict(arrowstyle='-|>', color=GREY, lw=1.0, shrinkA=0, shrinkB=0))
box(X0+6, 10.6, X1-X0-12, 5.6, GREENBG, GREEN, 0.8)
t((X0+X1)/2, 13.4, '\u03b7  >  \u03b7$_{req}$', size=7.2, color=GREEN, weight='bold')

# ================= 3. the verdict =================
X0, X1 = 89, 128
box(X0, Y0, X1-X0, Y1-Y0, 'white', LGREY, 0.7)
header((X0+X1)/2, '3', 'The verdict')

# inset axes for the criterion plot
px = fig.add_axes([ (X0+6.5)/130, 20.0/50, (X1-X0-11)/130, 17.0/50 ])
KS, Ki = 29.0, 175.0
M = np.logspace(0, np.log10(3e4), 400)
for N0, col, lab in ((100.0, GREY, 'unstressed'), (25.0, LGREY, 'depleted')):
    px.plot(M, ((KS+N0)/KS)*M/(Ki+M), color=col, lw=1.0)
px.axhline(1.0, color='black', lw=0.5, ls=(0,(2,2)))
for eta, c in ((0.00, RED), (0.26, RED), (0.34, RED)):
    px.plot([1, 3e4], [eta, eta], color=c, lw=0.7, alpha=0.9)
px.axvspan(1e3, 3e4, color='#EDEDED', zorder=0)
px.set_xscale('log'); px.set_xlim(1, 3e4); px.set_ylim(0, 5)
px.set_yticks([0, 1, 5]); px.set_yticklabels(['0','1','5'], fontsize=4.4)
px.set_xticks([1, 1e2, 1e4]); px.set_xticklabels(['1','10$^{2}$','10$^{4}$'], fontsize=4.4)
px.tick_params(length=1.6, width=0.4, pad=1)
for s in px.spines.values(): s.set_linewidth(0.5)
px.spines['top'].set_visible(False); px.spines['right'].set_visible(False)
px.set_xlabel('nicotinamide, \u00b5mol L$^{-1}$', fontsize=4.2, labelpad=0.5)
px.set_ylabel('\u03b7$_{req}$', fontsize=5.0, labelpad=1)
px.text(1.3e2, 4.30, 'required', fontsize=4.4, color=GREY, ha='center')
px.text(7.0e3, 0.60, 'measured', fontsize=4.4, color=RED, ha='center')
px.text(5.0e3, 4.78, 'in use', fontsize=4.0, color=GREY, ha='center', va='center')

t((X0+X1)/2, 13.2, 'No published dose\u2013response series clears', size=5.3, weight='bold')
t((X0+X1)/2, 11.2, 'the criterion in unstressed tissue', size=5.3, weight='bold')

# ---------- arrows between blocks ----------
for x in (43.2, 86.7):
    ax.annotate('', xy=(x+1.6, 26), xytext=(x, 26),
                arrowprops=dict(arrowstyle='-|>', color=GREY, lw=0.9, shrinkA=0, shrinkB=0))

# ---------- banner ----------
box(2, 1.0, 126, 6.4, GREENBG, GREEN, 1.0)
t(65, 4.2, 'Branch and state decide; the dose does not.',
  size=7.0, color=GREEN, weight='bold')

import os; os.makedirs('figures', exist_ok=True)
fig.savefig('figures/PharmRes_GraphicalAbstract.png', dpi=600)
fig.savefig('figures/PharmRes_GraphicalAbstract.eps', format='eps')
from PIL import Image
im = Image.open('figures/PharmRes_GraphicalAbstract.png'); print('px', im.size, '| cm 13.0 x 5.0')
