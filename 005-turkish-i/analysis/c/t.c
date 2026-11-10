/* Turkey test, C: tolower()/toupper() byte by byte and strcasecmp(), after setlocale(LC_ALL, ""). */
#include <ctype.h>
#include <gnu/libc-version.h>
#include <locale.h>
#include <stdio.h>
#include <strings.h>
int main(void) {
  const char *loc = setlocale(LC_ALL, "");
  char lower[] = "TITLE", upper[] = "title";
  for (char *p = lower; *p; p++) *p = (char)tolower((unsigned char)*p);
  for (char *p = upper; *p; p++) *p = (char)toupper((unsigned char)*p);
  printf("{\"lang\":\"C\",\"version\":\"glibc %s\",\"locale\":\"%s\",\"api\":\"tolower() / toupper() / strcasecmp()\",\"lower_TITLE\":\"%s\",\"upper_title\":\"%s\",\"FILE_equals_file\":%s}\n",
         gnu_get_libc_version(), loc ? loc : "?", lower, upper, strcasecmp("FILE", "file") == 0 ? "true" : "false");
  return 0;
}
