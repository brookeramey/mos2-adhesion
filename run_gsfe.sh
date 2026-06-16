#!/bin/bash
PW=/home/brooke/qe/q-e-qe-7.3/bin/pw.x
mkdir -p outputs/gsfe

inputs=(inputs/gsfe/gsfe_*.in)
total=${#inputs[@]}

for idx in "${!inputs[@]}"; do
    f="${inputs[$idx]}"
    base=$(basename $f .in)
    out="outputs/gsfe/${base}.out"
    num=$((idx+1))

    if [ -f "$out" ] && grep -q "JOB DONE" "$out"; then
        echo "  [${num}/${total}] ${base} ... already done"
        continue
    fi

    echo "  [${num}/${total}] ${base} ..."
    $PW < $f > $out 2>&1

    if grep -q "JOB DONE" "$out"; then
        echo "  [${num}/${total}] ${base} ... DONE"
    else
        echo "  [${num}/${total}] ${base} ... FAILED"
    fi
done
echo "MoS2 GSFE scan complete"
