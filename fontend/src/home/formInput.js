import React from "react";
import CRUD from "../services/crud";
import { Form, FormGroup, Button, Input, Label } from "reactstrap";

function FormInput(props) {
  const [postData, setPostData] = React.useState({
    
    customer_name: "",
    contact_name: "",
    address: "",
    city: "Da Nang",
    postal_code: "45000",
    country: "VN",
  });

  function handleChangeCustomerName(e) {
    e.preventDefault();
    setPostData({ ...postData, customer_name: e.target.value }); 
  }
  function handleChangeContactName(e) {
    e.preventDefault();
    setPostData({ ...postData, contact_name: e.target.value }); 
  }
  function handleChangeAddress(e) {
    e.preventDefault();
    setPostData({ ...postData, address: e.target.value });
  }

  function handleOnClickSubmit(e) {

    e.preventDefault();
    
  }

  return (
    <form>
      <input
        type="text"
        name="customerID"
        value={postData.customer_name}
        onChange={handleChangeCustomerName}
        placeholder="ID"
      />
      <input
        type="text"
        name="customerName"
        value={postData.customer_name}
        onChange={handleChangeCustomerName}
        placeholder="Customer Name"
      />
      <input
        type="text"
        name="contactName"
        value={postData.contact_name}
        onChange={handleChangeContactName}
        placeholder="Contact Name"
      />
      <input
        type="text"
        name="address"
        value={postData.address}
        onChange={handleChangeAddress}
        placeholder="Address"
      />
      <input type="text" name="city" value={postData.city} placeholder="City" />
      <input type="text" name="postalCode" value={postData.postal_code} placeholder="PostalCode" />
      <input type="text" name="country" value={postData.country} />
      <button name="btnSubmit" value="Submit" onClick={handleOnClickSubmit}>
        Submit{" "}
      </button>
    </form>
  );
  
}
export default FormInput;
