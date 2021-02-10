import React, { useState, useEffect} from 'react'
import axios from 'axios'
import Header from './components/ui/Header'
import Search from './components/ui/Search'
import ProductGrid from './components/products/ProductGrid'
import AddProduct from './components/products/AddProduct'
import './App.css';

const App = () => {
  const [products, setProducts] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [query, setQuery] = useState('')
  const [showAddProduct, setShowAddProduct] = useState(false)

  useEffect(() =>{
    const fetchProducts = async () => {
      setIsLoading(true)
      const result = await axios.get(`http://127.0.0.1:5000/products/?query=${query}`)
      console.log(result.data)
      setProducts(result.data)
      setIsLoading(false)
    }

    fetchProducts()
  }, [query])

  const addProduct = async (product) => {
    const res = await axios({
      method: 'post',
      url: 'http://127.0.0.1:5000/products/',
      headers: {
        'Content-type': 'application/json',
      },
      data: JSON.stringify(product),
    })

    const data = await res.data

    setProducts([...products, data])
  }

  return (
    <div className='container'>
      <Header 
        onAdd={() => setShowAddProduct(!showAddProduct)}
        showAdd={showAddProduct}
      />
      {showAddProduct && <AddProduct onAdd={addProduct} />}
      <Search getQuery={(q) => setQuery(q)}/>
      <ProductGrid isLoading={isLoading} products={products} />
    </div>
  )
}

export default App;
