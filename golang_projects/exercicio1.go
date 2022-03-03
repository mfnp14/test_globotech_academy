package main

import "fmt"

type cliente struct {
	nome  string
	email string
}

type produto struct {
	nome  string
	preco float32
	qtd   int
}

type carrinho struct {
	cliente
	produtos []produto
}

func (c *carrinho) add2Cart(prod produto) {
	c.produtos = append(c.produtos, prod)
}

func main() {

	banana := produto{
		nome:  "banana",
		preco: 0.50,
		qtd:   4,
	}
	cereal := produto{
		nome:  "cereal",
		preco: 7.50,
		qtd:   1,
	}
	carrot := produto{
		nome:  "carrot",
		preco: 0.75,
		qtd:   4,
	}

	cart := carrinho{
		cliente: cliente{
			nome:  "Jose",
			email: "jose@email.com",
		},
		produtos: []produto{},
	}

	// add products to the shopping cart
	cp := &cart
	cp.add2Cart(banana)
	cp.add2Cart(cereal)
	cp.add2Cart(carrot)

	var total float32
	for _, e := range cart.produtos {
		total += float32(e.qtd) * e.preco
	}

	fmt.Printf("Hello, %s.\nYour cart contains the following items:\n", cart.cliente.nome)
	for _, e := range cart.produtos {
		fmt.Printf("%s\tx%d\n", e.nome, e.qtd)
	}
	//fmt.Println(cart)
	fmt.Printf("\nThe total cost will be $%.2f", total)
}
