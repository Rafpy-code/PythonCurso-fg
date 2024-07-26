import { useNavigate } from "react-router-dom";
import { format } from 'date-fns';

const FechaFormateada = ({created}) => {
  const formattedDate = format(created, 'dd/MM/yyyy HH:mm:ss');

  return (
    <div>
      <p>Create at: {formattedDate}</p>
    </div>
  );
};

export function TaskCard({ task }) {

    const navigate = useNavigate();

    return (        
        <div className="bg-purple-800 text-white p-3 hover:bg-orange-600 hover:cursor-pointer rounded-lg"            
            onClick={() => navigate(`/tasks/${task.id}`)}
        > 
            {/* <h3>Id: {task.id}</h3> */}
            <h1 className="font-bold uppercase">{task.title}</h1>
            <p className="text-lime-300">{task.description}</p>
            <p className="text-lime-300">{<FechaFormateada created={task.created} />}</p>
            {task.done ? (
                <p className="text-lime-300">Task ={">"} <span className="text-white">Done</span></p>) : <p className="text-lime-600">Task ={">"} <span className="text-white">Pending</span></p>
            }
        </div>
    );
}
