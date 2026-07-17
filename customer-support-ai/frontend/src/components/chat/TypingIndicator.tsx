export function TypingIndicator() {
  return (
    <div className="mb-4 flex justify-start">
      <div className="flex items-center gap-2 rounded-2xl border border-slate-800 bg-slate-900/80 px-4 py-3">
        <span className="h-2 w-2 animate-bounce rounded-full bg-cyan-400 [animation-delay:-0.2s]" />
        <span className="h-2 w-2 animate-bounce rounded-full bg-cyan-400 [animation-delay:-0.1s]" />
        <span className="h-2 w-2 animate-bounce rounded-full bg-cyan-400" />
      </div>
    </div>
  );
}
