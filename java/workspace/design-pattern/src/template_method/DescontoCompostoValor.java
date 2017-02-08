package template_method;

public class DescontoCompostoValor extends TemplateCalculator{

	@Override
	protected Double calcularMaximaTaxacao(Orcamento orcamento) {
		return orcamento.getValorFinal() * 0.1;
	}

	@Override
	protected Boolean deveCalcularMaximaTaxacao(Orcamento orcamento) {
		return orcamento.getValorFinal() > 500;
	}

	@Override
	protected Double calcularMinimaTaxacao(Orcamento orcamento) {
		return orcamento.getValorFinal() * 0.05;
	}

}
