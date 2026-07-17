export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 px-6 text-slate-100">
      <div className="max-w-3xl rounded-3xl border border-slate-800 bg-slate-900/70 p-10 shadow-2xl backdrop-blur">
        <p className="mb-4 text-sm uppercase tracking-[0.35em] text-cyan-400">Phase 1 scaffold</p>
        <h1 className="text-4xl font-semibold sm:text-5xl">TechMart Support AI</h1>
        <p className="mt-5 text-lg text-slate-300">
          This initial scaffold establishes the repository structure, frontend/backend configuration, logging, environment templates, and deployment files for the multi-agent support platform.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <span className="rounded-full border border-cyan-500/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
            Next.js + Tailwind
          </span>
          <span className="rounded-full border border-fuchsia-500/30 bg-fuchsia-500/10 px-4 py-2 text-sm text-fuchsia-300">
            FastAPI + MongoDB placeholders
          </span>
          <span className="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-4 py-2 text-sm text-emerald-300">
            Phase 1 complete
          </span>
        </div>
      </div>
    </main>
  );
}
