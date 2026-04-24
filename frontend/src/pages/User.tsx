import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const User: React.FC = () => {
  return (
    <div id="page-user-2">
    <div id="ifdkg" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="iwjt9" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="ix3r3" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="iitxe" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="i2ili" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/appointment">{"Appointment"}</a>
          <a id="in8vb" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/availability">{"Availability"}</a>
          <a id="i3d8v" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
        </div>
        <p id="izzy9" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="ijv7g" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="iqfwf" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"User"}</h1>
        <p id="iugt6" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage User data"}</p>
        <TableBlock id="table-user-2" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="User List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Role", "column_type": "field", "field": "role", "type": "str", "required": true}], "formColumns": [{"column_type": "field", "field": "role", "label": "role", "type": "str", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "appointment", "field": "appointment", "lookup_field": "clientName", "entity": "Appointment", "type": "str", "required": true}]}} dataBinding={{"entity": "User", "endpoint": "/user/"}} />
      </main>
    </div>    </div>
  );
};

export default User;
