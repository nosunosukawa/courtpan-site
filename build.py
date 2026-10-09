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
 ("1. 要点", "<ul><li>本アプリは、<b>動画の読み込み・解析・書き出しを、すべてお使いの Mac の中で行います。</b></li><li>本アプリは<b>自分ではインターネットに接続しません。</b>動画や解析の結果を、私たちや第三者のサーバーへ送ることはありません（購入・購入の復元・招待コードの入力のときだけ、macOS の App Store の仕組みが Apple と通信します。第3項）。</li><li>広告、アクセス解析、行動の追跡（トラッキング）の仕組みは入っていません。追跡をしないので、ブラウザなどの「Do Not Track（追跡しないでほしい）」の信号の有無によって扱いが変わることはありません。</li><li>アカウントの登録はありません。私たちが本アプリを通じてお客様の個人情報を受け取ることはありません。</li></ul>"),
 ("2. お使いの Mac の中で扱う情報", "<p>本アプリは次の情報を Mac の中に保存します。どれも本アプリが Mac の外へ送ることはありません。</p>" + tbl(["情報","保存する場所","消えるとき・消し方"],[
   ["お客様が選んだ動画の作業用の写し","本アプリ専用の保管場所（macOS が本アプリに割り当てるフォルダ）の一時フォルダ","処理が終わったとき、または次に本アプリを起動したときに自動で消します。元の動画は変更しません"],
   ["「この設定で30秒試す」で作る短い動画と、「検出を試す」で作る1コマの画像（どちらも動画に映った人が映ります）","本アプリ専用の保管場所の一時フォルダ","次に同じ操作をしたときに置き換えます。本アプリを終了しても残ることがあり、macOS が一時フォルダを片付けるときに消えます"],
   ["書き出した本編の動画","「ムービー」フォルダの中の「CourtPan」フォルダ","Finder、または本アプリの設定の「書き出した動画」から消せます"],
   ["書き出した結果を開き直すための情報（元の動画の場所〈Mac のユーザー名を含むフォルダの名前〉、コートの範囲、コマごとの人の位置〈四角の座標だけ〉、得点のしるし、入力したチーム名など）","書き出したフォルダの中の隠しフォルダ「.data」（Finder では通常は見えません）","書き出したフォルダごと消すと消えます。<b>書き出したフォルダをそのまま人に渡すと、この情報も一緒に渡ります</b>"],
   ["得点シーンのしるし（チャプター）。チャプターの名前には、入力したチーム名が入ります（例「〇〇の得点」）","書き出した本編の動画ファイルの中","動画と一緒に消えます。<b>動画を人に渡したり投稿したりすると、チーム名も一緒に渡ります</b>"],
   ["検出結果の控え（選手とボールの位置、スコアボードの部分の画像など。同じ動画を作り直すときに使います）","本アプリ専用の保管場所","本アプリの設定の「保存した検出結果」から消せます"],
   ["会場の設定（コートの範囲など）","本アプリ専用の保管場所","本アプリの画面から消せます"],
   ["無料体験の記録（処理した動画を見分けるための、元に戻せない数字と回数。ファイル名は残しません）","Mac のキーチェーン","無料体験の回数を正しく数えるため、本アプリを削除しても残ります。キーチェーンアクセスで「com.nosunosukawa.courtpan.license」の項目を消すと消えます"],
   ["設定（最後に入力したチーム名を含む）","本アプリ専用の保管場所","本アプリを削除したときに、macOS の手順に従って消えます"]]) +
   "<p>動画には、選手・審判・観客などの人が映っていることがあります。本アプリはそれらを Mac の外へ送りません。撮影と、書き出した動画の公開・共有については、映っている方（お子さまの場合は保護者の方）への配慮と、大会・会場の撮影の決まりの確認をお願いします。</p><p>本アプリは、処理が終わったことをお知らせする通知を出すことがあります（お客様が許可した場合）。通知は Mac の中だけで作られます。</p>"),
 ("3. 購入・購入の復元・招待コード（オファーコード）", "<p>本アプリの購入、購入の復元、オファーコードの入力は、Apple の App Store の仕組みで行われ、Apple が処理します。私たちは、お客様の氏名、Apple アカウント、支払いの情報を受け取りません。Apple が扱う情報については、<a href=\"https://www.apple.com/legal/privacy/\">Apple のプライバシーポリシー</a>をご覧ください。</p><p>私たちは App Store Connect を通じて、Apple から売上や利用状況の集計（個人を特定しない形のもの）を受け取ります。お客様が Apple にクラッシュ（異常終了）の報告や解析データの共有を許可している場合は、Apple を通じてその報告を受け取ることがあり、本アプリの不具合を直すためだけに使います。</p>"),
 ("4. お問い合わせ・招待コードの受け渡し・このページで扱う情報（本アプリの外）", "<ul><li>お客様がメールでお問い合わせくださった場合、私たちはメールアドレスとお問い合わせの内容を受け取り、<b>お返事と、不具合の調査のためだけに</b>使います。</li><li>私たちが招待コードを直接お渡しした場合は、お渡しした方のお名前・連絡先と、お渡ししたコードの控えを、<b>コードの管理（重複や期限の確認）のためだけに</b>持ちます。</li><li>これらは、目的を果たしたあと、遅くとも2年で消します。</li><li>私たちはメールの受け取りと保管に Google LLC（米国）の Gmail を使っています。米国には、日本の個人情報保護法と同じ水準の包括的な個人情報保護の法律はなく、州ごとの法律などがあります。</li><li>このページと CourtPan のサポートページは、GitHub, Inc.（米国）の GitHub Pages で公開しています。GitHub は安全のため、閲覧した方の IP アドレスを記録・保存します（GitHub の説明による）。私たちはこれらのページに解析・広告の仕組みを入れておらず、その記録を利用しません。</li></ul>"),
 ("5. 第三者への提供", "<p>私たちは、法令に基づく場合を除き、お客様の個人情報を第三者に提供しません。販売、広告のための共有もしません。</p>"),
 ("6. 安全管理のために行っていること", "<ul><li>お問い合わせのメールは、私たちだけが使うアカウントで管理しています。</li><li>本アプリの中の情報は Mac の中だけにあり、macOS のアプリの保護（App Sandbox）のもとで保存されます。</li></ul>"),
 ("7. 開示・訂正・削除などのご請求", f"<p>私たちが持っているお客様の個人情報（第4項のもの）について、開示・訂正・利用の停止・削除などをご希望の場合は、{MAIL} までメールでご連絡ください。ご本人であることを確かめたうえで、遅滞なく対応します。</p>"),
 ("8. お子さまについて", "<p>本アプリは、年齢を問わず、お子さまを含む誰からも個人情報を集めません。13歳未満のお子さまからのメールであると分かった場合は、お返事に必要な範囲を超えて保存せず、速やかに消します。</p>"),
 ("9. このポリシーの変更", "<p>内容を変えるときは、このページで改定日とともにお知らせします。情報の扱いを大きく変える場合（たとえば、Mac の外へ情報を送るようにする場合）は、本アプリの更新の前にこのページを改め、本アプリの中でもお知らせします。</p>"),
 ("10. 事業者・お問い合わせ先", f"<ul><li>事業者・個人情報の責任者: {SELLER_JA}</li><li>住所: ご請求があれば、遅滞なくお知らせします</li><li>メール: {MAIL}</li></ul>"),
 ("11. 英国・米国・カナダ・オーストラリア・ニュージーランドの方へ", "<ul><li>第4項の情報について、私たちは上の事業者として責任を負います。取り扱いの根拠は、お問い合わせへのお返事（お客様のご依頼に応じるため）と、招待コードの管理（私たちの正当な利益）です。</li><li>お客様は、ご自身の個人情報について、開示・訂正・削除・利用の制限・利用への異議・データの受け取り（持ち運び）を求めることができます（第7項の連絡先へ）。</li><li>私たちは日本にいます。お客様のメールは日本の私たちと、米国の Google LLC（Gmail）で扱われます。</li><li>私たちの対応にご不満がある場合は、お住まいの国の監督機関（英国の Information Commissioner's Office、カナダのプライバシー・コミッショナー、オーストラリアの OAIC、ニュージーランドのプライバシー・コミッショナーなど）に申し立てることができます。</li></ul>"),
]
en_priv = [
 ("1. Summary", "<ul><li>The App reads, analyzes, and exports your videos <b>entirely on your Mac</b>.</li><li>The App <b>does not connect to the internet by itself</b>. We do not send your videos or any analysis results to our servers or to anyone else. (Only when you make a purchase, restore purchases, or redeem a code does macOS's App Store system communicate with Apple; see section 3.)</li><li>The App contains no advertising, no analytics, and no tracking. Because we do not track you, we treat everyone the same whether or not a browser sends a \"Do Not Track\" signal.</li><li>There is no account to create. We do not receive any personal information from you through the App.</li></ul>"),
 ("2. Information kept on your Mac", "<p>The App stores the following on your Mac only. The App never sends any of it off your Mac.</p>" + tbl(["Information","Where","When it is removed / how to remove it"],[
   ["A working copy of the video you choose","A temporary folder inside the App's own container (a folder macOS assigns to the App)","Deleted automatically when processing ends, or the next time the App starts. Your original video is not changed"],
   ["The short video made by \"Try 30 Seconds with These Settings\" and the single-frame image made by \"Test Detection\" (both show the people in your video)","A temporary folder inside the App's container","Replaced the next time you use the same feature. It may remain after you quit the App and is removed when macOS cleans up temporary folders"],
   ["Exported full-game videos","The \"CourtPan\" folder inside your Movies folder","Delete them in Finder or from \"Exported videos\" in the App's settings"],
   ["Information used to reopen an export (the location of the original video, i.e. folder names that may include your Mac user name; the court outline; per-frame positions of people, as box coordinates only; scoring tags; the team names you entered; etc.)","A hidden \".data\" folder inside each export folder (normally not visible in Finder)","Removed when you delete the export folder. <b>If you give someone the whole export folder, this information goes with it</b>"],
   ["Scoring tags (chapters). Chapter names include the team names you entered (for example, \"&lt;Team&gt; scores\")","Inside the exported video file","Removed with the video. <b>If you share or post the video, the team names go with it</b>"],
   ["Saved detection results (positions of players and the ball, images of the scoreboard area, etc., used to re-export the same video faster)","The App's container","Delete them from \"Saved detection results\" in the App's settings"],
   ["Venue settings (court outline, etc.)","The App's container","Delete them in the App"],
   ["Free-trial record (an irreversible number that identifies each processed video, and the count; file names are not kept)","Your Mac's keychain","Kept even if you delete the App, so the free trial is counted correctly. You can delete the item \"com.nosunosukawa.courtpan.license\" in Keychain Access"],
   ["Settings (including the last team names you entered)","The App's container","Removed following macOS's normal procedure when you delete the App"]]) +
   "<p>Your videos may show people such as players, referees, and spectators. The App never sends them off your Mac. When you record games or share exported videos, please respect the people who appear in them (and their parents or guardians, for children) and follow the recording rules of the event and venue.</p><p>If you allow notifications, the App may notify you when processing is finished. Notifications are created on your Mac.</p>"),
 ("3. Purchases, restoring purchases, and offer codes", "<p>Purchases, restoring purchases, and redeeming offer codes are handled by Apple through the App Store. We do not receive your name, your Apple Account, or your payment information. See <a href=\"https://www.apple.com/legal/privacy/\">Apple's Privacy Policy</a> for how Apple handles this information.</p><p>Through App Store Connect, we receive aggregated sales and usage figures from Apple that do not identify you. If you have chosen to share crash reports or analytics with app developers in your Apple settings, we may receive those reports through Apple and use them only to fix problems in the App.</p>"),
 ("4. Contacting us, invitation codes, and this website (outside the App)", "<ul><li>If you email us, we receive your email address and your message and use them only to reply and to investigate problems.</li><li>If we give you an invitation code directly, we keep your name, contact details, and a record of the code we gave you, only to manage the codes (to avoid duplicates and check expiry).</li><li>We delete this information once its purpose is fulfilled, and no later than 2 years.</li><li>We use Gmail by Google LLC (United States) to receive and store email. The United States does not have a comprehensive federal privacy law equivalent to Japan's Act on the Protection of Personal Information; privacy is governed by sector-specific and state laws.</li><li>This page and the CourtPan support page are hosted on GitHub Pages by GitHub, Inc. (United States). According to GitHub, the IP address of each visitor is logged and stored for security purposes. We have not added any analytics or advertising to these pages, and we do not use those logs.</li></ul>"),
 ("5. Sharing with third parties", "<p>We do not share your personal information with third parties except where required by law. We never sell it or share it for advertising.</p>"),
 ("6. Security measures", "<ul><li>Email is kept in an account used only by us.</li><li>Information inside the App stays on your Mac and is stored under macOS app protection (App Sandbox).</li></ul>"),
 ("7. Your requests", f"<p>To request access to, correction of, suspension of use of, or deletion of the personal information we hold about you (section 4), email us at {MAIL}. We will respond without undue delay after confirming your identity.</p>"),
 ("8. Children", "<p>The App does not collect personal information from anyone, including children. If we learn that an email came from a child under 13, we will not keep it longer than needed to reply and will delete it promptly.</p>"),
 ("9. Changes to this policy", "<p>We will post any changes on this page with the \"Last updated\" date. If we make a significant change (for example, if the App starts sending information off your Mac), we will update this page before releasing that App update and will also notify you in the App.</p>"),
 ("10. Contact", f"<ul><li>Operator and person responsible for personal information: {SELLER_EN}</li><li>Address: provided without delay upon request</li><li>Email: {MAIL}</li></ul>"),
 ("11. If you are in the United Kingdom, the United States, Canada, Australia, or New Zealand", "<ul><li>We are responsible for the information described in section 4. We process it to reply to you at your request and, for invitation codes, on the basis of our legitimate interest in managing the codes.</li><li>You may ask us to give you access to, correct, delete, or restrict the use of your personal information, to stop using it, or to give it to you in a portable form (contact us as in section 7).</li><li>We are based in Japan. Your email is handled by us in Japan and by Google LLC (Gmail) in the United States.</li><li>If you are not satisfied with our response, you can complain to the privacy regulator where you live, such as the UK Information Commissioner's Office, the Office of the Privacy Commissioner of Canada, the Office of the Australian Information Commissioner, or the New Zealand Privacy Commissioner.</li></ul>"),
]
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
ja_sup = [
 ("CourtPan について", "<p>三脚に固定した iPhone などで引きで撮ったバスケットボールの試合動画を、Mac の中だけで解析して、選手を追いかけて寄る自動ズームの本編を作るアプリです。スコアボードの得点が変わったところにしるし（チャプター）を付けられます。</p><ul><li>動く環境: Apple シリコンの Mac（M1 以降）・macOS 15 以降</li><li>動画は Mac の外へ送りません</li></ul>"),
 ("お問い合わせ", f"<p>使い方のご質問・不具合のご報告は {MAIL} までお送りください。不具合のときは、Mac の機種・macOS の版・動画の長さと解像度を書いていただけると調べやすくなります。</p>"),
 ("よくあるご質問", "<ul><li><b>処理にどれくらいかかりますか？</b> Mac の機種と動画の長さで変わります。処理の画面に残り時間の目安が出ます。</li><li><b>書き出した動画はどこにありますか？</b>「ムービー」フォルダの中の「CourtPan」フォルダです。</li><li><b>購入を別の Mac で使えますか？</b> 同じ Apple アカウントの Mac なら、アプリの「購入を復元」で使えます。</li><li><b>返金したいときは？</b> App Store での購入の返金は Apple が扱います。<a href=\"https://reportaproblem.apple.com/\">reportaproblem.apple.com</a> からお申し込みください。お住まいの国の法律で認められた権利は、この案内によって制限されません。</li></ul>"),
 ("プライバシー・利用規約", f'<p><a href="privacy.ja.html">プライバシーポリシー</a></p><p>CourtPan の利用規約は、Apple の標準の使用許諾契約（<a href="{EULA}">{EULA}</a>）です。</p>'),
]
en_sup = [
 ("About CourtPan", "<p>CourtPan analyzes wide, tripod-shot basketball game videos (for example, from an iPhone) entirely on your Mac, and makes an auto-zoomed full-game video that follows the players. It can also tag the moments when the scoreboard score changes (chapters).</p><ul><li>Requires a Mac with Apple silicon (M1 or later) and macOS 15 or later</li><li>Your videos never leave your Mac</li></ul>"),
 ("Contact", f"<p>For questions or bug reports, email {MAIL}. For bugs, please include your Mac model, macOS version, and the length and resolution of the video.</p>"),
 ("FAQ", "<ul><li><b>How long does processing take?</b> It depends on your Mac and the length of the video. The processing screen shows an estimate of the time remaining.</li><li><b>Where are my exported videos?</b> In the \"CourtPan\" folder inside your Movies folder.</li><li><b>Can I use my purchase on another Mac?</b> Yes, on any Mac signed in with the same Apple Account, using \"Restore Purchase\" in the App.</li><li><b>How do I request a refund?</b> Refunds for App Store purchases are handled by Apple at <a href=\"https://reportaproblem.apple.com/\">reportaproblem.apple.com</a>. This does not limit any rights you have under the consumer laws of your country.</li></ul>"),
 ("Privacy and terms", f'<p><a href="privacy.html">Privacy Policy</a></p><p>CourtPan is licensed under Apple\'s standard End User License Agreement (<a href="{EULA}">{EULA}</a>).</p>'),
]
foot = "© 2026 Nobutaka Kawasaki"
w = lambda n, s: open(n, "w").write(s)
w("privacy.ja.html", page("ja", "CourtPan プライバシーポリシー", "CourtPan は動画を Mac の中だけで処理し、外へ送りません。", "CourtPan は、動画を Mac の中だけで処理します。Nobutaka Kawasaki（のす工房、以下「私たち」）は、Mac 用アプリ「CourtPan」（以下「本アプリ」）での情報の扱いを、次のとおり定めます。", "制定日: 2026年9月30日<br>改定日: 2026年10月9日", ja_priv, ("privacy.html", "English"), foot + ' · <a href="index.ja.html">サポート</a>'))
w("privacy.html", page("en", "CourtPan Privacy Policy", "CourtPan processes your videos only on your Mac and never sends them anywhere.", "CourtPan processes your videos only on your Mac. This policy explains how Nobutaka Kawasaki (Nosu Works, \"we\") handles information in the Mac app \"CourtPan\" (the \"App\").", "Effective date: September 30, 2026<br>Last updated: October 9, 2026", en_priv, ("privacy.ja.html", "日本語"), foot + ' · <a href="index.html">Support</a>'))
w("index.ja.html", page("ja", "CourtPan サポート", "CourtPan のお問い合わせ先とよくあるご質問。", "バスケの試合動画を、Mac の中で自動ズームの本編に。", "", ja_sup, ("index.html", "English"), foot + ' · <a href="privacy.ja.html">プライバシーポリシー</a>'))
w("index.html", page("en", "CourtPan Support", "Contact and FAQ for CourtPan.", "Auto-zoomed full-game video from your basketball games, made on your Mac.", "", en_sup, ("index.ja.html", "日本語"), foot + ' · <a href="privacy.html">Privacy Policy</a>'))
