"""Arma la carpeta entregables/ con los productos finales y la convención Equipo3_Proyecto3_*.

Uso, desde la raíz del repositorio:
    python scripts/armar_entregables.py

Antes de correrlo:
- el notebook y el R Markdown deben estar ejecutados;
- los PDF de la presentación y del anexo de IA deben estar generados
  (Edge o Chrome: Imprimir → Guardar como PDF, sin márgenes, con gráficos de fondo).

La presentación de entregables/ es una copia autocontenida: las imágenes van dentro del HTML
y los botones apuntan a las carpetas Python/ y R/ de entregables/ (en el repositorio apuntan
a python/html/ y r/salidas/).
"""
import base64
import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "entregables"
ENLACE_PBI = ("https://app.powerbi.com/links/N7NaGvljjq?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99"
              "&pbi_source=linkShare")

# origen (relativo a la raíz) -> destino (relativo a entregables/)
COPIAS = {
    "presentacion/Equipo3_Proyecto3_Presentacion.pdf": "Equipo3_Proyecto3_Presentacion.pdf",
    "docs/Equipo3_Proyecto3_Anexo_IA.pdf": "Equipo3_Proyecto3_Anexo_IA.pdf",
    "docs/Definiciones_compartidas.md": "Equipo3_Proyecto3_Fuentes_Definiciones_Limitaciones.md",
    "docs/LEEME_entregables.md": "Equipo3_Proyecto3_LEEME.md",
    "powerbi/Equipo3_Proyecto3_Dashboard.pbix": "PowerBI/Equipo3_Proyecto3_Dashboard.pbix",
    "python/Equipo3_Proyecto3_Analisis.ipynb": "Python/Equipo3_Proyecto3_Analisis.ipynb",
    "python/html/Equipo3_Proyecto3_Plotly_Panorama_Sectores.html": "Python/Equipo3_Proyecto3_Plotly_Panorama_Sectores.html",
    "python/html/Equipo3_Proyecto3_Plotly_Sectores_por_Edad.html": "Python/Equipo3_Proyecto3_Plotly_Sectores_por_Edad.html",
    "r/Equipo3_Proyecto3_Mapa.Rmd": "R/Equipo3_Proyecto3_Mapa.Rmd",
    "r/Equipo3_Proyecto3_Mapa.html": "R/Equipo3_Proyecto3_Mapa.html",
    "r/salidas/Equipo3_Proyecto3_Mapa_Brecha_Departamento.png": "R/Equipo3_Proyecto3_Mapa_Brecha_Departamento.png",
    "r/salidas/Equipo3_Proyecto3_Intervalos_Departamento.png": "R/Equipo3_Proyecto3_Intervalos_Departamento.png",
    "r/salidas/Equipo3_Proyecto3_Mapa_Interactivo.html": "R/Equipo3_Proyecto3_Mapa_Interactivo.html",
}


def presentacion_autocontenida():
    carpeta = RAIZ / "presentacion"
    html = (carpeta / "Equipo3_Proyecto3_Presentacion.html").read_text(encoding="utf-8")

    def incrustar(m):
        ruta = carpeta / m.group(1)
        if not ruta.exists():
            return m.group(0)   # captura pendiente: se deja igual y la presentación muestra el aviso
        datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
        return f'src="data:image/png;base64,{datos}"'

    html = re.sub(r'src="(img/[^"]+\.png)"', incrustar, html)
    html = html.replace('href="../python/html/', 'href="Python/').replace('href="../r/salidas/', 'href="R/')
    (DESTINO / "Equipo3_Proyecto3_Presentacion.html").write_text(html, encoding="utf-8")


def main():
    for viejo in DESTINO.glob("*"):
        if viejo.name == ".gitkeep":
            continue
        shutil.rmtree(viejo) if viejo.is_dir() else viejo.unlink()

    faltan = []
    for origen, destino in COPIAS.items():
        ruta = RAIZ / origen
        if not ruta.exists():
            faltan.append(origen)
            continue
        (DESTINO / destino).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ruta, DESTINO / destino)

    (DESTINO / "PowerBI" / "Equipo3_Proyecto3_Enlace_PowerBI.txt").write_text(
        "Tablero publicado en Power BI Service:\n" + ENLACE_PBI + "\n", encoding="utf-8")
    presentacion_autocontenida()

    print("Archivos en entregables/:")
    for f in sorted(DESTINO.rglob("*")):
        if f.is_file() and f.name != ".gitkeep":
            print(f"  {f.relative_to(DESTINO)}  ({f.stat().st_size / 1e6:.1f} MB)")
    if faltan:
        print("\nFALTAN (revisar antes de enviar):")
        for f in faltan:
            print("  ", f)


if __name__ == "__main__":
    main()
