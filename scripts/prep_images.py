"""One-off image prep script for the PockRomWeb marketing site.
Run once from the repo root: python scripts/prep_images.py
Reads source screenshots/icons from the repo root and the sibling app repo,
writes optimized web assets into assets/img/.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_ROOT = r"C:\Users\USER\Desktop\things\Project"
IMG_OUT = os.path.join(ROOT, "assets", "img")
SHOT_OUT = os.path.join(IMG_OUT, "screenshots")

os.makedirs(SHOT_OUT, exist_ok=True)

SCREENSHOTS = {
    "CharacterChat.jpg": "character-chat",
    "CharacterCustomization.jpg": "character-customization",
    "CharacterGadgetInteraction.jpg": "gadget-interaction",
    "ModelSelection.jpg": "model-selection",
    "SessionSummary.jpg": "session-summary",
}

for src_name, out_stem in SCREENSHOTS.items():
    src = os.path.join(ROOT, src_name)
    im = Image.open(src).convert("RGB")
    jpg_path = os.path.join(SHOT_OUT, out_stem + ".jpg")
    im.save(jpg_path, "JPEG", quality=85, optimize=True)
    webp_path = os.path.join(SHOT_OUT, out_stem + ".webp")
    im.save(webp_path, "WEBP", quality=82, method=6)
    print("screenshot:", out_stem, im.size, os.path.getsize(jpg_path), os.path.getsize(webp_path))

# Hero / feature graphic (1024x500 source)
fg_src = os.path.join(APP_ROOT, "feature_graphic.png")
fg = Image.open(fg_src).convert("RGB")
fg.save(os.path.join(IMG_OUT, "hero.png"), "PNG", optimize=True)
fg.save(os.path.join(IMG_OUT, "hero.webp"), "WEBP", quality=88, method=6)
print("hero:", fg.size)

# OG / social share image: center-crop to 1200x630 target ratio then upscale
target_ratio = 1200 / 630
w, h = fg.size
src_ratio = w / h
if src_ratio > target_ratio:
    new_w = int(h * target_ratio)
    x0 = (w - new_w) // 2
    box = (x0, 0, x0 + new_w, h)
else:
    new_h = int(w / target_ratio)
    y0 = (h - new_h) // 2
    box = (0, y0, w, y0 + new_h)
og = fg.crop(box).resize((1200, 630), Image.LANCZOS)
og.save(os.path.join(IMG_OUT, "og-image.png"), "PNG", optimize=True)
print("og-image:", og.size, os.path.getsize(os.path.join(IMG_OUT, "og-image.png")))

# App icon -> apple-touch-icon (180) + a larger 512 fallback
icon_src = os.path.join(APP_ROOT, "assets", "icon.png")
icon = Image.open(icon_src).convert("RGB")
icon.resize((512, 512), Image.LANCZOS).save(os.path.join(IMG_OUT, "icon-512.png"), "PNG", optimize=True)
icon.resize((180, 180), Image.LANCZOS).save(os.path.join(IMG_OUT, "icon-180.png"), "PNG", optimize=True)
print("icons done")

# Favicon: reuse the app's own pre-made 48x48 favicon (has transparency)
fav_src = os.path.join(APP_ROOT, "assets", "favicon.png")
fav = Image.open(fav_src).convert("RGBA")
fav.save(os.path.join(IMG_OUT, "favicon-48.png"), "PNG", optimize=True)
fav.resize((32, 32), Image.LANCZOS).save(os.path.join(IMG_OUT, "favicon-32.png"), "PNG", optimize=True)
print("favicon done")

print("ALL DONE")
