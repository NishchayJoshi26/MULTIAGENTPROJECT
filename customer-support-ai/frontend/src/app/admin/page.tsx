import { Sidebar } from '@/components/layout/Sidebar';
import { Card } from '@/components/ui/Card';

const analytics = [
  { label: 'Total users', value: '3,214' },
  { label: 'Escalations', value: '54' },
  { label: 'Satisfaction', value: '94%' },
  { label: 'Knowledge base docs', value: '132' }
];

export default function AdminPage() {
  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentPath="/admin" />
      <main className="flex-1 p-6 lg:p-8">
        <h1 className="text-3xl font-semibold">Admin dashboard</h1>
        <p className="mt-2 text-sm text-slate-400">Operational visibility for support leadership.</p>
        <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          {analytics.map((item) => (
            <Card key={item.label}>
              <p className="text-sm text-slate-400">{item.label}</p>
              <p className="mt-2 text-2xl font-semibold text-slate-100">{item.value}</p>
            </Card>
          ))}
        </div>
        <div className="mt-6 grid gap-6 lg:grid-cols-[1fr_0.8fr]">
          <Card>
            <h2 className="text-lg font-semibold">Recent activity</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-400">
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">Refund policy review completed</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">2 high-priority complaint tickets escalated</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">FAQ agent response confidence improved</li>
            </ul>
          </Card>
          <Card>
            <h2 className="text-lg font-semibold">System health</h2>
            <div className="mt-4 space-y-3 text-sm text-slate-400">
              <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-4 py-3 text-emerald-300">LLM gateway healthy</div>
              <div className="rounded-xl border border-cyan-500/20 bg-cyan-500/10 px-4 py-3 text-cyan-300">Vector store available</div>
              <div className="rounded-xl border border-fuchsia-500/20 bg-fuchsia-500/10 px-4 py-3 text-fuchsia-300">MongoDB connection placeholder ready</div>
            </div>
          </Card>
        </div>
      </main>
    </div>
  );
}
