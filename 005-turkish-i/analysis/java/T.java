// Turkey test, Java: the default (no-argument) case functions.
import java.util.Locale;
public class T {
  public static void main(String[] a) {
    String lower = "TITLE".toLowerCase(), upper = "title".toUpperCase();
    boolean same = "FILE".toLowerCase().equals("file");
    System.out.printf("{\"lang\":\"Java\",\"version\":\"%s\",\"locale\":\"%s\",\"api\":\"toLowerCase() / toUpperCase()\",\"lower_TITLE\":\"%s\",\"upper_title\":\"%s\",\"FILE_equals_file\":%s}%n",
      System.getProperty("java.version"), Locale.getDefault(), lower, upper, same);
  }
}
