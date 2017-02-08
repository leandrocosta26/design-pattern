package object_builder;

import java.util.Date;

public class ObjectBuilder {

	private String titulo;
	private String codigo;
	private Date date;
	private String descricao;
	
	public ObjectBuilder comTitulo(String titulo){
		this.titulo = titulo;
		return this;
	}
	
	public ObjectBuilder comCodigo(String codigo){
		this.codigo = codigo;
		return this;
	}
	
	public ObjectBuilder comDate(Date date){
		this.date = date;
		return this;
	}
	
	public ObjectBuilder comDescricao(String descricao){
		this.descricao = descricao;
		return this;
	}
	
	public NotaFiscal construir() throws Exception{
		if(titulo == null || titulo.isEmpty()){
			throw new Exception("Titulo não pode ser em branco");
		}
		if(codigo == null || codigo.isEmpty()){
			throw new Exception("codigo não pode ser em branco");
		}
		if(date == null){
			this.date = new Date();
		}
		if(descricao == null ){
			this.descricao = "";
		}
		return new NotaFiscal(titulo, codigo, date, descricao);
	}
}
