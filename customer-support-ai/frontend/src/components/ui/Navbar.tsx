"use client";

import Link from 'next/link';
import { Moon, Sun, Menu } from 'lucide-react';
import { Button } from './Button';
import { useTheme } from '@/context/ThemeContext';

export function Navbar() {
  const { isDark, toggleTheme } = useTheme();

  return (
    <header className="border-b border-slate-800 bg-slate-950/80 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <Link href="/" className="text-lg font-semibold text-slate-100">
          TechMart Support AI
        </Link>
        <div className="flex items-center gap-3">
          <Button variant="ghost" className="hidden sm:inline-flex" onClick={toggleTheme}>
            {isDark ? <Sun size={16} /> : <Moon size={16} />}
          </Button>
          <Button variant="secondary" className="hidden sm:inline-flex">
            <Link href="/login">Sign In</Link>
          </Button>
          <Button>
            <Link href="/register">Get Started</Link>
          </Button>
          <button className="rounded-xl border border-slate-800 p-2 text-slate-300 sm:hidden">
            <Menu size={18} />
          </button>
        </div>
      </div>
    </header>
  );
}
