import axios from "axios";

const instance = axios.create({
  baseURL: "https://ats-system-uylp.onrender.com",
});

export default instance;
