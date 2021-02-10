import { useState } from 'react'

const AddProduct = ({ onAdd }) => {
    const [name, setName] = useState('')
    const [number, setNumber] = useState('')
    const [tags, setTags] = useState([''])
    const [img, setImg] = useState('')

    const onSubmit = (e) => {
        e.preventDefault()
        
        if (!name) {
            alert('Please add a name')
            return
        }

        onAdd({ name, number, tags, img })

        setName('')
        setNumber('')
        setTags([''])
        setImg('')
    }

    return (
        <form className='add-form' onSubmit={onSubmit}>
            <div className='form-control'>
                <label>Name</label>
                <input 
                type='text' 
                placeholder='Enter Name'
                value={name}
                onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div className='form-control'>
                <label>Number</label>
                <input 
                type='text' 
                placeholder='Enter Number'
                value={number}
                onChange={(e) => setNumber(e.target.value)}
                />
            </div>
            <div className='form-control'>
                <label>Tags</label>
                <input 
                type='text' 
                placeholder='Enter Tags Seperated By Comma'
                value={tags}
                onChange={(e) => setTags(e.target.value.split(','))}
                />
            </div>
            <div className='form-control'>
                <label>Image</label>
                <input 
                type='text' 
                placeholder='Image'
                value={img}
                onChange={(e) => setImg(e.target.value)}
                />
            </div>
            <input type='submit' value='Save Product' className='btn btn-block'/>
        </form>        
    
    )
}

export default AddProduct
