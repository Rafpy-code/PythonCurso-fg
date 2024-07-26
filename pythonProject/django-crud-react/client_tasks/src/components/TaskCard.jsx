import { useNavigate } from "react-router-dom";

export function TaskCard({ task }) {

    const navigate = useNavigate();

    return (        
        <div style={{background:'orange'}}            
            onClick={() => navigate(`/tasks/${task.id}`)}
        > 
            <h3>Id: {task.id}</h3>
            <h1>{task.title}</h1>
            <p>{task.description}</p>
            <p>{task.created}</p>
            {task.done ? (
                <p>Task ={">"} <span>Done</span></p>) : <p>Task ={">"} <span>Pending</span></p>
            }
            <hr />            
        </div>
    );
}