import CRUD from "../services/crud";
import React from "react";
import TableContent from "./tableContent";
import FormInput from "./formInput";


function Home() {
  const [listCustomers, setListCustomers] = React.useState([]);

  const RetrieveAllCustomers = () => {
    CRUD.getAll().then((res) => {
      console.log(res);
      setListCustomers(res.data.data);
    });
  };

  React.useEffect(() => {
    RetrieveAllCustomers();
  }, []);

  return (
    <>
      <TableContent items={listCustomers} />
      <FormInput />
    </>
  );
}
export default Home;
