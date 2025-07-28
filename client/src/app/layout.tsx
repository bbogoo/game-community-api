import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";

export const metadata = {
  title: "YourSiteName",
  description: "게임 랭킹 & 커뮤니티 사이트",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <body className="flex flex-col min-h-screen">
        <Header />

        {/* 페이지 콘텐츠 영역 */}
        <main className="flex-grow">{children}</main>

        <Footer />
      </body>
    </html>
  );
}
