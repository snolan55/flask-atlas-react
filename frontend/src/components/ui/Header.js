import React from 'react'
import Button from './Button'

const Header = ({onAdd, showAdd}) => {
    return (
        <header>
            <h1>Warehouse</h1>
                <Button
                    color={showAdd ? 'red' : 'green'}
                    text={showAdd ? 'Close' : 'Add'}
                    onClick={onAdd}
                />
        </header>

        
    )
}

export default Header
