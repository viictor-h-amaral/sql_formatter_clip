SQL FORMATTER


from:
select nome, CPF
cidade
FROM funcionarios inner JOIN funcionario_enderecos
where funcionários.situacao = 'ATIVO'

to:
select
	nome,
	cpf,
	cidade
from
	funcionarios
	inner join funcionario_enderecos
where
	funcionários.situcao = 'ATIVO'




step 0: identificar que o conteúdo de entrada é, de fato, um sql (via de regra, contém cláusulas select e from)
step 1: concatenar todo o texto em uma linha só.
step 2: trocar múltiplos espaços consecutivos (exemplo: "  ") por espaço único
step 3: transformar o texto sql para minúsculo. Adendo: não pode mexer nos textos entre aspas simples.
step 4.1: varrer texto à procura de palavras chave: select, from, where, order by, group by, having, limit, with, inner/left/outer/right join
step 4.2: para cada palavra chave, tratar corretamente: 
		4.2.1 todas palavras chave precisam ficar sozinhas em suas linhas
		4.2.2 palavras chave como select, from, where, group by, having, order by sempre necessitam de "enter" antes e depois de aparecerem
		4.2.3 palavras chave como limit, inner/left/outer/right join apenas necessitam de "enter" antes. O que vem depois varia
		4.2.4 palavras chave de operadores lógicos como and, or, not possuem comportamentos a depender do grupo em que estão. Por exemplo, o and e or no escopo do where sempre pulam uma linha. Já no escopo de um on de um 
			join, and e or não pulam linha

		