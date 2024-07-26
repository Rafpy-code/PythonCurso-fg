import { useEffect } from "react";
import { useForm } from "react-hook-form"
import { createTask, updateTask, deleteTask, getTask, } from "../api/tasks.api";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-hot-toast";

export function TaskFormPage() {

    const { register, 
            handleSubmit, 
            formState: { errors },
            setValue
        } = useForm();

    const navigate = useNavigate();
    const params = useParams();
    // console.log(params);

    const onSubmit = handleSubmit(async data => {
        if (params.id) {
            console.log("Updating");
            await updateTask(params.id, data);
            toast.success("Task updated", {
                position: "bottom-right",
                style: {
                    background: "#239208",
                    color: "#FFFFFF",
                }
            });
        } else {
            console.log("Creating");        
            await createTask(data);
            toast.success("Task created", {
                position: "bottom-right",
                style: {
                    background: "#239208",
                    color: "#FFFFFF",
                }
            });
        }
        navigate("/tasks");
    });

    useEffect(() => {
        async function loadTask() {
            if (params.id) {
                console.log("Fetching");
                const response = await getTask(params.id);
                console.log(response.data);
                setValue("title", response.data.title);
                setValue("description", response.data.description);
                setValue("created", response.data.createdAt);
                setValue("done", response.data.done);
            }
        }
        loadTask();
    }, [])

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit}>
                <input 
                    type="text"
                    placeholder="Title"
                    {...register("title", { required: true})}
                    className="bg-purple-700 text-white p-3 rounded-lg block w-full mb-3"
                />
                {errors.title && <span>Title is required</span>}
                
                <textarea 
                    placeholder="Description"
                    {...register("description", { required: true})}
                    className="bg-purple-700 text-white p-3 rounded-lg block w-full mb-3"
                ></textarea>
                {errors.description && <span>Description is required</span>}
                <input type="hidden" name="" {...register("created")}/>
                <div className="flex justify-between bg-purple-700 text-white rounded-lg p-3 mt-3 mb-3 block w-full">Done   <input 
                        type="checkbox"
                        {...register("done")} 
                    /> 
                </div>                             
            </form>
            {/* Uso el operador ternario para saber si es update o create */}
            {params.id ? (
                <div className="flex justify-between">
                    <button 
                        onClick={onSubmit}
                        className="bg-orange-600 text-white px-3 py-2 rounded-lg w-48"
                    >Update</button>
                    <button 
                        className="bg-red-800 text-white px-3 py-2 rounded-lg w-48"
                        onClick={async () => {
                            const accepted = window.confirm("Are you sure?");
                            if (!accepted) return;
                            await deleteTask(params.id);
                            toast.success("Task deleted", {
                                position: "bottom-right",
                                style: {
                                    background: "#239208",
                                    color: "#FFFFFF",
                                }
                            });
                            navigate("/tasks");
                        }}
                    >Delete</button>
                </div>
            ) : <button 
                    className="bg-purple-800 text-white p-3 rounded-lg block w-full mt-3"
                    onClick={onSubmit}
                >Save</button>}
        </div>
    )
}