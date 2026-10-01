import os
from pathlib import Path
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QImage, QPainter, QColor, QPen, QGuiApplication
from qgis.PyQt.QtSvg import QSvgRenderer

app = QGuiApplication([])

svg_path = r"d:\GitHub\bajiki\logo-fix\magelloku-app-icon.svg"
icons_dir = r"d:\GitHub\maggeloku-mcp\qgis_mcp_plugin\icons"

renderer = QSvgRenderer(svg_path)
if not renderer.isValid():
    raise SystemExit("SVG is not valid")

sizes = {
    "icon.png": (256, 256),
    "icon_128.png": (128, 128),
    "icon_64.png": (64, 64),
    "icon_32.png": (32, 32),
    "icon_16.png": (16, 16),
    "mcp_logo.png": (256, 256),
}

for name, (w, h) in sizes.items():
    img = QImage(w, h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)
    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.SmoothPixmapTransform)
    renderer.render(painter)
    painter.end()
    out_path = os.path.join(icons_dir, name)
    ok = img.save(out_path, "PNG")
    print("Saved:", name, ok)

# For icon_active.png (64x64 with a bright green active badge)
img = QImage(64, 64, QImage.Format_ARGB32)
img.fill(Qt.transparent)
painter = QPainter(img)
painter.setRenderHint(QPainter.Antialiasing)
painter.setRenderHint(QPainter.SmoothPixmapTransform)
renderer.render(painter)

# draw vibrant green active dot at bottom-right
painter.setBrush(QColor("#00E676"))
painter.setPen(QPen(QColor("#173F34"), 2))
painter.drawEllipse(40, 40, 20, 20)
painter.end()

out_path = os.path.join(icons_dir, "icon_active.png")
ok = img.save(out_path, "PNG")
print("Saved: icon_active.png", ok)
