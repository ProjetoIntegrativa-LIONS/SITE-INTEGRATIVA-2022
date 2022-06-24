from datetime import datetime
from flask import Blueprint, render_template , redirect , request, url_for
from Diretorio_login.login import validarSessao
from Dominio_project.ControlContatos import  ControlContato
from Dominio_project.ControlInicio import  Inicio, ControlInicio
from Dominio_project.ControlProjeto import Projeto, ControlProjeto
from Dominio_project.ControlQuemSomos import QuemSomos, ControlQuemSomos
import os

bp_admin = Blueprint('admin',__name__, url_prefix="/admin", template_folder= 'templates')

DIRETORIO = "static\\assets\\images\\downloads"

discionarioTelas = {
    'inicio' : 'inicio',
    'quemSomos' : 'quemSomos',
    'projetos' : 'projeto',
    'contato' : 'contato'
}

#region INICIO ADMINISTRADOR
@bp_admin.route("/", methods = ['POST' , 'GET'] )
@validarSessao
def homeAdmin():
    controlador = ControlInicio();    
    registro = controlador.SelectInicio();        
    return render_template("CadastroInicioAdminDesktop.html" , registro = registro, tela=discionarioTelas.get('inicio'))

@bp_admin.route("/modificarInicio", methods = ['POST'] )
@validarSessao
def modificarInicio():    
    if request.method == "POST":

        texto1 = request.form['texto1']
        titulo2 = request.form['titulo2']
        texto2 = request.form['texto2']
        texto3 = request.form['texto3']

        arquivo1 = request.files['arquivo-1']
        arquivo3 = request.files['arquivo-3']
        deveEditar = True;
        controlador = ControlInicio();
        if( arquivo1.filename == "" or arquivo3.filename == ""):
            objetoInicio = Inicio(id=1,imagem1="",imagem3="",descricaoImagem3="",descricaoImagem1="",texto1=texto1,texto2=texto2,texto3=texto3,titulo2=titulo2);
            controlador.UpdateSemImage(objetoInicio)
            deveEditar=False

        if(deveEditar == True):
            nome_imagem = "imagemInicio1."
            nome_imagem += arquivo1.filename.split(".")[1];        
            arquivo1.save(os.path.join(DIRETORIO, nome_imagem))

            nome_imagem2 = "imagemInicio2."
            nome_imagem2 += arquivo3.filename.split(".")[1];        
            arquivo3.save(os.path.join(DIRETORIO, nome_imagem2))

            objetoInicio = Inicio(id=1,imagem1=arquivo1,imagem3=arquivo3,descricaoImagem1=nome_imagem,descricaoImagem3=nome_imagem2,texto1=texto1,texto2=texto2,texto3=texto3,titulo2=titulo2);
            controlador.Update(objetoInicio);

    return redirect(url_for('admin.homeAdmin'));
#endregion

#region QUEM SOMOS ADMINISTRADOR

@bp_admin.route("/AdmQuemSomos" )
@validarSessao
def AdmQuemSomos():
    controlador = ControlQuemSomos();
    registro = controlador.SelectId();
    return render_template("CadastroQuemSomosAdminDesktop.html", registro = registro , tela=discionarioTelas.get('quemSomos'))

@bp_admin.route("/modificarQuemSomos", methods = ['POST'] )
@validarSessao
def modificarQuemSomos():
    if request.method == "POST":
        titulo1 = request.form['titulo1']
        texto1 = request.form['texto1']
        texto2 = request.form['texto2']
        controlador = ControlQuemSomos();
        imagem2 = request.files['arquivo-2']

        if( imagem2.filename != ""):    
            nome_imagem = "imagemQuemSomos."
            nome_imagem += imagem2.filename.split(".")[1];        
            imagem2.save(os.path.join(DIRETORIO, nome_imagem))
            objetoQuemSomos = QuemSomos(descricaoImagem2=nome_imagem,imagem2=imagem2,texto1=texto1,texto2=texto2,titulo1=titulo1,id=1);
            controlador.Update(objetoQuemSomos);
        else:
            objetoQuemSomos = QuemSomos(descricaoImagem2="",imagem2="",texto1=texto1,texto2=texto2,titulo1=titulo1,id=1);
            controlador.UpdateSemImagem(objetoQuemSomos);

    return redirect(url_for('admin.AdmQuemSomos'));

#endregion

#region PROJETOS ADMINISTRADOS
@bp_admin.route("/AdmProjetos" )
@validarSessao
def AdmProjetos():
    controlador = ControlProjeto();
    registro = controlador.SelectAll();
    return render_template("ViewProjetosAdminDesktop.html", registro = registro ,tela=discionarioTelas.get('projetos'))

@bp_admin.route("/telaCadastroProjetos")
@validarSessao
def telaCadastroProjetos(id):
    controlador = ControlProjeto();
    if(id != 0):
        projeto = controlador.SelectId(id);
    else:
        projeto = Projeto(data=datetime.now(),nome="",descricao="",descricaoImagem="",imagem="",id=id);

    return render_template("CadastroProjetosAdminDesktop.html", dados = projeto ,tela=discionarioTelas.get('projetos'))

@bp_admin.route("/cadastroEmBancoDeProjeto", methods = ['POST'] )
@validarSessao
def cadastroEmBancoDeProjeto():
    if request.method == "POST":
        
        id = request.form['id_projeto']
        titulo = request.form['titulo']
        descricao = request.form['descricao']        
        imagem = request.files['arquivo-1']
        banco = ControlProjeto();
        
        if( imagem.filename != ""):    
            nome_imagem = "imagemProjeto."
            nome_imagem += imagem.filename.split(".")[1];        
            imagem.save(os.path.join(DIRETORIO, nome_imagem))

            objetoProjeto = Projeto(data=datetime.now() ,descricao=descricao,nome=titulo,imagem=imagem,descricaoImagem=nome_imagem,id=id);
            if id == "0":
                banco.Insert(objetoProjeto);
        else:
            objetoProjeto = Projeto(data=datetime.now() ,descricao=descricao,nome=titulo,imagem="",descricaoImagem="",id=id);
            
        
        if id != "0" and imagem.filename =="":
            banco.UpdateSemImagem(projeto=objetoProjeto);
        else:
            banco.Update(projeto=objetoProjeto);

    return redirect(url_for('admin.AdmProjetos'));

@bp_admin.route("/deletarEditarInserirProjeto",methods = ['POST'])
@validarSessao
def deletarEditarInserirProjeto():
    tipo = request.form['tipo']
    idProjeto = request.form['id_projeto']   

    if tipo == "Adicionar Novo":
        return telaCadastroProjetos(id=0);        

    if tipo =="Editar":
        return telaCadastroProjetos(id=idProjeto);

    if tipo =="Excluir":
        banco = ControlProjeto();
        banco.Drop(idProjeto);
    return redirect(url_for('admin.AdmProjetos'));
#endregion

#region CONTATO ADMINISTRADOR
@bp_admin.route("/AdmContato" )
@validarSessao
def AdmContato():
    controlador = ControlContato();
    dados = controlador.SelectAll();
    return render_template("ViewContatoAdminDesktop.html",dados=dados, tela=discionarioTelas.get('contato'))

@bp_admin.route("/visualizarContato", methods = ['POST'])
@validarSessao
def visualizarContato():
    if request.method == "POST":
        id = request.form['id']
        controlador = ControlContato();
        contato = controlador.SelectId(id);
        return render_template("ViewContatoUnicoAdminDesktop.html",dados=contato, tela=discionarioTelas.get('contato'))
#endregion


    