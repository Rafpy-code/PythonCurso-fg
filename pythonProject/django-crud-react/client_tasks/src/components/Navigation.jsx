import { Link } from 'react-router-dom'

export function Navigation() {
    return (
        <div>
            <Link to={'/tasks'}><h1>Task App</h1></Link>
            <nav className="navigation">
                <ul>
                    <Link to={'/tasks-create'}>Create task</Link>
                </ul>
            </nav>
        </div>
    )
}
