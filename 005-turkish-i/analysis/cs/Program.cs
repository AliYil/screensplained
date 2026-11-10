// Turkey test, C#: the default (culture-sensitive) case functions.
using System.Globalization;
var lower = "TITLE".ToLower();
var upper = "title".ToUpper();
var same = string.Compare("FILE", "file", true) == 0;
Console.WriteLine($"{{\"lang\":\"C#\",\"version\":\".NET {Environment.Version}\",\"locale\":\"{CultureInfo.CurrentCulture.Name}\",\"api\":\"ToLower() / ToUpper() / string.Compare(a, b, ignoreCase)\",\"lower_TITLE\":\"{lower}\",\"upper_title\":\"{upper}\",\"FILE_equals_file\":{same.ToString().ToLower()}}}");
