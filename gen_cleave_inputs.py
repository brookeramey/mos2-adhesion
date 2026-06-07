import os

LAYERS_FIXED = [
    ('S',  0.3333328794, 0.6666667587, -0.1049877899),
    ('Mo', 0.0000000000, 0.0000000000, -0.0525964321),
    ('S',  0.3333328794, 0.6666667587, -0.0001809091),
    ('S',  0.6666667587, 0.3333328794,  0.1036040435),
    ('Mo', 0.3333328794, 0.6666667587,  0.1560929369),
    ('S',  0.6666667587, 0.3333328794,  0.2085443296),
    ('S',  0.0000000000, 0.0000000000,  0.3116481327),
    ('Mo', 0.6666667587, 0.3333328794,  0.3641373260),
    ('S',  0.0000000000, 0.0000000000,  0.4165763268),
]

LAYER4_BASE = [
    ('S',  0.3333328794, 0.6666667587,  0.5183202237),
    ('Mo', 0.0000000000, 0.0000000000,  0.5707379433),
    ('S',  0.3333328794, 0.6666667587,  0.6231027411),
]

C_CELL = 30.0
A_LAT  = 3.160

displacements = [round(i*0.2, 1) for i in range(21)]
displacements += [round(4.5+i*0.5, 1) for i in range(8)]

TEMPLATE = """&CONTROL
  calculation   = 'scf'
  prefix        = 'mos2_cleave'
  outdir        = './tmp/cleave/cleave_dz{tag}/'
  pseudo_dir    = './pseudo/'
  verbosity     = 'low'
/

&SYSTEM
  ibrav=4
  a={a}
  c={c}
  nat=12
  ntyp=2
  ecutwfc=80.0
  ecutrho=640.0
  occupations='smearing'
  smearing='m-p'
  degauss=0.02
  input_dft='vdw-df2-b86r'
/

&ELECTRONS
  mixing_mode   = 'local-TF'
  mixing_beta   = 0.2
  conv_thr      = 1.0e-8
/

ATOMIC_SPECIES
  Mo  95.960  Mo.pbe-spn-kjpaw_psl.1.0.0.UPF
  S   32.060  S.pbe-n-kjpaw_psl.1.0.0.UPF

ATOMIC_POSITIONS crystal
{positions}
K_POINTS automatic
16 16 1 0 0 0
"""

os.makedirs('inputs/cleave', exist_ok=True)
os.makedirs('outputs/cleave', exist_ok=True)

for i, dz in enumerate(displacements):
    tag = f"{i:03d}_dz{dz:.1f}".replace('.', 'p')
    delta = dz / C_CELL
    pos_lines = []
    for sp, x, y, z in LAYERS_FIXED:
        pos_lines.append(f"  {sp}  {x:.10f}  {y:.10f}  {z:.10f}")
    for sp, x, y, z in LAYER4_BASE:
        pos_lines.append(f"  {sp}  {x:.10f}  {y:.10f}  {z+delta:.10f}")
    inp = TEMPLATE.format(tag=tag, a=A_LAT, c=C_CELL,
                          positions='\n'.join(pos_lines))
    open(f"inputs/cleave/cleave_{tag}.in", 'w').write(inp)

print(f"Generated {len(displacements)} inputs")
print(f"dz: {displacements[0]} to {displacements[-1]} A")
