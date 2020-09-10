// in src/App.js
import * as React from "react";
import { Admin, Resource } from "react-admin";
import { ContactList, ContactEdit, ContactCreate } from './Contacts';
import DataProvider from './DataProvider';

// const dataProvider = jsonServerProvider("http://jsonplaceholder.typicode.com");
// const dataProvider = jsonServerProvider("http://localhost:5000/api");
const App = () => (
  <Admin dataProvider={DataProvider}>
    <Resource name="contacts" list={ContactList} edit={ContactEdit} create={ContactCreate} />
  </Admin>
);
export default App;
