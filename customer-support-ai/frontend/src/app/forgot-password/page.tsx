import Link from 'next/link';
import { RefreshCw } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';

export default function ForgotPasswordPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-[radial-gradient(circle_at_top,_rgba(14,165,233,0.18),_transparent_40%),linear-gradient(135deg,_#020617,_#111827)] px-4 py-10">
      <Card className="w-full max-w-md border-slate-800/80">
        <div className="mb-6 flex items-center gap-3">
          <div className="rounded-2xl bg-emerald-500/15 p-2 text-emerald-400">
            <RefreshCw size={20} />
          </div>
          <div>
            <h1 className="text-xl font-semibold text-slate-100">Reset password</h1>
            <p className="text-sm text-slate-400">We’ll send a secure reset link</p>
          </div>
        </div>
        <div className="space-y-4">
          <Input label="Email" type="email" placeholder="you@company.com" />
          <Button fullWidth>Send reset link</Button>
          <p className="text-center text-sm text-slate-400">
            <Link href="/login" className="text-cyan-400">Back to sign in</Link>
          </p>
        </div>
      </Card>
    </main>
  );
}
