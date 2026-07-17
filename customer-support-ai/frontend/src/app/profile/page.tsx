import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { Sidebar } from '@/components/layout/Sidebar';

export default function ProfilePage() {
  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentPath="/profile" />
      <main className="flex-1 p-6 lg:p-8">
        <h1 className="text-3xl font-semibold">Profile</h1>
        <p className="mt-2 text-sm text-slate-400">Manage your account details and role preferences.</p>
        <div className="mt-6 grid gap-6 lg:grid-cols-[1fr_0.6fr]">
          <Card>
            <div className="flex items-center gap-4">
              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-500/15 text-2xl font-semibold text-cyan-400">AC</div>
              <div>
                <h2 className="text-xl font-semibold">Ava Chen</h2>
                <p className="text-sm text-slate-400">Operations Lead · Premium Customer</p>
              </div>
            </div>
            <div className="mt-6 grid gap-4 sm:grid-cols-2">
              <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4">
                <p className="text-sm text-slate-400">Email</p>
                <p className="mt-1 text-sm text-slate-100">ava@techmart.com</p>
              </div>
              <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4">
                <p className="text-sm text-slate-400">Region</p>
                <p className="mt-1 text-sm text-slate-100">North America</p>
              </div>
            </div>
          </Card>
          <Card>
            <h2 className="text-lg font-semibold">Preferences</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-400">
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">Dark mode enabled</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">Email summaries enabled</li>
              <li className="rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">Auto-escalation on high priority complaints</li>
            </ul>
            <Button className="mt-6">Update profile</Button>
          </Card>
        </div>
      </main>
    </div>
  );
}
