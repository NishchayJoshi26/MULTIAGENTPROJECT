import { clsx } from 'clsx';
import { ReactNode } from 'react';

type CardProps = {
  children: ReactNode;
  className?: string;
  padded?: boolean;
};

export function Card({ children, className, padded = true }: CardProps) {
  return (
    <div className={clsx('rounded-2xl border border-slate-800 bg-slate-900/70 shadow-xl shadow-slate-950/30 backdrop-blur', padded ? 'p-6' : 'p-0', className)}>
      {children}
    </div>
  );
}
