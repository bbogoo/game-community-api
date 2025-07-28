"use client";

import Link from "next/link";

export default function Header() {
  return (
    <header className="bg-gray-900 text-white px-6 py-4 flex justify-between items-center shadow-md">
      <div className="text-xl font-bold">
        <Link href="/">SiteName</Link>
      </div>
      <nav className="space-x-6">
        <Link href="/games" className="hover:text-blue-400 transition">
          게임 랭킹
        </Link>
        <Link href="/community" className="hover:text-blue-400 transition">
          커뮤니티
        </Link>
        <Link href="/login" className="hover:text-blue-400 transition">
          로그인
        </Link>
      </nav>
    </header>
  );
}
