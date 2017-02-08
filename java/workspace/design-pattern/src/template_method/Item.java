package template_method;

public class Item {
	
	public Item(String name, Double valor){
		this.name = name;
		this.valor = valor;
	}
	
	private String name;
	private Double valor;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Double getValor() {
		return valor;
	}
	public void setValor(Double valor) {
		this.valor = valor;
	}

}
