package palindrome;
import java.util.List;

public class App {
    public static void main(String[] args){

        Loader fileReader = new Loader();
        String filename = "dictionary.txt";
        List<String> ls = fileReader.reader(filename);
        for(String x: ls){
            String word = x.toLowerCase();
            String reversedStr = "";
            for (int i = 0; i < word.length(); i++) {
                reversedStr = word.charAt(i) + reversedStr;
            }
            if(word.equals(reversedStr) && word.length() > 1){
                System.out.println("the word: "+ word +" is a palindrome");
                System.out.println("Orginal word: "+ word +" reversed: "+reversedStr);
            }
        }

    }
}
