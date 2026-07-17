import { clsx } from 'clsx';
import { InputHTMLAttributes } from 'react';

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label?: string;
  error?: string;
};

export function Input({ label, error, className, ...props }: InputProps) {
  return (
    <div className="w-full">
      {label ? <label className="mb-2 block text-sm font-medium text-slate-300">{label}</label> : null}
      <input
        {...props}
        className={clsx(
          'w-full rounded-xl border border-slate-700 bg-slate-900/80 px-4 py-3 text-sm text-slate-100 outline-none transition focus:border-cyan-400 focus:ring-2 focus:ring-cyan-500/20',
          error && 'border-red-500 focus:border-red-500 focus:ring-red-500/20',
          className
        )}
      />
      {error ? <p className="mt-2 text-sm text-red-400">{error}</p> : null}
    </div>
  );
}
