import { motion } from 'framer-motion';
import { MessageBubble } from './MessageBubble';
import { TypingIndicator } from './TypingIndicator';

type ChatMessage = {
  id: number;
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
};

type ChatWindowProps = {
  messages: ChatMessage[];
  isTyping?: boolean;
};

export function ChatWindow({ messages, isTyping = false }: ChatWindowProps) {
  return (
    <motion.div initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} className="flex h-[65vh] flex-col overflow-hidden rounded-3xl border border-slate-800 bg-slate-950/70 p-4">
      <div className="flex-1 overflow-y-auto px-2 py-2">
        {messages.map((message) => (
          <MessageBubble key={message.id} role={message.role} content={message.content} timestamp={message.timestamp} />
        ))}
        {isTyping ? <TypingIndicator /> : null}
      </div>
    </motion.div>
  );
}
