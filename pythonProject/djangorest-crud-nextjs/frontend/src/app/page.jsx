import ListTask from "./components/ListTask";
import FormTask from "./components/FormTask";

export const dynamic = 'force-dynamic';


function HomePage() {
  return (
    <div className="container mx-auto">
      <h1 className="m-3 text-xl">Task App con Next.js</h1>
      <div className="flex gap-x-10">
        <FormTask />
        <ListTask />
      </div>
    </div>
  );
}

export default HomePage;
