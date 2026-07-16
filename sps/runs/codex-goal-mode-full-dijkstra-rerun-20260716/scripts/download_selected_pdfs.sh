#!/bin/zsh
# Download current selected PDFs and extract their text for the C3 gate.

set -u

if [[ $# -ne 1 ]]; then
  print -u2 "usage: $0 RUN_DIR"
  exit 64
fi

run_dir="$1"
jobs="$run_dir/download_jobs.tsv"
status_file="$run_dir/fulltext_download_status.tsv"

mkdir -p "$run_dir/sources/pdfs" "$run_dir/sources/text"
printf 'paper_id\tarxiv_id\tpdf_url\tretrieved_at_utc\thttp_status\tstatus\tbytes\tsha256\tpage_count\tpdf_file\ttext_file\terror_file\n' > "$status_file"

{
  IFS=$'\t' read -r header
  while IFS=$'\t' read -r paper_id arxiv_id pdf_url pdf_file text_file; do
    output="$run_dir/$pdf_file"
    text_output="$run_dir/$text_file"
    error_file="$output.curl.stderr.txt"
    retrieved_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    http_status=""
    fetch_status="OK"
    if http_status="$(curl --fail --silent --show-error --location --max-time 180 \
      --user-agent 'play-the-toy-with-children/part1-fulltext-audit (contact: local-codex-run)' \
      --write-out '%{http_code}' --output "$output" "$pdf_url" 2>"$error_file")"; then
      bytes="$(wc -c < "$output")"
      hash_line="$(sha256sum "$output")"
      IFS=' ' read -r sha256 unused <<< "$hash_line"
      page_count="$(pdfinfo "$output" | awk '/^Pages:/ {print $2}')"
      if pdftotext -layout "$output" "$text_output"; then
        :
      else
        fetch_status="TEXT_EXTRACTION_ERROR"
      fi
    else
      fetch_status="ERROR"
      bytes="0"
      sha256=""
      page_count=""
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$paper_id" "$arxiv_id" "$pdf_url" "$retrieved_at" "$http_status" "$fetch_status" \
      "$bytes" "$sha256" "$page_count" "$pdf_file" "$text_file" "$error_file" >> "$status_file"
    sleep 2.1
  done
} < "$jobs"

print "wrote $status_file"
