import { Link } from 'react-router-dom'

export function Navigation() {
    return (
        <div>
        <div className='flex justify-between py-3'>
            <Link to={'/tasks'}>
                <h1 className='text-purple-800 font-bold text-4xl mb-4'>Task App</h1>
            </Link>
            <button className="bg-purple-800 text-white px-3 py-2 rounded-lg">
                <Link to={'/tasks-create'}>Create task</Link>
            </button>
        </div>
        <hr className='mb-4 border-t-4 border-purple-800' />
        </div>
    )
}
