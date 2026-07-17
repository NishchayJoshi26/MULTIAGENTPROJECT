import { clsx } from 'clsx';
import { ReactNode } from 'react';

type ButtonProps = {
  children: ReactNode;
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
  fullWidth?: boolean;
  type?: 'button' | 'submit' | 'reset';
  onClick?: () => void;
};

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  className,
  fullWidth = false,
  type = 'button',
  onClick
}: ButtonProps) {
  const base = 'inline-flex items-center justify-center rounded-xl font-medium transition focus:outline-none focus:ring-2 focus:ring-cyan-400/60 disabled:cursor-not-allowed disabled:opacity-60';
  const variants = {
    primary: 'bg-cyan-500 text-white hover:bg-cyan-400 shadow-lg shadow-cyan-500/20',
    secondary: 'bg-slate-800 text-slate-100 hover:bg-slate-700 border border-slate-700',
    ghost: 'bg-transparent text-slate-300 hover:bg-slate-800'
  };
  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2.5 text-sm',
    lg: 'px-6 py-3 text-base'
  };

  return (
    <button type={type} onClick={onClick} className={clsx(base, variants[variant], sizes[size], fullWidth && 'w-full', className)}>
      {children}
    </button>
  );
}
