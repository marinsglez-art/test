import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { TableProvider } from "./contexts/TableContext";
import Appointment from "./pages/Appointment";
import Availability from "./pages/Availability";
import User from "./pages/User";

function App() {
  return (
    <TableProvider>
      <div className="app-container">
        <main className="app-main">
          <Routes>
            <Route path="/appointment" element={<Appointment />} />
            <Route path="/availability" element={<Availability />} />
            <Route path="/user" element={<User />} />
            <Route path="/" element={<Navigate to="/appointment" replace />} />
            <Route path="*" element={<Navigate to="/appointment" replace />} />
          </Routes>
        </main>
      </div>
    </TableProvider>
  );
}
export default App;
