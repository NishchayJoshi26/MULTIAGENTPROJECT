import { Inbox } from 'lucide-react';

type EmptyStateProps = {
  title: string;
  description: string;
};

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-slate-800 bg-slate-900/40 px-8 py-12 text-center">
      <div className="rounded-full bg-slate-800 p-3 text-slate-400">
        <Inbox size={24} />
      </div>
      <h3 className="mt-4 text-lg font-semibold text-slate-200">{title}</h3>
      <p className="mt-2 max-w-sm text-sm text-slate-400">{description}</p>
    </div>
  );
}
