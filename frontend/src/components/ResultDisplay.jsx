// import { useNavigate } from "react-router-dom";

const ResultsDisplay = ({ result }) => {
  // const navigate = useNavigate();
  if (!result) return null;

  const { job_description, resume_analysis } = result;
  // const totalScore = resume_analysis?.total_score ?? 0;

  return (
    <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
      <h3 className="text-blue-600 text-xl font-semibold mb-4">
        Skill Breakdown
      </h3>

      {/* ─────── LISTS ───────────────────────────── */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Skills Required */}
        <div>
          <h4 className="text-green-600 font-semibold mb-1">
            Skills Required
          </h4>
          <ul className="list-disc list-inside text-sm max-h-52 overflow-y-auto pr-2">
            {job_description.skills.map((skill, i) => (
              <p key={i}>{skill}</p>
            ))}
          </ul>
        </div>

        {/* Matched + Missing */}
        <div>
          <div className="mb-6">
            <h4 className="text-green-600 font-semibold mb-1">
              Matched Skills
            </h4>
            {/* <ul className="list-disc list-inside text-sm max-h-24 overflow-y-auto pr-2">
              {resume_analysis.matched.it_skills.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul> */}
            <p className="text-sm">
              {resume_analysis.matched.it_skills.join(', ')}
            </p>
          </div>

          <div>
            <h4 className="text-red-600 font-semibold mb-1">
              Missing Skills
            </h4>
            <p className="text-sm">
              {resume_analysis.missing.it_skills.join(', ')}
            </p>
          </div>
        </div>
      </div>

      {/* ─────── ACTION BUTTONS ─────────────────── */}
      {/* <div className="mt-8 flex flex-col md:flex-row items-center gap-4">
        {/* Interview button (enabled when score ≥ 60) 
        <button
          className={`px-6 py-3 rounded-lg font-semibold transition
            ${totalScore >= 60
              ? "bg-emerald-600 hover:bg-emerald-700"
              : "bg-emerald-800/40 cursor-not-allowed"
            }`}
          onClick={() => navigate("/interview", { state: result })}
          disabled={totalScore < 60}
        >
          🚀&nbsp;Continue to Interview
        </button>

        {/* Upgrader button (enabled when score < 60) 
        <button
          className={`px-6 py-3 rounded-lg font-semibold transition
            ${totalScore < 60
              ? "bg-cyan-600 hover:bg-cyan-700"
              : "bg-cyan-800/40 cursor-not-allowed"
            }`}
          onClick={() => navigate("/upgrader", { state: result })}
          disabled={totalScore >= 60}
        >
          ✍️&nbsp;Improve my Resume
        </button>

        {/* helper text 
        <p className="text-sm text-gray-600">
          {totalScore >= 60
            ? "Looks good! You may proceed to interview."
            : "We suggest refining your resume first."}
        </p>
      </div> */}
    </div>
  );
};

export default ResultsDisplay;
