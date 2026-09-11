from pathlib import Path

p = Path("index.html")
lines = p.read_text().splitlines(True)
markers = (
    "cdn.utmify.com.br/scripts/utms/latest.js",
    'window.pixelId = "6a3af228cd6a58108c27902c"',
    'window.googlePixelId = "6a49c263bf29386f748b7a2d"',
)

out = []
i = 0
while i < len(lines):
    if any(marker in lines[i] for marker in markers):
        while out and "<script" not in out[-1]:
            out.pop()
        if out and "<script" in out[-1]:
            out.pop()
        while i < len(lines) and "</script>" not in lines[i]:
            i += 1
        i += 1
        if i < len(lines) and lines[i].strip() == "":
            i += 1
        continue
    out.append(lines[i])
    i += 1

p.write_text("".join(out))
