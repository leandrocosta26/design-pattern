import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;

public class Controller {

	public static void main(String[] args) {
		while(true){
		List<Integer> listInteger = new ArrayList<>();
		Integer value =  new Integer(0);
		while(value < 1000000){
			listInteger.add(value);
			value += 1;
		}
		
		ForkJoinPool fork = new ForkJoinPool(250);
		fork.submit(() -> {
			listInteger.stream().parallel().forEach(a -> {
				System.out.println("Number of list " +  a.toString());
			});
		});
		}
 	}
}
