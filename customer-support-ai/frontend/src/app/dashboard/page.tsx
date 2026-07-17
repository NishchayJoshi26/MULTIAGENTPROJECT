import { ArrowUpRight, Bot, MessageSquare, Users, Zap } from 'lucide-react';
import Link from 'next/link';
import { Sidebar } from '@/components/layout/Sidebar';
import { Card } from '@/components/ui/Card';

const metrics = [
  { title: 'Active sessions', value: '184', icon: MessageSquare, tone: 'text-cyan-400' },
  { title: 'Avg. response', value: '1.2s', icon: Zap, tone: 'text-fuchsia-400' },
  { title: 'Human escalations', value: '12', icon: Users, tone: 'text-emerald-400' }
];

export default function DashboardPage() {
  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentPath="/dashboard" />
      <main className="flex-1 p-6 lg:p-8">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Overview</p>
            <h1 className="text-3xl font-semibold">Customer support operations</h1>
          </div>
          <Link href="/chat" className="rounded-2xl border border-cyan-500/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
            Open support workspace
          </Link>
        </div>
        <div className="grid gap-4 md:grid-cols-3">
          {metrics.map((metric) => {
            const Icon = metric.icon;
            return (
              <Card key={metric.title} className="border-slate-800/80">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-slate-400">{metric.title}</p>
                    <p className="mt-2 text-2xl font-semibold text-slate-100">{metric.value}</p>
                  </div>
                  <div className={`rounded-2xl bg-slate-800/80 p-3 ${metric.tone}`}>
                    <Icon size={20} />
                  </div>
                </div>
              </Card>
            );
          })}
        </div>
        <div className="mt-6 grid gap-6 xl:grid-cols-[1.4fr_0.8fr]">
          <Card className="border-slate-800/80">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-semibold text-slate-100">Live support insights</h2>
              <span className="rounded-full border border-emerald-500/20 bg-emerald-500/10 px-3 py-1 text-sm text-emerald-400">Healthy</span>
            </div>
            <div className="mt-6 rounded-2xl border border-slate-800 bg-slate-950/70 p-5">
              <div className="flex items-start gap-3">
                <div className="rounded-2xl bg-cyan-500/15 p-2 text-cyan-400">
                  <Bot size={18} />
                </div>
                <div>
                  <p className="font-medium text-slate-100">Multi-agent routing is active</p>
                  <p className="mt-2 text-sm text-slate-400">This mock dashboard shows the support surface for billing, technical, product, complaint, and FAQ agents.</p>
                </div>
              </div>
            </div>
          </Card>
          <Card className="border-slate-800/80">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-semibold text-slate-100">Recommended actions</h2>
              <ArrowUpRight size={18} className="text-cyan-400" />
            </div>
            <ul className="mt-4 space-y-3 text-sm text-slate-400">
              <li className="rounded-xl border border-slate-800 bg-slate-950/70 px-4 py-3">Review billing escalations from the last hour.</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/70 px-4 py-3">Validate refund policy answers for the FAQ agent.</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/70 px-4 py-3">Create a knowledge-base update for warranty claims.</li>
            </ul>
          </Card>
        </div>
      </main>
    </div>
  );
}
