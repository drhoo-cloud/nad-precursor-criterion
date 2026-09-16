#!/usr/bin/env python3
"""
Reproduces every derived number quoted in the manuscript.

    Resting NAD+ sets the ceiling, not the dose:
    a quantitative criterion for vitamin B3 precursors across tissues

Run:  python3 verify_values.py
Nothing here is a measurement. Every number below is arithmetic on the five
inputs of Table 2, which were measured or assumed by others.
"""
K_S, K_I = 29.0, 175.0          # SIRT1: Michaelis constant, nicotinamide Ki
N_UN, N_DP = 100.0, 25.0        # nuclear free NAD+, unstressed / fourfold depleted
M0 = 30.0                       # resting intracellular nicotinamide
ETA = 0.34                      # highest published elasticity

sat     = lambda N: N / (K_S + N)
gain    = lambda N, N0: sat(N) / sat(N0)
penalty = lambda M: (1.0 + M0 / K_I) / (1.0 + M / K_I)
eta_req = lambda M, N0: M * (K_S + N0) / (K_S * (K_I + M))
G_max   = lambda N0: (K_S + N0) / N0
M_star  = lambda N0: K_I * (G_max(N0) * (1 + M0 / K_I) - 1)
M_dag   = lambda N0: K_S * K_I / N0          # concentration at which eta_req = 1

def out(M, N0, eta=ETA):
    return gain(N0 * (M / M0) ** eta, N0) * penalty(M)

R = lambda x: round(x, 2)
print("Table 2 -- inputs (measured or assumed elsewhere)")
print(f"  K_S {K_S:.0f}   K_i {K_I:.0f}   N0 {N_UN:.0f} / {N_DP:.0f}   M0 {M0:.0f}  umol/L")

print("\nTable 2 -- derived            unstressed  depleted   ratio   manuscript")
print(f"  G_max                        {G_max(N_UN):.2f}       {G_max(N_DP):.2f}"
      f"      {G_max(N_DP)/G_max(N_UN):.1f}x    1.29 / 2.16, 1.7x  (S4.3)")
print(f"  M* (umol/L)                  {M_star(N_UN):.0f}         {M_star(N_DP):.0f}"
      f"       {M_star(N_DP)/M_star(N_UN):.1f}x    89 / 268           (S4.3)")
print(f"  eta_req at M0                {eta_req(M0,N_UN):.2f}       {eta_req(M0,N_DP):.2f}"
      f"      {eta_req(M0,N_UN)/eta_req(M0,N_DP):.1f}x    0.65 / 0.27, 2.4x  (S4.3)")
print(f"  eta_req at 1 mmol/L          {eta_req(1000,N_UN):.2f}       {eta_req(1000,N_DP):.2f}"
      f"             3.79 / 1.58        (S4.4)")
print(f"  M+ (eta_req = 1, umol/L)     {M_dag(N_UN):.0f}          {M_dag(N_DP):.0f}"
      f"               51 / 203           (S4.4)")

print("\nSection 4.2 -- where the effector starts")
print(f"  fractional saturation        {100*sat(N_UN):.0f}%        {100*sat(N_DP):.0f}%"
      f"                78% / 46%")
print(f"  G_max at the whole-cell figure (400 umol/L)  {G_max(400):.2f}        1.07")

print("\nSection 4.4 -- the concentrations actually used")
for M in (100.0, 1000.0, 30000.0):
    print(f"  M = {M:8.0f}   eta_req {eta_req(M,N_UN):.2f} / {eta_req(M,N_DP):.2f}"
          f"   penalty 1/{1/penalty(M):.0f}-fold")
print(f"  penalty range over 1-30 mmol/L: {1/penalty(1000):.0f}- to {1/penalty(30000):.0f}-fold below baseline"
      "        six- to 147-fold")

print("\nSection 5.1 -- worked example (Hara 2007, HEK293)")
import math
eta_obs = math.log(1.31 / 1.00) / math.log(5000.0 / 20.0)
print(f"  eta observed                 {eta_obs:.2f}                             0.05")
print(f"  eta_req at 20 umol/L         {eta_req(20,N_UN):.2f} / {eta_req(20,N_DP):.2f}"
      f"                     0.46 / 0.19")
print(f"  eta_req at 5 mmol/L          {eta_req(5000,N_UN):.2f} / {eta_req(5000,N_DP):.2f}"
      f"                     4.30 / 1.80")

print("\nFigure 4 -- the best measured response, eta = %.2f" % ETA)
for M in (39.1, 100.0):
    print(f"  M = {M:6.1f}   unstressed {100*(out(M,N_UN)-1):+.1f}%"
          f"   depleted {100*(out(M,N_DP)-1):+.1f}%")
