import Link from 'next/link';
import { Button } from '@/components/ui/Button';

export default function NotFound() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 text-slate-100">
      <div className="max-w-md text-center">
        <p className="text-sm uppercase tracking-[0.35em] text-cyan-400">404</p>
        <h1 className="mt-3 text-4xl font-semibold">Page not found</h1>
        <p className="mt-3 text-sm text-slate-400">The resource you are looking for doesn’t exist or has moved.</p>
        <div className="mt-6 flex justify-center">
          <Button>
            <Link href="/">Return home</Link>
          </Button>
        </div>
      </div>
    </main>
  );
}
