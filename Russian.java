import java.util.Scanner;
import java.util.List;

public class Russian {
	public static List<Character> cons =  Arrays.asList('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь');
	public static List<Character> consCap = Arrays.asList('Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь');
	
	public static void main(String args[]) {
		// copy("фдлацоущш");
		Scanner scan = new Scanner(System.in);
		String in;

		System.out.print("input: ");
		in = scan.nextLine();
		// System.out.println();

		System.out.println("input was "+in);
		process(in);

		scan.close();
	}

	public static void process (String in) {
		char c;
		int[] inds = new int[in.length()];
		for (int i = 0; i < in.length(); i++) {
			c = in.charAt(i);
			inds[i] = cons.indexOf(""+c);
		}
	}
}