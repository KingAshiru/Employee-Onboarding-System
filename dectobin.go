package main

import (
	"fmt"	
	"strconv"
)

var number int64

func main(){
	//This program converts a decimal number to it's binary equivalent
	fmt.Println("This program converts a decimal number to it's binary equivalent")
	fmt.Println("Please enter a number:")
	fmt.Scan(&number)
	fmt.Println(strconv.FormatInt(number,2))
}	

