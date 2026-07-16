#!/bin/zsh
# Fetch the pre-encoded jobs with the desktop-approved curl transport.

set -u

if [[ $# -ne 1 ]]; then
  print -u2 "usage: $0 RUN_DIR"
  exit 64
fi

run_dir="${1:A}"
jobs="$run_dir/transport_jobs.tsv"
status_file="$run_dir/transport_status.tsv"
raw_dir="$run_dir/raw/arxiv"
delay_seconds="${ARXIV_DELAY_SECONDS:-3.1}"

mkdir -p "$raw_dir"
printf 'route_id\tround\tfamily\tfacet\tquery_type\texpression\turl\tretrieved_at_utc\thttp_status\tstatus\tbytes\tsha256\traw_file\terror_file\n' > "$status_file"

{
  IFS=$'\t' read -r header
  while IFS=$'\t' read -r route_id round family facet query_type expression url raw_file; do
    output="$run_dir/$raw_file"
    error_file="${output%.xml}.curl.stderr.txt"
    retrieved_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    http_status=""
    fetch_status="OK"
    if http_status="$(curl --fail --silent --show-error --location --max-time 90 \
      --user-agent 'play-the-toy-with-children/part1-audit (contact: local-codex-run)' \
      --write-out '%{http_code}' --output "$output" "$url" 2>"$error_file")"; then
      bytes="$(wc -c < "$output")"
      hash_line="$(sha256sum "$output")"
      sha256="${hash_line%% *}"
    else
      fetch_status="ERROR"
      bytes="0"
      sha256=""
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$route_id" "$round" "$family" "$facet" "$query_type" "$expression" "$url" \
      "$retrieved_at" "$http_status" "$fetch_status" "$bytes" "$sha256" "$raw_file" \
      "${error_file#$run_dir/}" >> "$status_file"
    sleep "$delay_seconds"
  done
} < "$jobs"

print "wrote $status_file"
