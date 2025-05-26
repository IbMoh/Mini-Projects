package palindrome;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Loader {
    
    public List<String> reader(String fileName){

        List<String> word_list = new ArrayList<>();

        try {
            File file = new File(fileName);
            Scanner reader = new Scanner(file);

            while (reader.hasNextLine()){
                String data = reader.nextLine();
                word_list.add(data);
            }

            reader.close();

        } catch (FileNotFoundException e) {
            System.out.println(e);
        }

        return word_list;
    }

}

