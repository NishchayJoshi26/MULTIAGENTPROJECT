import { clsx } from 'clsx';

type MessageBubbleProps = {
  role: 'user' | 'assistant';
  content: string;
  timestamp?: string;
};

export function MessageBubble({ role, content, timestamp }: MessageBubbleProps) {
  return (
    <div className={clsx('mb-4 flex', role === 'user' ? 'justify-end' : 'justify-start')}>
      <div className={clsx('max-w-[80%] rounded-2xl px-4 py-3 text-sm shadow', role === 'user' ? 'bg-cyan-500 text-white' : 'border border-slate-800 bg-slate-900/80 text-slate-200')}>
        <p className="whitespace-pre-wrap leading-6">{content}</p>
        {timestamp ? <p className={clsx('mt-2 text-[11px]', role === 'user' ? 'text-cyan-100/70' : 'text-slate-500')}>{timestamp}</p> : null}
      </div>
    </div>
  );
}
