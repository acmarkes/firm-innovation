# Machine Learning Aplicado à Propensão a Inovar das Empresas Latinoamericanas 

A inovação é o motor do desenvolvimento econômico, social e sustentável dos países, mobilizando significativos recursos dos setores privado e público. Neste trabalho, nós utilizamos algoritmos de aprendizado de máquina para construir um modelo preditivo de se uma firma irá inovar. Desenvolvemos esse modelo para cinco países da América do Sul e atingimos uma precisão de 90%. Se restringirmos a análise a inovações que transcendem ao nível da firma, atingimos 97% de precisão para as empresas que não inovam, o que permite filtrar a maior parte das empresas que não irão promover inovação em nível setorial, nacional ou global.

## How to Run

1. Clone este repositório
2. Crie um ambiente com Python==3.8 e [PyCaret](https://pycaret.gitbook.io/docs/)==2.3
3. Faça o download do [dataset](https://publications.iadb.org/en/harmonized-latin-american-innovation-surveys-database-lais-firm-level-microdata-study-innovation) 
4. Extraia o arquivo *zip* e copie "LAIS_public.csv" para a pasta data/raw
5. Execute o notebook "inovacao-firmas.ipynb"
