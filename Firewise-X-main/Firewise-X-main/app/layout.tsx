import type { Metadata, Viewport } from "next";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  themeColor: "#060b17",
};

export const metadata: Metadata = {
  title: "FIREWISE-X | NASA Space Apps Challenge 2026",
  description: "Evidence-Grounded Research Engine for Microgravity Fire Safety (NASA BASS-II PSI-25)",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body>{children}</body>
    </html>
  );
}
