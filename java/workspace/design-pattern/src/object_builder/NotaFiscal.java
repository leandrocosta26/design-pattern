package object_builder;

import java.util.Date;

public class NotaFiscal {
	
	public NotaFiscal(String titulo, String codigo, Date date, String descricao) {
		super();
		this.titulo = titulo;
		this.codigo = codigo;
		this.date = date;
		this.descricao = descricao;
	}

	private String titulo;
	private String codigo;
	private Date date;
	private String descricao;

	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public String getCodigo() {
		return codigo;
	}
	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
}
