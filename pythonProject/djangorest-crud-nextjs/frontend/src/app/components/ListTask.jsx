import TaskCard from "./TaskCard";

async function loadTask() {
    const response = await fetch(`${process.env.BACKEND_URL}/api/tasks/`);
    const tasks = await response.json();
    return tasks;
}

async function ListTask() {

  const tasks = await loadTask();  
  // console.log(tasks);
    return (
      <div className="bg-slate-700 p-4 w-full rounded-md">
        <h1>Tasks List</h1>
        {tasks.map((task) => (
          <TaskCard key={task.id} task={task} />
        ))}
      </div>
    );
  }

  export default ListTask;
  