import Link from 'next/link';
import { LayoutGrid, MessageCircle, User, Settings, ShieldCheck, Sparkles } from 'lucide-react';
import type { Route } from 'next';

type SidebarProps = {
  currentPath?: string;
};

type SidebarLink = {
  href: Route;
  label: string;
  icon: typeof LayoutGrid;
};

const links: SidebarLink[] = [
  { href: '/dashboard', label: 'Dashboard', icon: LayoutGrid },
  { href: '/chat', label: 'Chat', icon: MessageCircle },
  { href: '/profile', label: 'Profile', icon: User },
  { href: '/settings', label: 'Settings', icon: Settings },
  { href: '/admin', label: 'Admin', icon: ShieldCheck }
];

export function Sidebar({ currentPath = '/dashboard' }: SidebarProps) {
  return (
    <aside className="hidden w-72 shrink-0 border-r border-slate-800 bg-slate-950/70 p-5 lg:flex lg:flex-col">
      <div className="mb-8 flex items-center gap-3 rounded-2xl border border-slate-800 bg-slate-900/70 p-3">
        <div className="rounded-2xl bg-cyan-500/15 p-2 text-cyan-400">
          <Sparkles size={18} />
        </div>
        <div>
          <p className="text-sm font-semibold text-slate-100">TechMart AI</p>
          <p className="text-xs text-slate-500">Customer Support</p>
        </div>
      </div>
      <nav className="space-y-2">
        {links.map((link) => {
          const Icon = link.icon;
          const active = currentPath === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              className={`flex items-center gap-3 rounded-xl px-3 py-3 text-sm transition ${active ? 'bg-cyan-500/15 text-cyan-300' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-100'}`}
            >
              <Icon size={16} />
              <span>{link.label}</span>
            </Link>
          );
        })}
      </nav>
      <div className="mt-auto rounded-2xl border border-slate-800 bg-slate-900/70 p-4 text-sm text-slate-400">
        <p className="font-medium text-slate-200">Need a human handoff?</p>
        <p className="mt-2">Escalations are routed automatically for high-priority complaints.</p>
      </div>
    </aside>
  );
}
