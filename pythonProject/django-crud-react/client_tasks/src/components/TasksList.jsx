import { useState, useEffect } from "react";
import { getAllTasks } from "../api/tasks.api";
import { TaskCard } from "./TaskCard";

export function TasksList() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        async function loadTasks() {
            try {
                const response = await getAllTasks();
                // Extrae el array de tareas de la propiedad `results`
                const tasksArray = response.data.results;
                // Verifica que `tasksArray` sea un array antes de actualizar el estado
                if (Array.isArray(tasksArray)) {
                    setTasks(tasksArray);
                } else {
                    console.error('Expected `results` to be an array but received:', tasksArray);
                    setTasks([]); // Establece un valor por defecto si no es un array
                }
            } catch (error) {
                console.error('Error fetching tasks:', error);
                setTasks([]); // Establece un valor por defecto en caso de error
            }
        }

        loadTasks();
    }, []);

    return (
        <div>
            {tasks.map(task => (
                <TaskCard key={task.id} task={task} />
            ))}
        </div>
    );
}
