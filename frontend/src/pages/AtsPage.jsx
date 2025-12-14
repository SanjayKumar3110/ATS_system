import { useState } from "react";
import UploadForm from "../components/UploadForm";
import ResultsDisplay from "../components/ResultDisplay";
import { PieChart, Pie, Cell, Tooltip } from "recharts";

const COLORS = ["#00C49F", "#FF8042", "#FFBB28", "#8884d8"];

export default function AtsPage() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const totalScore = result?.resume_analysis?.total_score ?? 0;
  const suggestUpgrader = totalScore < 60;

  // Helper to format AI response (Markdown-style bold to HTML)
  const formatAIResponse = (text) => {
    if (!text) return null;
    return text.split('\n').map((line, index) => {
      const trimmedLine = line.trim();
      if (!trimmedLine) return <div key={index} className="h-2" />;

      // Check for standalone heading (e.g., "**Heading**" or "**Heading:**")
      const headingMatch = trimmedLine.match(/^\*\*(.*?)\*\*[:]?$/);
      if (headingMatch) {
        return (
          <h3 key={index} className="text-lg font-bold text-gray-900 mt-5 mb-2">
            {headingMatch[1]}
          </h3>
        );
      }

      // Parse inline bold text
      const parts = line.split(/(\*\*.*?\*\*)/g);
      return (
        <p key={index} className="mb-2 text-gray-700 leading-relaxed">
          {parts.map((part, i) => {
            if (part.startsWith('**') && part.endsWith('**')) {
              return (
                <strong key={i} className="font-bold text-gray-900">
                  {part.slice(2, -2)}
                </strong>
              );
            }
            return part;
          })}
        </p>
      );
    });
  };

  return (
    <div className="min-h-screen p-6 bg-gray-50 text-gray-900 space-y-10 font-sans">
      <h1 className="text-4xl font-extrabold text-center mb-6 text-gray-800 tracking-tight">
        AI Resume Matcher (ATS)
      </h1>

      {loading ? (
        <div className="flex flex-col items-center justify-center min-h-[50vh]">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-600 mb-6"></div>
          <p className="text-xl font-semibold text-gray-700 animate-pulse">
            Analyzing Resume & Job Description...
          </p>
        </div>
      ) : !result ? (
        <div className="flex flex-col items-center justify-center min-h-[60vh]">
          <div className="w-full max-w-2xl">
            <p className="text-center text-gray-600 mb-8 text-lg">
              Upload your resume and a job description to get an instant match score and improvement tips.
            </p>
            <UploadForm setResult={setResult} setLoading={setLoading} />
          </div>
        </div>
      ) : (
        <div className="space-y-8 animate-fade-in">
          {/* DASHBOARD GRID */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

            {/* LEFT COLUMN: Score & Chart */}
            <div className="space-y-6">
              <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-200">
                <h3 className="text-gray-800 text-2xl font-bold mb-6 border-b pb-2 border-gray-100">
                  Final Score Overview
                </h3>
                <button onClick={() => setResult(null)}
                  className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg shadow-sm text-gray-700 font-medium hover:bg-gray-50 hover:text-blue-600 transition"
                >
                  ← Analyze New Resume
                </button>
                <div className="flex flex-col items-center">
                  <PieChart width={500} height={300}>
                    <Pie
                      dataKey="value"
                      data={[
                        {
                          name: "IT Skills",
                          value: result.resume_analysis.score.it_skills,
                        },
                        {
                          name: "Soft Skills",
                          value: result.resume_analysis.score.soft_skills,
                        },
                        {
                          name: "Education",
                          value: result.resume_analysis.score.education,
                        },
                        {
                          name: "Experience",
                          value: result.resume_analysis.score.experience,
                        },
                      ]}
                      innerRadius={60}
                      outerRadius={100}
                      paddingAngle={5}
                      label={({ name, percent }) =>
                        `${name}: ${(percent * 100).toFixed(0)}%`
                      }
                    >
                      {COLORS.map((c, i) => (
                        <Cell key={i} fill={c} stroke="none" />
                      ))}
                    </Pie>
                    <Tooltip
                      contentStyle={{ backgroundColor: '#fff', borderRadius: '8px', border: '1px solid #e5e7eb', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)' }}
                      itemStyle={{ color: '#374151' }}
                    />
                  </PieChart>

                  <div className="mt-6 w-full grid grid-cols-2 gap-4 text-sm">
                    <div className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                      <span className="flex items-center gap-2 font-medium text-gray-700">
                        <span className="w-3 h-3 rounded-full bg-[#00C49F]"></span> IT Skills
                      </span>
                      <span className="font-bold text-gray-900">{result.resume_analysis.score.it_skills}%</span>
                    </div>
                    <div className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                      <span className="flex items-center gap-2 font-medium text-gray-700">
                        <span className="w-3 h-3 rounded-full bg-[#FF8042]"></span> Soft Skills
                      </span>
                      <span className="font-bold text-gray-900">{result.resume_analysis.score.soft_skills}%</span>
                    </div>
                    <div className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                      <span className="flex items-center gap-2 font-medium text-gray-700">
                        <span className="w-3 h-3 rounded-full bg-[#FFBB28]"></span> Education
                      </span>
                      <span className="font-bold text-gray-900">{result.resume_analysis.score.education}%</span>
                    </div>
                    <div className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                      <span className="flex items-center gap-2 font-medium text-gray-700">
                        <span className="w-3 h-3 rounded-full bg-[#8884d8]"></span> Experience
                      </span>
                      <span className="font-bold text-gray-900">{result.resume_analysis.score.experience}%</span>
                    </div>
                  </div>

                  <div className="mt-8 text-center">
                    <p className="text-4xl font-black text-gray-800">
                      {totalScore}%
                    </p>
                    <p className="text-sm text-gray-500 mt-1 font-medium uppercase tracking-wide">Total Match Score</p>
                    <p className="text-sm text-gray-500 mt-4 px-4">
                      {suggestUpgrader
                        ? "Score is below 60. We recommend to imporve resume."
                        : "Great score! You are ready for the interview."}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            {/* RIGHT COLUMN: JD & Skills */}
            <div className="space-y-6">
              {/* JD Box */}


              <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-200 max-h-[400px] overflow-y-auto custom-scrollbar">
                <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                  📄 Extracted Job Description
                </h2>

                <p className="text-sm leading-relaxed whitespace-pre-line text-gray-600">
                  {result.job_description.cleaned_jd}
                </p>
              </div>

              {/* Skill Breakdown */}
              <ResultsDisplay result={result} />
            </div>
          </div>

          {/* SUMMARY SECTION */}
          {result.ai_analysis && result.ai_analysis.detailed_review && (
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-200">
              <h3 className="text-gray-800 text-2xl font-bold mb-6 border-b pb-2 border-gray-100">
                Detail Summary
              </h3>
              <div className="prose max-w-none">
                {formatAIResponse(result.ai_analysis.detailed_review)}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

