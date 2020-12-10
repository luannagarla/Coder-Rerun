# Navegador da web
Lucas é um cara muito radical quando se trata de licenças de software. Desde o início da graduação em engenharia da computação, ele busca desenvolver todas as ferramentas de que necessita. Tudo isso começou após experiências ruins com softwares proprietários. Agora ele acredita que um verdadeiro programador deve ser autossuficiente, ou seja, ele deve construir todos os programas de que precisa, desde uma simples calculadora até seu próprio sistema operacional.

Neste semestre, Lucas está cursando o curso de desenvolvimento de sistemas web. Para dar continuidade à sua filosofia de vida, usando apenas softwares que ele mesmo construiu, Lucas já está programando seu próprio navegador. Muito do trabalho foi concluído, mas algumas funcionalidades ainda precisam ser concluídas.

O navegador de Lucas possui um campo de busca onde o usuário pode inserir uma palavra-chave, e clicando no botão de confirmação irá redirecionar para outra página com os resultados de sua busca. Quando alguma string é inserida no campo de busca, Lucas deseja que seu programa exiba, abaixo, algumas opções para autocompletar esta string de acordo com as buscas já realizadas pelo usuário.

Por exemplo, se as palavras "algoritmos" e "algas" já foram pesquisadas, ao digitar a string "alg", o programa deve sugerir as palavras "algoritmos" e "algas". Portanto, para cada string inserida, o programa deve sugerir palavras pesquisadas anteriormente e prefixadas com esta string. Se alguma palavra for igual à string digitada, ela também deve ser sugerida.

Lucas está preocupado com a quantidade de palavras que seu programa pode sugerir e o tamanho máximo que elas podem atingir. Então ele pediu que você o ajudasse a escrever um programa onde dadas algumas palavras já pesquisadas e uma série de consultas compostas por uma string, indique quantas palavras o navegador deve sugerir ao usuário, e o comprimento da maior dessas palavras.

# Entrada
A entrada é composta por vários casos de teste. A primeira linha de um caso de teste possui um inteiro N (1 ≤ N ≤ 10 ^ 4) indicando o número de palavras que já foram pesquisadas pelo programa de Lucas. Cada uma das próximas N linhas contém uma string não vazia de no máximo 100 letras minúsculas [a - z]. Para cada caso de teste, N palavras são diferentes. Em seguida, haverá um inteiro Q (1 ≤ Q ≤ 100) indicando o número de consultas. Cada uma das próximas Q linhas descreve uma consulta com uma string não vazia de no máximo 100 letras minúsculas [a - z], representando uma string inserida no campo de pesquisa.

# Resultado
Para cada caso de teste, imprima Q linhas, onde a i-ésima linha é a resposta à i-ésima consulta. A resposta de cada consulta deve ser composta por dois inteiros separados por espaço, representando, respectivamente, o número de palavras sugeridas pelo programa ao inserir a string indicada pela i-ésima consulta, e o comprimento da maior palavra contida naquele subconjunto. Se nenhuma palavra for sugerida, imprima -1. Imprima uma linha em branco no final de cada caso de teste.

