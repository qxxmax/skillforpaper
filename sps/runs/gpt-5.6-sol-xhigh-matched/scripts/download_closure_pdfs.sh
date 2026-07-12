#!/bin/sh
set -eu
op=75
for id in 2607.08505 2605.12597 2604.10209
do
  epoch=$(date +%s)
  path="sources/pdfs/$id.pdf"
  if curl -sS -L --fail --retry 4 --retry-delay 2 "https://arxiv.org/pdf/$id" -o "$path"; then
    bytes=$(wc -c < "$path" | tr -d ' ')
    printf 'N%03d,%s,arxiv,GET,https://arxiv.org/pdf/%s,success,1,%s,%s,closure primary PDF\n' "$op" "$epoch" "$id" "$bytes" "$path" >> network_access_log.csv
  else
    printf 'N%03d,%s,arxiv,GET,https://arxiv.org/pdf/%s,failed,0,0,%s,closure primary PDF retrieval failed\n' "$op" "$epoch" "$id" "$path" >> network_access_log.csv
  fi
  op=$((op + 1))
  sleep 1
done
