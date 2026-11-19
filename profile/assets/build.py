"""Build the nika-open organization profile media from the nika.sh brand kit.

Usage: python3 -I build.py <org-profile dir>
Writes out/banner-dark.png, out/banner-light.png (2400x840, rendered by headless Chrome with
the site's own Martian fonts) and out/avatar.png (1024x1024, rendered by rsvg-convert).
Tokens are quoted from nika.sh src/ui/roles.css (dark) and src/home/styles/01-foundations.css
(light); the mark path and the lockup geometry come from public/brand/.
"""
import base64
import pathlib
import re
import subprocess
import sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

THEMES = {
    "dark": {
        "bg": "oklch(9.4% 0.006 262)",
        "fg": "oklch(97% 0.003 255)",
        "fg2": "oklch(87.5% 0.006 258)",
        "fg3": "oklch(71.5% 0.008 260)",
        "fg4": "oklch(55.5% 0.008 260)",
        "stroke1": "oklch(100% 0 0 / 0.07)",
        "stroke2": "oklch(100% 0 0 / 0.115)",
        "accent": "oklch(54% 0.27 266)",
        "accent_mid": "oklch(66% 0.2 266)",
        "accent_fg": "oklch(80% 0.12 262)",
        "accent_wash": "oklch(54% 0.27 266 / 0.2)",
        "mark": "#9fd0ff",
        "word": "#f4f5f7",
    },
    "light": {
        "bg": "oklch(97.6% 0.004 258)",
        "fg": "oklch(19% 0.03 262)",
        "fg2": "oklch(30% 0.03 262)",
        "fg3": "oklch(43% 0.026 262)",
        "fg4": "oklch(55% 0.02 262)",
        "stroke1": "oklch(24% 0.05 262 / 0.08)",
        "stroke2": "oklch(24% 0.05 262 / 0.14)",
        "accent": "oklch(50% 0.28 266)",
        "accent_mid": "oklch(56% 0.25 266)",
        "accent_fg": "oklch(44% 0.27 266)",
        "accent_wash": "oklch(52% 0.26 266 / 0.12)",
        "mark": "#04050d",
        "word": "#0a0b0d",
    },
}

STAGES = [
    ("PLAN", "a readable .nika file"),
    ("CHECK", "checked before it runs"),
    ("RUN", "run with your model"),
    ("PROOF", "a trace and a receipt"),
]


def font_face(name: str, path: pathlib.Path, stretch: str) -> str:
    data = base64.b64encode(path.read_bytes()).decode()
    return (
        f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,{data}) format('woff2');"
        f"font-weight:100 900;font-stretch:{stretch};font-display:block}}"
    )


def mark_path(src: pathlib.Path) -> str:
    match = re.search(r'<path d="([^"]+)"', src.read_text(encoding="utf-8"))
    if not match:
        raise SystemExit("mark path not found")
    return match.group(1)


