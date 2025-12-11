import { BrowserRouter, Routes, Route } from "react-router-dom";
import AtsPage from "./pages/AtsPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AtsPage />} />
      </Routes>
    </BrowserRouter>
  );
}
