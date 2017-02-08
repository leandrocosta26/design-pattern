package state;

public class EmAprovacao extends EstadoDeUmOrcamento{

	@Override
	public void aprova(Orcamento orcamento) {
		orcamento.setEstadoAtual(new Aprovado());
	}

	@Override
	public void cancelado(Orcamento orcamento) {
		orcamento.setEstadoAtual(new Cancelado());
	}

	@Override
	public void finalizado(Orcamento orcamento) throws Exception {
		throw new Exception("Orcamento não pode ser finalizado");
	}

	@Override
	public void aplicaDescontoExtra(Orcamento orcamento) {
		orcamento.setDesconto(orcamento.getValorFinal() * 0.05);
	}

}
