# ft_linear_regression

A (very) basic linear regression using gradient descent.

For fun, I extracted the data of appartment transactions in Paris, available on the French's government [website](https://www.data.gouv.fr/fr/datasets/5c4ae55a634f4117716d5656/#_).
I extracted data for the appartments using the following commands :
`cat valeursfoncieres-2018.txt | grep -i "750[1-9][1-9]|Paris.*appartement" | cut -d "|" -f 11,28 | awf -F "|" '$2'!=""' | sed "s/,/./g" | sed "s/|,"/g`

See attached subject in ./doc

## About

## Usage
