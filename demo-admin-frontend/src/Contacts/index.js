// in src/Contacts
import * as React from "react";
import { Filter, List, Datagrid, TextField, Edit, SimpleForm, TextInput, Create } from 'react-admin';

const ContactFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="q" alwaysOn />
    </Filter>
);

export const ContactList = props => (
    <List filters={<ContactFilter />} {...props}>
        <Datagrid rowClick="edit">
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="company_name" />
            <TextField source="phone_number" />
        </Datagrid>
    </List>
);

export const ContactEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <TextInput source="company_name" />
            <TextInput source="phone_number" />
        </SimpleForm>
    </Edit>
);

export const ContactCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <TextInput source="company_name" />
            <TextInput source="phone_number" />
        </SimpleForm>
    </Create>
);