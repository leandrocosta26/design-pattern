package state;

import java.util.List;

public class Orcamento{
	
	private List<Item> itens;
	private EstadoDeUmOrcamento estadoAtual;
	private Double desconto;
	
	public Orcamento(){
		this.estadoAtual = new EmAprovacao();
		this.desconto = 0.0;
	}
	
	public void aprova() throws Exception{
		this.getEstadoAtual().aprova(this);
	}
	
	public void cancela() throws Exception{
		this.getEstadoAtual().cancelado(this);
	}

	public void finaliza() throws Exception{
		this.getEstadoAtual().finalizado(this);
	}
	
	public void aplicaDesconto() throws Exception{
		this.getEstadoAtual().aplicaDescontoExtra(this);
	}
	
	public Double getValorFinal() {
		return this.itens.stream().mapToDouble(valor -> valor.getValor()).sum() - this.getDesconto();
	}

	public List<Item> getItens() {
		return itens;
	}

	public void setItens(List<Item> itens) {
		this.itens = itens;
	}

	public EstadoDeUmOrcamento getEstadoAtual() {
		return estadoAtual;
	}

	public void setEstadoAtual(EstadoDeUmOrcamento estadoAtual) {
		this.estadoAtual = estadoAtual;
	}

	public Double getDesconto() {
		return desconto;
	}

	public void setDesconto(Double desconto) {
		this.desconto += desconto;
	}
}
