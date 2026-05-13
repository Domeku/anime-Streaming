# anime_streaming/components.py
# Aquí están todos los bloques visuales de la página

import reflex as rx
from anime_streaming.data import GENRES

# Tamaño de cada tarjeta de anime
CARD_W = "158px"
CARD_H = "218px"


def navbar() -> rx.Component:
    """Barra de navegación fija en la parte superior."""
    return rx.box(
        rx.hstack(
            # Logo: círculo blanco
            rx.box(
                width="28px",
                height="28px",
                border_radius="50%",
                border="2.5px solid white",
                flex_shrink="0",
            ),
            # Links de navegación
            rx.hstack(
                rx.text(
                    "Home",
                    color="white",
                    font_weight="700",
                    font_size="14px",
                    cursor="pointer",
                ),
                rx.text("My List", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("Movie", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("New Season", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("Language", color="#888888", font_size="14px", cursor="pointer"),
                gap="24px",
                align="center",
            ),
            rx.spacer(),
            # Barra de búsqueda
            rx.hstack(
                rx.box(
                    rx.text("Search here ...", color="#555555", font_size="13px"),
                    background="rgba(255,255,255,0.07)",
                    border_radius="20px",
                    padding_x="14px",
                    padding_y="7px",
                    min_width="175px",
                    cursor="text",
                ),
                rx.text("🔍", color="#777777", font_size="16px"),
                gap="8px",
                align="center",
            ),
            # Campana y avatar de usuario
            rx.hstack(
                rx.text("🔔", color="#777777", font_size="19px", cursor="pointer"),
                rx.box(
                    rx.image(
                        src="https://placehold.co/32x32/2a8888/ffffff?text=U",
                        width="32px",
                        height="32px",
                        border_radius="50%",
                    ),
                ),
                gap="12px",
                align="center",
            ),
            align="center",
            width="100%",
            padding_x="28px",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="1000",
        padding_y="17px",
        background="linear-gradient(to bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%)",
    )


def hero_section() -> rx.Component:
    """Sección hero grande con Frieren y los dos botones."""
    return rx.box(
        # Degradado oscuro en el lado izquierdo (para que el texto se lea bien)
        rx.box(
            position="absolute",
            top="0",
            left="0",
            bottom="0",
            width="65%",
            background="linear-gradient(to right, #0d0d0d 42%, transparent 100%)",
            z_index="1",
        ),
        # Degradado oscuro en la parte de abajo
        rx.box(
            position="absolute",
            left="0",
            right="0",
            bottom="0",
            height="55%",
            background="linear-gradient(to top, #0d0d0d 0%, transparent 100%)",
            z_index="1",
        ),
        # Contenido: título, descripción y botones
        rx.box(
            rx.vstack(
                rx.text(
                    "Frieren: Beyond Journey's End",
                    font_size="43px",
                    font_weight="800",
                    color="white",
                    line_height="1.08",
                    max_width="490px",
                ),
                rx.text(
                    "An elven mage begins a new journey after the hero's quest ends, confronting time, loss, "
                    "and memories. As her companions fade, she learns what it truly means to understand "
                    "and cherish human connections.",
                    color="#cccccc",
                    font_size="13px",
                    max_width="415px",
                    line_height="1.65",
                ),
                rx.hstack(
                    # ▶ BOTÓN PLAY — El único con función interna (navega a /frieren)
                    rx.link(
                        rx.hstack(
                            rx.text("▶", color="#111111", font_size="12px"),
                            rx.text("Play", color="#111111", font_weight="700", font_size="15px"),
                            gap="6px",
                            align="center",
                            background="white",
                            border_radius="22px",
                            padding_x="22px",
                            padding_y="9px",
                            cursor="pointer",
                        ),
                        href="/frieren",
                        text_decoration="none",
                    ),
                    # Botón More Info — Solo visual, sin función
                    rx.box(
                        rx.text(
                            "More Info",
                            color="white",
                            font_weight="500",
                            font_size="15px",
                        ),
                        background="rgba(255,255,255,0.13)",
                        border="1px solid rgba(255,255,255,0.28)",
                        border_radius="22px",
                        padding_x="22px",
                        padding_y="9px",
                        cursor="pointer",
                    ),
                    gap="12px",
                    margin_top="8px",
                ),
                align_items="flex-start",
                gap="16px",
            ),
            position="absolute",
            bottom="68px",
            left="28px",
            z_index="2",
        ),
        position="relative",
        width="100%",
        height="540px",
        # Fondo que simula los colores cálidos/rosados del anime Frieren
        background="linear-gradient(135deg, #1a0818 0%, #3a1030 25%, #4a1d3a 45%, #6a3555 65%, #7a4060 80%, #5a2848 100%)",
        overflow="hidden",
    )


def anime_card(title: str, gradient: str, badge: str = "") -> rx.Component:
    """Tarjeta individual de anime (imagen + título)."""
    # Si tiene badge "New Season", lo creamos; si no, ponemos un box vacío
    badge_element = (
        rx.box(
            rx.text(badge, color="white", font_size="10px", font_weight="600"),
            background="rgba(70,175,200,0.28)",
            border_bottom="2px solid #46AFC8",
            padding_x="8px",
            padding_y="4px",
            position="absolute",
            top="0",
            left="0",
            right="0",
            text_align="center",
            z_index="1",
        )
        if badge
        else rx.box()
    )

    return rx.box(
        # Área de la imagen (simulada con gradiente de color)
        rx.box(
            badge_element,
            background=gradient,
            width=CARD_W,
            height=CARD_H,
            border_radius="10px",
            position="relative",
            overflow="hidden",
            flex_shrink="0",
        ),
        # Título debajo de la imagen
        rx.text(
            title,
            color="white",
            font_size="12px",
            font_weight="500",
            margin_top="9px",
            width=CARD_W,
            line_height="1.4",
        ),
        flex_shrink="0",
        width=CARD_W,
        cursor="pointer",
    )


def anime_row(data: list) -> rx.Component:
    """Fila horizontal scrolleable de tarjetas de anime."""
    cards = [
        anime_card(
            title=item["title"],
            gradient=item["gradient"],
            badge=item.get("badge", ""),
        )
        for item in data
    ]
    return rx.box(
        rx.hstack(
            *cards,
            gap="16px",
            padding_bottom="8px",
        ),
        overflow_x="auto",
        width="100%",
        # Ocultar la barra de scroll para que se vea limpio
        style={
            "scrollbar_width": "none",
            "-ms-overflow-style": "none",
        },
    )


def genre_pills() -> rx.Component:
    """Fila de píldoras de géneros (All Genres, Action, Fantasy, etc.)."""
    pills = []
    for i, genre in enumerate(GENRES):
        if i == 0:
            # "All Genres" está seleccionado → fondo blanco
            pill = rx.box(
                rx.text(
                    genre,
                    color="#111111",
                    font_size="13px",
                    font_weight="600",
                    white_space="nowrap",
                ),
                background="white",
                border_radius="20px",
                padding_x="16px",
                padding_y="7px",
                flex_shrink="0",
                cursor="pointer",
            )
        else:
            # Los demás → borde gris oscuro
            pill = rx.box(
                rx.text(
                    genre,
                    color="#cccccc",
                    font_size="13px",
                    white_space="nowrap",
                ),
                border="1px solid #333333",
                border_radius="20px",
                padding_x="16px",
                padding_y="7px",
                flex_shrink="0",
                cursor="pointer",
            )
        pills.append(pill)

    return rx.box(
        rx.hstack(*pills, gap="10px", padding_bottom="4px"),
        overflow_x="auto",
        width="100%",
        style={
            "scrollbar_width": "none",
            "-ms-overflow-style": "none",
        },
    )


def content_section(title: str, data: list) -> rx.Component:
    """Sección con título y fila de tarjetas (Trending Now, Continue Watching, etc.)."""
    return rx.vstack(
        rx.text(
            title,
            color="white",
            font_size="18px",
            font_weight="700",
        ),
        anime_row(data),
        align_items="flex-start",
        width="100%",
        gap="14px",
    )