def banner_html(theme: dict, faces: str, mark_d: str) -> str:
    # Device units: the 2400x840 viewBox maps 1:1 onto the 2x screenshot pixels.
    left, right = 168, 2232
    plate, rail_y = 584, 682
    step = (right - left) / 4
    nodes = [left + i * step for i in range(4)]
    seams = "".join(
        f'<line x1="{x:.1f}" y1="{plate}" x2="{x:.1f}" y2="790" class="seam"/>'
        for x in nodes + [right]
    )
    stages = ""
    for i, ((word, caption), x) in enumerate(zip(STAGES, nodes)):
        last = i == len(STAGES) - 1
        anchor = "start"
        node = (
            f'<circle cx="{x:.1f}" cy="{rail_y}" r="24" class="halo"/>'
            f'<circle cx="{x:.1f}" cy="{rail_y}" r="12" class="node-fill"/>'
            if last
            else f'<circle cx="{x:.1f}" cy="{rail_y}" r="10" class="node-ring"/>'
        )
        stages += (
            node
            + f'<text x="{x:.1f}" y="{rail_y - 42}" text-anchor="{anchor}" class="stage">{word}</text>'
            + f'<text x="{x:.1f}" y="{rail_y + 70}" text-anchor="{anchor}" class="caption">{caption}</text>'
        )
    t = theme
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
{faces}
html,body{{margin:0;padding:0;background:{t['bg']};}}
svg{{display:block;width:1200px;height:420px;}}
.seam{{stroke:{t['stroke1']};stroke-width:2;}}
.rule{{stroke:{t['stroke2']};stroke-width:2;}}
.rail{{stroke:{t['accent']};stroke-width:4;}}
.node-ring{{fill:{t['bg']};stroke:{t['accent_mid']};stroke-width:4;}}
.node-fill{{fill:{t['accent']};}}
.halo{{fill:{t['accent_wash']};}}
.mark{{fill:{t['mark']};}}
.word{{font-family:'Martian Mono';font-stretch:100%;font-weight:700;font-size:34px;letter-spacing:0.02em;fill:{t['word']};}}
.dot{{fill:#ff7a3c;}}
.site{{font-family:'Martian Mono';font-stretch:87%;font-weight:450;font-size:32px;letter-spacing:0.04em;fill:{t['fg3']};}}
.eyebrow{{font-family:'Martian Mono';font-stretch:87%;font-weight:500;font-size:30px;letter-spacing:0.14em;fill:{t['accent_fg']};}}
.title{{font-family:'Martian Grotesk';font-stretch:96%;font-weight:350;font-size:112px;letter-spacing:-0.035em;fill:{t['fg']};}}
.lede{{font-family:'Martian Grotesk';font-stretch:100%;font-weight:400;font-size:42px;fill:{t['fg2']};}}
.stage{{font-family:'Martian Mono';font-stretch:87%;font-weight:600;font-size:34px;letter-spacing:0.16em;fill:{t['fg']};}}
.caption{{font-family:'Martian Mono';font-stretch:87%;font-weight:450;font-size:32px;fill:{t['fg3']};}}
</style></head><body>
<svg viewBox="0 0 2400 840" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="840" fill="{t['bg']}"/>
  <g transform="translate(160,86) scale(1.6)">
    <g transform="translate(4,6) scale(0.0473)"><path d="{mark_d}" class="mark"/></g>
    <text x="68" y="44" class="word">nika</text>
    <circle cx="161" cy="40" r="4.5" class="dot"/>
  </g>
  <text x="{right}" y="160" text-anchor="end" class="site">nika.sh</text>
  <text x="{left}" y="318" class="eyebrow">REPEATABLE WORK, SAVED AS A FILE</text>
  <text x="{left - 6}" y="436" class="title">Say it once. Keep it as a file.</text>
  <text x="{left}" y="510" class="lede">An open-source workflow language and engine.</text>
  <line x1="{left}" y1="{plate}" x2="{right}" y2="{plate}" class="rule"/>
  {seams}
  <line x1="{left}" y1="{rail_y}" x2="{nodes[-1]:.1f}" y2="{rail_y}" class="rail"/>
  {stages}
</svg>
</body></html>"""


def avatar_svg(mark_d: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1100" width="1024" height="1024">
  <rect width="1100" height="1100" fill="#04050d"/>
  <g transform="translate(198,198) scale(0.64)"><path d="{mark_d}" fill="#9fd0ff"/></g>
</svg>
"""


def main() -> int:
    root = pathlib.Path(sys.argv[1])
    src, out = root / "src", root / "out"
    out.mkdir(exist_ok=True)
    faces = font_face("Martian Grotesk", src / "fonts/martian-grotesk-variable.woff2", "75% 200%")
    faces += font_face("Martian Mono", src / "fonts/martian-mono-variable.woff2", "75% 112.5%")
    mark_d = mark_path(src / "nika-mark-dark.svg")
    for name, theme in THEMES.items():
        page = src / f"banner-{name}.html"
        page.write_text(banner_html(theme, faces, mark_d), encoding="utf-8")
        png = out / f"banner-{name}.png"
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=2", "--window-size=1200,420",
             "--virtual-time-budget=4000", f"--screenshot={png}", page.as_uri()],
            check=True, capture_output=True, timeout=120,
        )
        print("wrote", png)
    avatar = src / "avatar.svg"
    avatar.write_text(avatar_svg(mark_d), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "1024", "-h", "1024", "-o", str(out / "avatar.png"),
                    str(avatar)], check=True)
    print("wrote", out / "avatar.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
