package chan_of_responsability;

public class Compras {
	
	public Compras(Double total, Integer quantidade){
		this.total = total;
		this.quantidade = quantidade;
	}

	private Double total;
	private Integer quantidade;
	private Double desconto;
	
	public Double getTotal() {
		return total;
	}
	public void setTotal(Double total) {
		this.total = total;
	}
	public Integer getQuantidade() {
		return quantidade;
	}
	public void setQuantidade(Integer quantidade) {
		this.quantidade = quantidade;
	}

	public Double getDesconto() {
		return desconto;
	}
	public void setDesconto(Double desconto) {
		this.desconto = desconto;
	}
	
	
}
