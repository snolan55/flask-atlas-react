import React, { useState } from 'react'

const Search = ({ getQuery }) => {
    const [text,setText] = useState('')

    const onChange = (q) => {
        setText(q)
        getQuery(q)
    }

    return (
        <section className='search'>
            <form>
                <label>Search </label>
                <input
                  type='text'
                  className='form-control'
                  placholder='Search Products'
                  value={text}
                  onChange={(e) => onChange(e.target.value)}
                  autoFocus
                />
            </form>
        </section>
    )
}

export default Search
