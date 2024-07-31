'use client'
import { useRouter } from "next/navigation";
import { useState } from "react";

function FormTask() {

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const router = useRouter();

    const handleSubmit = async (e) => {
        e.preventDefault();
        // console.log(title, description);
        const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/tasks/`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({title, description})
            }
        )
        const data = await response.json();  
        console.log(data);
        router.refresh();
    };

    return (
      <div className="bg-slate-200 p-7 h-fit rounded-md">
        <form onSubmit={handleSubmit}>
            <h1 className="text-black font-bold">Añadir tarea</h1>

            <label 
                htmlFor="title"
                className="text-black text-xs"
            >Título</label>
            <input 
                type="text" 
                name="title" 
                className="bg-slate-400 rounded-md p-2 mb-2 block w-full text-slate-900"
                onChange={(e) => setTitle(e.target.value)}
            />

            <label 
                htmlFor="description"
                className="text-black text-xs"
            >Descripción</label>
            <textarea 
                name="description"
                className="bg-slate-400 rounded-md p-2 mb-2 block w-full text-slate-900"
                onChange={(e) => setDescription(e.target.value)}
            ></textarea>

            <button
                className="bg-indigo-500 p-3 rounded-md mt-4 hover:bg-indigo-700 text-white w-full"
            >Save</button>
        </form>        
      </div>
    );
  }

  export default FormTask;
