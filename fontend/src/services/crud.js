import HttpRequest from "./http-common";

const getAll = async () => {
  return await HttpRequest.get("http://localhost:8080/customer/all_Customer'");
};

const create = (data) => {
  return HttpRequest.post("http://localhost:8080/customer/insert", data);
};

const deleteOne = (id) => {
  return HttpRequest.delete(`http://localhost:8080//customer/delete/${id}`);
};

const updateOne = (id, data) => {
  return HttpRequest.put(`http://localhost:8080/customer/update/${id}`, data);
};
const methods = { getAll, create, deleteOne, updateOne }
export default methods;
