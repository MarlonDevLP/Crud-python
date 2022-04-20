### `Cadastro`
#### Verifica 
*  CPF informado é válido
*  Email existe o `@`
*  Nome verdadeiro *(sem numeros e caracteres especiais)*
*  Senha tem um tamanho igual à seis
> *Se as condições anteriores forem verdadeiras, o cadastro é criado e o cliente ganha um limite de `R$1000`*
### `Login`
#### Verifica 
* Se existe clientes cadastrados
* CPF e Email informado é válido e está cadastrado
* Se a senha informada é válida
>  *Se as condições anteriores forem verdadeiras, o cliente tem duas opções:*
> * *Comprar*
> * *Pagar a fatura*
### `Comprar`
* É possivel comprar do *Item1* até o *Item20*
* Ver todos os produtos da loja
* Ver o carrinho
* Se o limite chegar à 0 fica impossibilitado de comprar
### `Pagar Divida`
* Essa função permite pagar a divida e voltar ao saldo inicial `R$1000`
* Caso o cliente esteja com o saldo inicial, emite uma mensagem dizendo que não há nenhuma divida pendente.

