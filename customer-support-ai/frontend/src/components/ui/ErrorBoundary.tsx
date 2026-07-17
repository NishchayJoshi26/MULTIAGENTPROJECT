"use client";

import { Component, ReactNode } from 'react';

type ErrorBoundaryProps = {
  children: ReactNode;
};

type ErrorBoundaryState = {
  hasError: boolean;
};

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex min-h-[40vh] items-center justify-center rounded-2xl border border-red-500/30 bg-red-500/10 p-8 text-center text-red-300">
          <div>
            <h2 className="text-xl font-semibold">Something went wrong.</h2>
            <p className="mt-2 text-sm">The UI component crashed unexpectedly. Please refresh the page.</p>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
