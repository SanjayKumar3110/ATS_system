const ResultsDisplay = ({ result }) => {
  if (!result) return null;
  const { job_description, resume_analysis } = result;

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
            <ul className="list-disc list-inside text-sm max-h-24 overflow-y-auto pr-2">
              {resume_analysis.matched.it_skills.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul>
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
    </div>
  );
};

export default ResultsDisplay;
