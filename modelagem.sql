create database codevance;

use codevance;

create table fornecedores (
	id int auto_increment not null,
    razao_social varchar(500) not null,
    cnpj varchar(14) not null,
    email varchar (100),
    senha varchar(500) not null,
    primary key (id)
);

create table parcelas (
	id int auto_increment not null,
    id_fornecedor int not null,
    data_emissao datetime default current_timestamp,
    data_vencimento date not null,
    data_vencimento_nova date,
    valor_original decimal(10, 2) not null,
    valor_novo decimal(10, 2),
    primary key (id),
    constraint id_fornecedor foreign key (id_fornecedor) references fornecedores (id)
);

create table logs (
	id int auto_increment not null,
    id_parcelas int not null,
    estado varchar(22) not null,
    primary key (id),
    constraint id_parcelas foreign key (id_parcelas) references parcelas (id),
    constraint estado check (estado in ('Disponivel', 'Indisponivel', 'Aguardando Confirmacao', 'Antecipado', 'Negado'))
);

select * from fornecedores;
select * from parcelas;
select * from logs;
select * from django_migrations;

drop table fornecedores;
drop table parcelas;
drop table logs;
drop table auth_group;
drop table auth_group_permissions;
drop table auth_permission;
drop table auth_user;
drop table auth_user_groups;
drop table auth_user_user_permissions;
drop table django_admin_log;
drop table django_content_type;
drop table django_migrations;
drop table django_session;

insert into fornecedores (razao_social, cnpj, email) values ('Empresa Teste 1', '00000000000100', 'empresateste1@email.com');
insert into parcelas (id_fornecedor, data_vencimento, valor_original) values ('1', '2022-08-30', 1000.00);
insert into logs (id_parcelas, estado) values ('1', 'Aguardando Confirmacao');