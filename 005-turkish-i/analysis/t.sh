# Turkey test, Bash: ${var,,} and ${var^^}.
a=TITLE b=title f=FILE
[[ "${f,,}" == "file" ]] && same=true || same=false
printf '{"lang":"Bash","version":"%s","locale":"%s","api":"${var,,} / ${var^^}","lower_TITLE":"%s","upper_title":"%s","FILE_equals_file":%s}\n' "$BASH_VERSION" "$LANG" "${a,,}" "${b^^}" "$same"
