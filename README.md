# 🎌 Anime Streaming — Landing Page con Reflex

Una plataforma de streaming de anime construida completamente con **Python y Reflex**, sin una sola línea de JavaScript. Recrea la experiencia visual de plataformas como Crunchyroll o Netflix Anime, con navegación entre páginas, portadas reales de cada anime y una interfaz oscura y moderna.

---

## 🖥️ ¿Qué es este proyecto?

Es una aplicación web que simula la pantalla principal de un servicio de streaming de anime. Al abrirla en el navegador verás:

- Una **barra de navegación** fija con logo, menú y avatar de usuario.
- Un **hero principal** con la imagen de *Frieren: Beyond Journey's End*, título, descripción y dos botones.
- Tres secciones de tarjetas scrolleables: **Trending Now**, **Continue Watching for You** y **Recommended For You**.
- Una fila de **píldoras de géneros** (Action, Fantasy, Romance, etc.).

Al hacer clic en el botón **▶ Play** del hero, la app navega a una segunda página interna (`/frieren`) que muestra el detalle del anime: banner, ficha técnica con rating, y una lista de episodios.

---

## 📁 Estructura del proyecto

```
anime-streaming/
├── anime_streaming/
│   ├── __init__.py
│   ├── anime_streaming.py   # Páginas y configuración de la app
│   ├── components.py        # Componentes reutilizables (navbar, cards, etc.)
│   └── data.py              # Datos de los animes (títulos, imágenes, géneros)
├── assets/                  # Imágenes: portadas, banner, logo, avatar
├── rxconfig.py              # Configuración de Reflex
└── pyproject.toml           # Dependencias gestionadas con Poetry
```

---

## ⚙️ Requisitos previos

Antes de correr el proyecto, necesitas tener instalado:

- **Python 3.10 o superior** — [python.org](https://www.python.org/)
- **Poetry 2.x** — gestor de dependencias ([poetry.eustace.io](https://python-poetry.org/))
- **Git** — control de versiones ([git-scm.com](https://git-scm.com/))

---

## 🚀 Cómo correr el proyecto

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/anime-streaming.git
cd anime-streaming

# 2. Instala las dependencias con Poetry
poetry install

# 3. Ejecuta la aplicación
poetry run reflex run

# 4. Abre el navegador en:
#    http://localhost:3000
```

> La primera vez puede tardar 1–2 minutos mientras Reflex prepara el entorno frontend.

---

## 🗂️ Páginas disponibles

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal con hero, géneros y secciones de anime |
| `/frieren` | Página de detalle de *Frieren: Beyond Journey's End* con episodios |

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3.12** | Lenguaje base |
| **Reflex** | Framework web full-stack en Python puro |
| **Poetry** | Gestión de dependencias y entorno virtual |
| **Git** | Control de versiones |

---

## 📸 Capturas

La interfaz recrea la estética oscura de plataformas de streaming profesionales con fondo `#0d0d0d`, acentos en teal (`#46AFC8`) y tipografía Inter.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## 👤 Autor

**Damian Lorenzo**  
Materia: Análisis y Diseño — Colegio APEC Fernando Arturo de Meriño  
Profesor: José Mañon · Mayo 2026
