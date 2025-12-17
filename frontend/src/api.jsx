import axios from "axios";

const instance = axios.create({
  // URL is not specified then it will run on local host
  // If error occurs remove process.env.REACT_APP_API_URL 
  // and keep only "http://127.0.0.1:8000"
  // baseURL: process.env.REACT_APP_API_URL || "http://127.0.0.1:8000",
  baseURL: "http://127.0.0.1:8000",
});

export default instance;
