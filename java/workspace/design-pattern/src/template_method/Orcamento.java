package template_method;

import java.util.List;

public class Orcamento {
	
	private List<Item> itens;

	public Double getValorFinal() {
		return this.itens.stream().mapToDouble(valor -> valor.getValor()).sum();
	}

	public List<Item> getItens() {
		return itens;
	}

	public void setItens(List<Item> itens) {
		this.itens = itens;
	}
}
