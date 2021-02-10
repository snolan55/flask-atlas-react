import React from 'react'
import ProductItem from './ProductItem'

const ProductGrid = ({products, isLoading}) => {
    return isLoading ? (
    <h1>Loading...</h1>
    ) : (
    <section className="cards">
        {products.map((product, index) => (
            <ProductItem key={index} product={product}></ProductItem>
            ))}
    </section>)
}

export default ProductGrid
