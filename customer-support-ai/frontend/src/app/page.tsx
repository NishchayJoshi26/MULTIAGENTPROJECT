import Link from 'next/link';
import { ArrowRight, Bot, ShieldCheck, Sparkles, Zap } from 'lucide-react';
import { Navbar } from '@/components/ui/Navbar';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';

const features = [
  { title: 'Multi-agent routing', description: 'Billing, technical, product, complaint, and FAQ agents work together.', icon: Bot },
  { title: 'Enterprise-grade UX', description: 'Polished support experience with responsive, accessible UI.', icon: ShieldCheck },
  { title: 'Real-time support', description: 'Typing indicators, streaming-ready chat, and instant feedback flows.', icon: Zap }
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(6,182,212,0.2),_transparent_40%),linear-gradient(135deg,_#020617,_#111827)] text-slate-100">
      <Navbar />
      <section className="mx-auto flex max-w-7xl flex-col items-center px-6 py-20 text-center lg:py-28">
        <div className="rounded-full border border-cyan-500/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
          <span className="mr-2 inline-flex items-center"><Sparkles size={14} /></span>
          Phase 2 frontend preview
        </div>
        <h1 className="mt-8 max-w-4xl text-4xl font-semibold leading-tight sm:text-6xl">
          Enterprise AI customer support, designed for modern teams.
        </h1>
        <p className="mt-6 max-w-2xl text-lg text-slate-400">
          A polished SaaS experience with a multi-agent support workspace, conversation history, responsive layouts, and modern dashboards.
        </p>
        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <Button>
            <Link href="/register" className="flex items-center gap-2">Get started <ArrowRight size={16} /></Link>
          </Button>
          <Button variant="secondary">
            <Link href="/dashboard">View dashboard</Link>
          </Button>
        </div>
      </section>
      <section className="mx-auto max-w-7xl px-6 pb-20">
        <div className="grid gap-6 md:grid-cols-3">
          {features.map((feature) => {
            const Icon = feature.icon;
            return (
              <Card key={feature.title}>
                <div className="w-fit rounded-2xl bg-slate-800/70 p-3 text-cyan-400">
                  <Icon size={18} />
                </div>
                <h2 className="mt-4 text-lg font-semibold text-slate-100">{feature.title}</h2>
                <p className="mt-2 text-sm text-slate-400">{feature.description}</p>
              </Card>
            );
          })}
        </div>
      </section>
    </main>
  );
}
