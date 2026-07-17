import { CheckCircle2, AlertCircle } from 'lucide-react';

type ToastProps = {
  title: string;
  message: string;
  type?: 'success' | 'error';
};

export function Toast({ title, message, type = 'success' }: ToastProps) {
  const icon = type === 'success' ? <CheckCircle2 size={18} /> : <AlertCircle size={18} />;
  const tone = type === 'success' ? 'border-emerald-500/30 bg-emerald-500/10 text-emerald-300' : 'border-red-500/30 bg-red-500/10 text-red-300';

  return (
    <div className={`flex items-start gap-3 rounded-2xl border px-4 py-3 shadow-lg ${tone}`}>
      <div className="mt-0.5">{icon}</div>
      <div>
        <p className="font-medium">{title}</p>
        <p className="text-sm opacity-90">{message}</p>
      </div>
    </div>
  );
}
