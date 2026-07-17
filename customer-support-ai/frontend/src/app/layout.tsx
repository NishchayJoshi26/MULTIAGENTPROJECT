import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'TechMart Support AI',
  description: 'Enterprise multi-agent customer support assistant scaffold'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
