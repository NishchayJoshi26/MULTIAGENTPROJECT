import Link from 'next/link';
import { ArrowRight, ShieldCheck } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';

export default function LoginPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-[radial-gradient(circle_at_top,_rgba(6,182,212,0.16),_transparent_45%),linear-gradient(135deg,_#020617,_#111827)] px-4 py-10">
      <Card className="w-full max-w-md border-slate-800/80">
        <div className="mb-6 flex items-center gap-3">
          <div className="rounded-2xl bg-cyan-500/15 p-2 text-cyan-400">
            <ShieldCheck size={20} />
          </div>
          <div>
            <h1 className="text-xl font-semibold text-slate-100">Welcome back</h1>
            <p className="text-sm text-slate-400">Sign in to your support workspace</p>
          </div>
        </div>
        <div className="space-y-4">
          <Input label="Email" type="email" placeholder="you@company.com" />
          <Input label="Password" type="password" placeholder="••••••••" />
          <Button fullWidth className="mt-2">
            Continue <ArrowRight size={16} className="ml-2" />
          </Button>
          <div className="flex items-center justify-between text-sm text-slate-400">
            <Link href="/forgot-password" className="hover:text-cyan-400">Forgot password?</Link>
            <Link href="/register" className="hover:text-cyan-400">Create account</Link>
          </div>
        </div>
      </Card>
    </main>
  );
}
