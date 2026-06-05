# MoS₂ Adhesion Fingerprint — Phase 3

**Project:** First-principles adhesion engineering framework — molybdenum disulfide  
**Code:** Quantum ESPRESSO v7.3  
**Machine:** bohr (32-core Linux workstation)  
**Status:** Structural relaxation running

---

## Why MoS2

Third material in the universality study. Key differences from graphite and hBN:

| Property | Graphite | hBN | MoS2 |
|----------|----------|-----|------|
| Bonding | Covalent (C-C) | Ionic (B-N) | Mixed ionic-covalent (Mo-S) |
| Atoms per layer | 2 (C) | 2 (B,N) | 3 (S-Mo-S sandwich) |
| Lattice constant a | 2.464 A | 2.504 A | 3.160 A |
| d0 (exp) | 3.354 A | 3.330 A | 6.147 A |
| Layer thickness | ~0 A | ~0 A | ~3.17 A |
| Electronic structure | Semimetal | Insulator | Semiconductor (1.8 eV gap) |
| Interfacial atoms | C | B, N | S (3rd row) |

MoS2 is the first material in this study with:
- A three-atom layer basis (S-Mo-S sandwich)
- Heavy transition metal (Mo, 4d electrons)
- Nearly double the interlayer spacing of graphite
- Third-row interfacial atoms (S vs C, B, N for previous materials)

---

## Key Predictions (based on graphite and hBN results)

From the universality pattern established in Phases 1-2:

1. **lambda(MoS2) > lambda(graphite) = 0.624 A**
   S is a 3rd-row element with larger atomic radius than C, B, N.
   Pauli repulsion extends over a longer range -> larger lambda.
   Predicted: lambda ~ 0.9-1.2 A

2. **W_ad(MoS2) > W_ad(graphite)**
   Larger interlayer spacing but heavier atoms with larger polarizability.
   Expected stronger vdW dispersion.

3. **UBER deviation may be larger**
   If lambda is significantly different, the deviation pattern may change.
   Tests whether lambda universality holds beyond 2nd-row elements.

4. **W_SP/W_ad ratio ~ 10-15%**
   If the ratio of lateral to normal adhesion is approximately universal,
   this should hold for MoS2 despite different structure.

---

## System Setup

- 4-layer 2H-stacked MoS2 slab (AA prime stacking)
- Lattice: Hexagonal, a = 3.160 A, c = 30.0 A
- Atoms: 12 (3 per layer: 1 Mo + 2 S)
- Pseudopotentials: Mo.pbe-spn-kjpaw_psl.1.0.0.UPF, S.pbe-n-kjpaw_psl.1.0.0.UPF
- Functional: rev-vdW-DF2 (vdw-df2-b86r)
- Parameters: ecutwfc=80 Ry, k=16x16x1

## Workflow

- [ ] Step 1: Structural relaxation (running)
- [ ] Step 2: Cleavage energy scan
- [ ] Step 3: UBER fit
- [ ] Step 4: GSFE surface
- [ ] Step 5: Full fingerprint comparison vs graphite and hBN

---

## Parent Projects

- Phase 1 (graphite): github.com/brookeramey/graphene-adhesion
  W_ad=21.60 meV/A2, lambda=0.624 A, F_max=2041 MPa,
  W_SP=2.41 meV/A2, tau=1.02 GPa, theta*=63.4 deg

- Phase 2 (hBN): github.com/brookeramey/hbn-adhesion
  W_ad=21.02 meV/A2, lambda=0.642 A, F_max=1931 MPa,
  W_SP=3.32 meV/A2, tau=1.37 GPa, theta*=54.7 deg

## Key Finding So Far

Cleavage parameters (W_ad, lambda) are nearly identical for graphite and hBN
despite different bonding — universality of Pauli repulsion confirmed for
2nd-row elements. MoS2 will test whether this extends to 3rd-row elements.
