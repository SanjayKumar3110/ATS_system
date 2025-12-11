import { useState } from "react";
import axios from "../api";

const UploadForm = ({ setResult, setLoading }) => {
  const [file, setFile] = useState(null);
  const [jobData, setJobData] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    if (jobData.startsWith("http://") || jobData.startsWith("https://")) {
      formData.append("job_url", jobData);
    } else {
      formData.append("pasted_text", jobData);
    }

    if (setLoading) setLoading(true);
    try {
      const res = await axios.post("/ats/analyze", formData);
      setResult(res.data);
    } catch (err) {
      console.error("❌ ERROR:", err);
      alert("Upload failed: " + err.message);
    } finally {
      if (setLoading) setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-xl shadow-md space-y-4 w-full max-w-lg mx-auto border border-gray-200">
      <label className="block font-semibold">Upload Resume (PDF/JPEG/PNG)</label>
      <input
        type="file"
        accept=".pdf,.jpg,.jpeg,.png"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full p-2 border border-gray-300 bg-white text-gray-900 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
        required
      />

      <label className="block font-semibold">Paste Job Description Or Job Link</label>
      <input
        className="w-full p-2 bg-white text-gray-900 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
        placeholder="https://www.linkedin.com/jobs/view/..."
        value={jobData}
        onChange={(e) => setJobData(e.target.value)}
      />

      <button
        type="submit"
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Analyze Resume
      </button>
    </form>
  );
};

export default UploadForm;
