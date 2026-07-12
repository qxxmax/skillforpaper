#!/bin/sh
set -eu

out="sources/pdfs"
log="network_access_log.csv"
op=47

for id in \
  1904.12072 2007.07115 2106.05934 2003.06413 2202.11712 \
  2512.19575 2207.00283 2110.02673 2502.02127 2107.00734 \
  2201.08862 2210.03139 2309.17082 2502.05504 2510.26081 \
  2601.19552 2602.09045 2605.06134 2510.01328 2605.11199 \
  2111.15141 2302.13834 2410.02711
do
  epoch=$(date +%s)
  path="$out/$id.pdf"
  if curl -sS -L --fail --retry 4 --retry-delay 2 "https://arxiv.org/pdf/$id" -o "$path"; then
    bytes=$(wc -c < "$path" | tr -d ' ')
    printf 'N%03d,%s,arxiv,GET,https://arxiv.org/pdf/%s,success,1,%s,%s,primary PDF\n' "$op" "$epoch" "$id" "$bytes" "$path" >> "$log"
  else
    printf 'N%03d,%s,arxiv,GET,https://arxiv.org/pdf/%s,failed,0,0,%s,primary PDF retrieval failed\n' "$op" "$epoch" "$id" "$path" >> "$log"
  fi
  op=$((op + 1))
  sleep 1
done
