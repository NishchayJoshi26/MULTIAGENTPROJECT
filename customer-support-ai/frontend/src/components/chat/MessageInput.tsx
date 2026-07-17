import { Send } from 'lucide-react';
import { Button } from '../ui/Button';

type MessageInputProps = {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
};

export function MessageInput({ value, onChange, onSend }: MessageInputProps) {
  return (
    <div className="flex items-center gap-3 rounded-2xl border border-slate-800 bg-slate-900/70 p-3">
      <input
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Ask about billing, installation, products, or complaints"
        className="flex-1 bg-transparent px-2 py-2 text-sm text-slate-100 outline-none"
      />
      <Button variant="primary" className="rounded-xl" onClick={onSend}>
        <Send size={16} />
      </Button>
    </div>
  );
}
