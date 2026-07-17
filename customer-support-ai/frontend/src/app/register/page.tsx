import Link from 'next/link';
import { Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';

export default function RegisterPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-[radial-gradient(circle_at_top,_rgba(34,211,238,0.18),_transparent_40%),linear-gradient(135deg,_#020617,_#111827)] px-4 py-10">
      <Card className="w-full max-w-md border-slate-800/80">
        <div className="mb-6 flex items-center gap-3">
          <div className="rounded-2xl bg-fuchsia-500/15 p-2 text-fuchsia-400">
            <Sparkles size={20} />
          </div>
          <div>
            <h1 className="text-xl font-semibold text-slate-100">Create your workspace</h1>
            <p className="text-sm text-slate-400">Start your AI support experience</p>
          </div>
        </div>
        <div className="space-y-4">
          <Input label="Full name" placeholder="Ava Chen" />
          <Input label="Email" type="email" placeholder="ava@company.com" />
          <Input label="Password" type="password" placeholder="••••••••" />
          <Button fullWidth>Start free trial</Button>
          <p className="text-center text-sm text-slate-400">
            Already have an account? <Link href="/login" className="text-cyan-400">Sign in</Link>
          </p>
        </div>
      </Card>
    </main>
  );
}
