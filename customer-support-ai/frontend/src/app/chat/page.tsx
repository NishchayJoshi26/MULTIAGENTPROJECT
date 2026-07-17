"use client";

import { useState } from 'react';
import { Sidebar } from '@/components/layout/Sidebar';
import { ChatWindow } from '@/components/chat/ChatWindow';
import { MessageInput } from '@/components/chat/MessageInput';
import { Card } from '@/components/ui/Card';

const initialMessages = [
  {
    id: 1,
    role: 'assistant' as const,
    content: 'Hello! I can help you with billing, installation, product questions, complaints, or general FAQ support.',
    timestamp: '09:30'
  },
  {
    id: 2,
    role: 'user' as const,
    content: 'My premium subscription is still locked after payment.',
    timestamp: '09:31'
  }
];

export default function ChatPage() {
  const [messages, setMessages] = useState(initialMessages);
  const [draft, setDraft] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  const handleSend = () => {
    if (!draft.trim()) return;
    setMessages((prev) => [
      ...prev,
      { id: prev.length + 1, role: 'user', content: draft, timestamp: 'Now' }
    ]);
    setDraft('');
    setIsTyping(true);
    setTimeout(() => setIsTyping(false), 1200);
  };

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentPath="/chat" />
      <main className="flex-1 p-4 lg:p-8">
        <div className="mb-4 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Support Workspace</p>
            <h1 className="text-2xl font-semibold">Multi-agent conversation</h1>
          </div>
        </div>
        <Card className="border-slate-800/80 p-0">
          <div className="p-4">
            <ChatWindow messages={messages} isTyping={isTyping} />
            <div className="mt-4">
              <MessageInput value={draft} onChange={setDraft} onSend={handleSend} />
            </div>
          </div>
        </Card>
      </main>
    </div>
  );
}
