'use client'
import { useRouter } from "next/navigation";
import { useState } from "react"
// probar en lugar de router.refresh() que no va

function TaskCard({task}) {

    const router = useRouter();
    const [editing, setEditing] = useState(false);
    const [newTitle, setNewTitle] = useState(task.title);
    const [newDescription, setNewDescription] = useState(task.description);

    const handleDone = async (id) => {
        const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/tasks/${id}/done/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({done: !task.done})
        })
        .then(response => {
            if (response.status === 200) {
                console.log('Task updated successfully');
                // router.push('/');
                router.refresh()
            } else {
                console.log('Failed to update task');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this task?')) {
            // Delete the task
            const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/tasks/${id}`, {
                method: 'DELETE'
            })
            router.refresh();
        }
    }

    const handleUpdate = async (id) => {
        const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/tasks/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({title: newTitle, description: newDescription})
        });
        const data = await response.json();
        setNewTitle(data.title);
        setNewDescription(data.description);
        setEditing(!editing);
        router.refresh();
    }

    return (
        <div 
            className="bg-slate-500 text-slate-200 px-4 py-3 mb-2 rounded-md text-slate-200 flex justify-between items-center"
        >
            <div className="flex flex-col">
              {!editing ? (
              <h2 className="font-bold">
                {newTitle}
                {task.done && <span>🎯</span>}
              </h2>
              ) : (
              <input
                type="text"
                placeholder={task.title}
                autoFocus
                className="border-none outline-none bg-slate-500 p-2 text-green-300"
                onChange={(e) => setNewTitle(e.target.value)}
              />
              )}

              {
                !editing ? (
                  <p>{newDescription}</p>
                ) : (
                  <textarea
                    placeholder={task.description}
                    className="border-none ouline-none bg-slate-700 p-2 text-green-300 w-full"
                    rows={1}
                    onChange={(e) => setNewDescription(e.target.value)}
                  />
                )
              }              
            </div>
            
            <div className="flex justify-between gap-x-2">
              {
                editing ? (
                  <button
                    className="bg-purple-500 text-white rounded-md p-2"
                    onClick={() => handleUpdate(task.id)}
                  >Save changes</button>
                ) : null
              }

              <button
                className= {
                  (task.done ? "text-white rounded-md p-2 bg-green-500" : "text-white rounded-md p-2 bg-orange-500")
                }
                onClick={() => handleDone(task.id)}
              >{
                task.done ? "Done" : "Undone"}
              </button>

              <button 
                className="bg-indigo-500 text-white rounded-md p-2"
                onClick={() => setEditing(!editing)}
              >Update</button>

              <button
                className="bg-red-500 text-white rounded-md p-2"
                onClick={() => handleDelete(task.id)}
              >Delete</button>
            </div>
          </div>
    )
}

export default TaskCard;


  

// .then(response => {
//   console.log(response);
//     if (response.status === 204) {
//         console.log('Task deleted successfully');
//         router.replace('/');
//         router.refresh()
//     } else {
//         console.log('Failed to delete task');
//     }
    
// })
// .catch(error => console.error('Error:', error));
