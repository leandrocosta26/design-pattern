package template_method;

import java.util.ArrayList;
import java.util.List;

public class Executor {
	public static void main(String[] args) {
		List<Item> itens = new ArrayList<>();
		Item item1 = new Item("Item 1", 50.00);
		Item item2 = new Item("Item 2", 570.00);
		itens.add(item1);
		itens.add(item2);
		Orcamento orcarmento =  new Orcamento();
		orcarmento.setItens(itens);
		System.out.println(new DescontoCompostoValor().calcula(orcarmento));
		System.out.println(new DescontoCompostoItens().calcula(orcarmento));
	}
}
