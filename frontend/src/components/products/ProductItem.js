import React from 'react'

const ProductItem = ({product}) =>  {
    return (
       <div className="card">
           <img src={product.img} alt=""></img>
           <div className="card-body">
               <h2><b>{product.name}</b></h2>
               <h4>#{product.number}</h4>
               <p>({product.tags[0]}),({product.tags[1]}),({product.tags[2]})</p>
           </div>
       </div>
    )
    
}

export default ProductItem
