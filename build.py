# CourtPan のサイト（サポート・プライバシーポリシー、日本語と英語）を作る。
# 本文は _inbox/courtzoom/appstore/privacy-policy.md（法務の案）を、確かめられない一文を除いて写したもの
import html
CSS = """
:root{--bg:#F4F1EC;--card:#FFFFFF;--ink:#1D232B;--ink-soft:#5E6773;--accent:#C0641E;--ok:#2F7D5B;--line:#E2DDD4}
@media (prefers-color-scheme: dark){:root{--bg:#14171B;--card:#1D2127;--ink:#E9EDF1;--ink-soft:#9AA4AF;--accent:#E88A45;--ok:#5BBF8E;--line:#2C323A}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.7;padding:24px 20px 64px;-webkit-font-smoothing:antialiased}
.wrap{max-width:720px;margin:0 auto}
header{margin:20px 0 28px}
h1{font-size:28px;line-height:1.2;font-weight:800}
.lead{margin-top:12px;font-size:17px;font-weight:600}
.date{margin-top:8px;font-size:13px;color:var(--ink-soft)}
.lang{float:right;font-size:13px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;display:flex;gap:14px}
.card+.card{margin-top:10px}
.pad{width:5px;border-radius:2.5px;flex:none;background:var(--ok)}
.body{flex:1;min-width:0}
.card h2{font-size:16px;margin-bottom:6px}
.card p,.card li{font-size:15px}
.card p+p,.card p+ul,.card ul+p{margin-top:8px}
.card ul{padding-left:1.2em}
.tw{overflow-x:auto;margin-top:8px}
table{border-collapse:collapse;width:100%;min-width:560px;font-size:14px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-top:1px solid var(--line)}
th{font-size:12.5px;color:var(--ink-soft);border-top:none}
a{color:var(--accent);font-weight:600;text-decoration:none}
a:hover{text-decoration:underline}
footer{margin-top:40px;text-align:center;color:var(--ink-soft);font-size:13px}
"""
def page(lang, title, desc, lead, date, sections, other, foot):
    cards = []
    for h, body in sections:
        cards.append(f'<div class="card"><div class="pad"></div><div class="body"><h2>{h}</h2>{body}</div></div>')
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{html.escape(desc)}"><style>{CSS}</style></head>
<body><div class="wrap"><header><a class="lang" href="{other[0]}">{other[1]}</a><h1>{title}</h1><p class="lead">{lead}</p>{f'<p class="date">{date}</p>' if date else ''}</header>
{''.join(cards)}
<footer>{foot}</footer></div></body></html>
"""
def tbl(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'
MAIL = '<a href="mailto:nosunosukawa@gmail.com">nosunosukawa@gmail.com</a>'
SELLER_JA = "Nobutaka Kawasaki（のす工房）"
SELLER_EN = "Nobutaka Kawasaki (Nosu Works)"

ja_priv = [
 ("1. 要点", "<ul><li>本アプリは、<b>動画の読み込み・解析・書き出しを、すべてお使いの Mac の中で行います。</b></li><li>本アプリは<b>自分ではインターネットに接続しません。</b>動画や解析の結果を、私たちや第三者のサーバーへ送ることはありません（購入・購入の復元・招待コードの入力のときだけ、macOS の App Store の仕組みが Apple と通信します。第3項）。</li><li>広告、アクセス解析、行動の追跡（トラッキング）の仕組みは入っていません。</li><li>アカウントの登録はありません。私たちが本アプリを通じてお客様の個人情報を受け取ることはありません。</li></ul>"),
 ("2. お使いの Mac の中で扱う情報", "<p>本アプリは次の情報を Mac の中に保存します。どれも Mac の外へは送りません。</p>" + tbl(["情報","保存する場所","消えるとき・消し方"],[
   ["お客様が選んだ動画の作業用の写し","本アプリ専用の保管場所（macOS が本アプリに割り当てるフォルダ）の一時フォルダ","処理が終わったとき、または次に本アプリを起動したときに自動で消します。元の動画は変更しません"],
   ["書き出した動画と結果（ハイライト、場面の一覧など）。結果のフォルダには、元の動画の場所（Mac のユーザー名を含むフォルダの名前）と入力したチーム名も記録します。結果のフォルダを人に渡すときはご注意ください","「ムービー」フォルダの中の「CourtPan」フォルダ","Finder、または本アプリの設定の「書き出した動画」から消せます"],
   ["検出結果の控え（選手とボールの位置など。同じ動画を作り直すときに使います）","本アプリ専用の保管場所","本アプリの設定の「保存した検出結果」から消せます"],
   ["会場の設定（コートの範囲など）","本アプリ専用の保管場所","本アプリの画面から消せます"],
   ["無料体験の記録（処理した動画を見分けるための、元に戻せない数字と回数。ファイル名は残しません）","Mac のキーチェーン","無料体験の回数を正しく数えるため、本アプリを削除しても残ります。キーチェーンアクセスで「com.nosunosukawa.courtpan.license」の項目を消すと消えます"],
   ["設定（最後に入力したチーム名を含む）","本アプリ専用の保管場所","本アプリを削除したときに、macOS の手順に従って消えます"]]) +
   "<p>動画には、選手・審判・観客などの人が映っていることがあります。本アプリはそれらを Mac の外へ送りません。撮影と、書き出した動画の公開・共有については、映っている方への配慮と、大会・会場の撮影の決まりの確認をお願いします。</p><p>本アプリは、処理が終わったことをお知らせする通知を出すことがあります（お客様が許可した場合）。通知は Mac の中だけで作られます。</p>"),
 ("3. 購入・購入の復元・招待コード（オファーコード）", "<p>本アプリの購入、購入の復元、オファーコードの入力は、Apple の App Store の仕組みで行われ、Apple が処理します。私たちは、お客様の氏名、Apple アカウント、支払いの情報を受け取りません。Apple が扱う情報については、<a href=\"https://www.apple.com/legal/privacy/\">Apple のプライバシーポリシー</a>をご覧ください。</p><p>私たちは App Store Connect を通じて、Apple から売上や利用状況の集計（個人を特定しない形のもの）を受け取ります。お客様が Apple にクラッシュ（異常終了）の報告や解析データの共有を許可している場合は、Apple を通じてその報告を受け取ることがあり、本アプリの不具合を直すためだけに使います。</p>"),
 ("4. お問い合わせ・招待コードの受け渡しで扱う情報（本アプリの外）", "<ul><li>お客様がメールでお問い合わせくださった場合、私たちはメールアドレスとお問い合わせの内容を受け取り、<b>お返事と、不具合の調査のためだけに</b>使います。</li><li>私たちが招待コードを直接お渡しした場合は、お渡しした方のお名前・連絡先と、お渡ししたコードの控えを、<b>コードの管理（重複や期限の確認）のためだけに</b>持ちます。</li><li>これらは、目的を果たしたあと、遅くとも2年で消します。</li><li>私たちはメールの受け取りと保管に Google LLC（米国）の Gmail を使っています。米国には、日本の個人情報保護法と同じ水準の包括的な個人情報保護の法律はなく、州ごとの法律などがあります。</li></ul>"),
 ("5. 第三者への提供", "<p>私たちは、法令に基づく場合を除き、お客様の個人情報を第三者に提供しません。販売、広告のための共有もしません。</p>"),
 ("6. 安全管理のために行っていること", "<ul><li>お問い合わせのメールは、私たちだけが使うアカウントで管理しています。</li><li>本アプリの中の情報は Mac の中だけにあり、macOS のアプリの保護（App Sandbox）のもとで保存されます。</li></ul>"),
 ("7. 開示・訂正・削除などのご請求", f"<p>私たちが持っているお客様の個人情報（第4項のもの）について、開示・訂正・利用の停止・削除などをご希望の場合は、{MAIL} までメールでご連絡ください。ご本人であることを確かめたうえで、遅滞なく対応します。</p>"),
 ("8. お子さまについて", "<p>本アプリは、年齢を問わず、お子さまを含む誰からも個人情報を集めません。</p>"),
 ("9. このポリシーの変更", "<p>内容を変えるときは、このページで変更日とともにお知らせします。情報の扱いを大きく変える場合（たとえば、Mac の外へ情報を送るようにする場合）は、本アプリの更新の前にこのページを改め、本アプリの中でもお知らせします。</p>"),
 ("10. 事業者・お問い合わせ先", f"<ul><li>事業者: {SELLER_JA}</li><li>住所: ご請求があれば、遅滞なくお知らせします</li><li>メール: {MAIL}</li></ul>"),
]
en_priv = [
 ("1. Summary", "<ul><li>The App reads, analyzes, and exports your videos <b>entirely on your Mac</b>.</li><li>The App <b>does not connect to the internet by itself</b>. We do not send your videos or any analysis results to our servers or to anyone else. (Only when you make a purchase, restore purchases, or redeem a code does macOS's App Store system communicate with Apple; see section 3.)</li><li>The App contains no advertising, no analytics, and no tracking.</li><li>There is no account to create. We do not receive any personal information from you through the App.</li></ul>"),
 ("2. Information kept on your Mac", "<p>The App stores the following on your Mac only. None of it leaves your Mac.</p>" + tbl(["Information","Where","When it is removed / how to remove it"],[
   ["A working copy of the video you choose","A temporary folder inside the App's own container (a folder macOS assigns to the App)","Deleted automatically when processing ends, or the next time the App starts. Your original video is not changed"],
   ["Exported videos and results (highlights, scene lists). Each result folder also records the location of the original video (folder names that may include your Mac user name) and the team names you entered. Please keep this in mind before giving a result folder to someone else","The \"CourtPan\" folder inside your Movies folder","Delete them in Finder or from \"Exported videos\" in the App's settings"],
   ["Saved detection results (positions of players and the ball, used to re-export the same video faster)","The App's container","Delete them from \"Saved detection results\" in the App's settings"],
   ["Venue settings (court outline, etc.)","The App's container","Delete them in the App"],
   ["Free-trial record (an irreversible number that identifies each processed video, and the count; file names are not kept)","Your Mac's keychain","Kept even if you delete the App, so the free trial is counted correctly. You can delete the item \"com.nosunosukawa.courtpan.license\" in Keychain Access"],
   ["Settings (including the last team names you entered)","The App's container","Removed following macOS's normal procedure when you delete the App"]]) +
   "<p>Your videos may show people such as players, referees, and spectators. The App never sends them off your Mac. When you record games or share exported videos, please respect the people who appear in them and follow the recording rules of the event and venue.</p><p>If you allow notifications, the App may notify you when processing is finished. Notifications are created on your Mac.</p>"),
 ("3. Purchases, restoring purchases, and offer codes", "<p>Purchases, restoring purchases, and redeeming offer codes are handled by Apple through the App Store. We do not receive your name, your Apple Account, or your payment information. See <a href=\"https://www.apple.com/legal/privacy/\">Apple's Privacy Policy</a> for how Apple handles this information.</p><p>Through App Store Connect, we receive aggregated sales and usage figures from Apple that do not identify you. If you have chosen to share crash reports or analytics with app developers in your Apple settings, we may receive those reports through Apple and use them only to fix problems in the App.</p>"),
 ("4. Contacting us and receiving invitation codes (outside the App)", "<ul><li>If you email us, we receive your email address and your message and use them only to reply and to investigate problems.</li><li>If we give you an invitation code directly, we keep your name, contact details, and a record of the code we gave you, only to manage the codes (to avoid duplicates and check expiry).</li><li>We delete this information once its purpose is fulfilled, and no later than 2 years.</li><li>We use Gmail by Google LLC (United States) to receive and store email. The United States does not have a comprehensive federal privacy law equivalent to Japan's Act on the Protection of Personal Information; privacy is governed by sector-specific and state laws.</li></ul>"),
 ("5. Sharing with third parties", "<p>We do not share your personal information with third parties except where required by law. We never sell it or share it for advertising.</p>"),
 ("6. Security measures", "<ul><li>Email is kept in an account used only by us.</li><li>Information inside the App stays on your Mac and is stored under macOS app protection (App Sandbox).</li></ul>"),
 ("7. Your requests", f"<p>To request access to, correction of, suspension of use of, or deletion of the personal information we hold about you (section 4), email us at {MAIL}. We will respond without undue delay after confirming your identity.</p>"),
 ("8. Children", "<p>The App does not collect personal information from anyone, including children.</p>"),
 ("9. Changes to this policy", "<p>We will post any changes on this page with the date of the change. If we make a significant change (for example, if the App starts sending information off your Mac), we will update this page before releasing that App update and will also notify you in the App.</p>"),
 ("10. Contact", f"<ul><li>Operator: {SELLER_EN}</li><li>Address: provided without delay upon request</li><li>Email: {MAIL}</li></ul>"),
]
ja_sup = [
 ("CourtPan について", "<p>スタンドに置いた iPhone などで引きで撮ったバスケットボールの試合動画を、Mac の中だけで解析して、選手とボールを追うズーム映像とハイライトを作るアプリです。</p><ul><li>動く環境: Apple シリコンの Mac（M1 以降）・macOS 15 以降</li><li>動画は Mac の外へ送りません</li></ul>"),
 ("お問い合わせ", f"<p>使い方のご質問・不具合のご報告は {MAIL} までお送りください。不具合のときは、Mac の機種・macOS の版・動画の長さと解像度を書いていただけると調べやすくなります。</p>"),
 ("よくあるご質問", "<ul><li><b>処理にどれくらいかかりますか？</b> Mac の機種と動画の長さで変わります。処理の画面に残り時間の目安が出ます。</li><li><b>書き出した動画はどこにありますか？</b>「ムービー」フォルダの中の「CourtPan」フォルダです。</li><li><b>購入を別の Mac で使えますか？</b> 同じ Apple アカウントの Mac なら、アプリの「購入を復元」で使えます。</li></ul>"),
 ("プライバシー", '<p><a href="privacy.ja.html">プライバシーポリシー</a></p>'),
]
en_sup = [
 ("About CourtPan", "<p>CourtPan analyzes wide-angle basketball game videos (for example, from an iPhone on a stand) entirely on your Mac, and creates a zoomed video that follows the players and the ball, plus highlights.</p><ul><li>Requires a Mac with Apple silicon (M1 or later) and macOS 15 or later</li><li>Your videos never leave your Mac</li></ul>"),
 ("Contact", f"<p>For questions or bug reports, email {MAIL}. For bugs, please include your Mac model, macOS version, and the length and resolution of the video.</p>"),
 ("FAQ", "<ul><li><b>How long does processing take?</b> It depends on your Mac and the length of the video. The processing screen shows an estimate of the time remaining.</li><li><b>Where are my exported videos?</b> In the \"CourtPan\" folder inside your Movies folder.</li><li><b>Can I use my purchase on another Mac?</b> Yes, on any Mac signed in with the same Apple Account, using \"Restore Purchases\" in the App.</li></ul>"),
 ("Privacy", '<p><a href="privacy.html">Privacy Policy</a></p>'),
]
foot = "© 2026 Nobutaka Kawasaki"
w = lambda n, s: open(n, "w").write(s)
w("privacy.ja.html", page("ja", "CourtPan プライバシーポリシー", "CourtPan は動画を Mac の中だけで処理し、外へ送りません。", "CourtPan は、動画を Mac の中だけで処理します。Nobutaka Kawasaki（のす工房、以下「私たち」）は、Mac 用アプリ「CourtPan」（以下「本アプリ」）での情報の扱いを、次のとおり定めます。", "制定日: 2026年9月30日", ja_priv, ("privacy.html", "English"), foot + ' · <a href="index.ja.html">サポート</a>'))
w("privacy.html", page("en", "CourtPan Privacy Policy", "CourtPan processes your videos only on your Mac and never sends them anywhere.", "CourtPan processes your videos only on your Mac. This policy explains how Nobutaka Kawasaki (Nosu Works, \"we\") handles information in the Mac app \"CourtPan\" (the \"App\").", "Effective date: September 30, 2026", en_priv, ("privacy.ja.html", "日本語"), foot + ' · <a href="index.html">Support</a>'))
w("index.ja.html", page("ja", "CourtPan サポート", "CourtPan のお問い合わせ先とよくあるご質問。", "バスケの試合動画を、Mac の中で自動でズーム映像とハイライトに。", "", ja_sup, ("index.html", "English"), foot + ' · <a href="privacy.ja.html">プライバシーポリシー</a>'))
w("index.html", page("en", "CourtPan Support", "Contact and FAQ for CourtPan.", "Automatic zoomed video and highlights from your basketball games, made on your Mac.", "", en_sup, ("index.ja.html", "日本語"), foot + ' · <a href="privacy.html">Privacy Policy</a>'))
