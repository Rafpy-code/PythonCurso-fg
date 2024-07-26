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
        <div>
            <form onSubmit={onSubmit}>
                <input 
                    type="text"
                    placeholder="Title"
                    {...register("title", { required: true})} 
                />
                {errors.title && <span>Title is required</span>}
                
                <textarea 
                    placeholder="Description"
                    {...register("description", { required: true})}
                ></textarea>
                {errors.description && <span>Description is required</span>}
                <input type="hidden" name="" {...register("created")}/>
                Done <input type="checkbox" name="" id="" {...register("done")} />                              
            </form>
            {/* Uso el operador ternario para saber si es update o create */}
            {params.id ? (
                <div>
                    <button onClick={onSubmit}>Update</button>
                    <button 
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
            ) : <button onClick={onSubmit}>Save</button>}
        </div>
    )
}