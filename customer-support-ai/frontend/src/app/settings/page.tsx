import { Sidebar } from '@/components/layout/Sidebar';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

export default function SettingsPage() {
  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentPath="/settings" />
      <main className="flex-1 p-6 lg:p-8">
        <h1 className="text-3xl font-semibold">Settings</h1>
        <p className="mt-2 text-sm text-slate-400">Configure the experience and operational preferences.</p>
        <div className="mt-6 space-y-4">
          <Card>
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-lg font-semibold">Theme</h2>
                <p className="text-sm text-slate-400">Switch between dark and light experiences.</p>
              </div>
              <Button variant="secondary">Toggle theme</Button>
            </div>
          </Card>
          <Card>
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-lg font-semibold">Notifications</h2>
                <p className="text-sm text-slate-400">Receive updates for updates and tickets.</p>
              </div>
              <Button variant="secondary">Manage</Button>
            </div>
          </Card>
        </div>
      </main>
    </div>
  );
}
