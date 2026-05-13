# anime_streaming/anime_streaming.py

import reflex as rx
from anime_streaming.components import (
    navbar,
    hero_section,
    content_section,
    genre_pills,
)
from anime_streaming.data import TRENDING_ANIME, CONTINUE_WATCHING, RECOMMENDED

BG = "#0d0d0d"


def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero_section(),
        rx.vstack(
            content_section("Trending Now", TRENDING_ANIME),
            genre_pills(),
            content_section("Continue Watching for You", CONTINUE_WATCHING),
            content_section("Recommended For You", RECOMMENDED),
            align_items="flex-start",
            gap="32px",
            padding_x="28px",
            padding_top="28px",
            padding_bottom="50px",
            width="100%",
        ),
        background=BG,
        min_height="100vh",
    )


def frieren_detail() -> rx.Component:
    return rx.box(
        # Navbar con botón volver
        rx.box(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.text("←", color="white", font_size="22px"),
                        rx.text("Volver", color="white", font_size="15px", font_weight="500"),
                        gap="8px",
                        align="center",
                    ),
                    href="/",
                    text_decoration="none",
                ),
                rx.spacer(),
                rx.text(
                    "Frieren: Beyond Journey's End",
                    color="white",
                    font_weight="600",
                    font_size="16px",
                ),
                rx.spacer(),
                align="center",
                width="100%",
                padding_x="28px",
            ),
            position="sticky",
            top="0",
            z_index="1000",
            padding_y="18px",
            background="rgba(13,13,13,0.96)",
            backdrop_filter="blur(10px)",
        ),
        # Banner con imagen real
        rx.box(
            rx.image(
                src="/banner.jpg",
                width="100%",
                height="100%",
                object_fit="cover",
                position="absolute",
                top="0",
                left="0",
            ),
            rx.box(
                position="absolute", top="0", left="0", bottom="0", width="62%",
                background="linear-gradient(to right, #0d0d0d 40%, transparent 100%)",
                z_index="1",
            ),
            rx.box(
                position="absolute", left="0", right="0", bottom="0", height="60%",
                background="linear-gradient(to top, #0d0d0d 0%, transparent 100%)",
                z_index="1",
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        "Frieren: Beyond Journey's End",
                        font_size="38px",
                        font_weight="800",
                        color="white",
                        line_height="1.1",
                        max_width="490px",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.text("⭐ 9.4", color="white", font_size="13px", font_weight="700"),
                            background="rgba(255,200,0,0.18)",
                            border="1px solid rgba(255,200,0,0.4)",
                            border_radius="6px",
                            padding_x="10px",
                            padding_y="4px",
                        ),
                        rx.text("2023", color="#999999", font_size="13px"),
                        rx.text("28 eps", color="#999999", font_size="13px"),
                        rx.text("TV", color="#999999", font_size="13px"),
                        gap="12px",
                        align="center",
                    ),
                    rx.text(
                        "An elven mage begins a new journey after the hero's quest ends, "
                        "confronting time, loss, and memories. As her companions fade, she learns "
                        "what it truly means to understand and cherish human connections.",
                        color="#cccccc",
                        font_size="14px",
                        max_width="440px",
                        line_height="1.65",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.text("▶  Reproducir", color="#111111", font_weight="700", font_size="15px"),
                            background="white",
                            border_radius="22px",
                            padding_x="28px",
                            padding_y="10px",
                            cursor="pointer",
                        ),
                        rx.box(
                            rx.text("+ Mi Lista", color="white", font_weight="500", font_size="15px"),
                            background="rgba(255,255,255,0.13)",
                            border="1px solid rgba(255,255,255,0.28)",
                            border_radius="22px",
                            padding_x="24px",
                            padding_y="10px",
                            cursor="pointer",
                        ),
                        gap="12px",
                        margin_top="8px",
                    ),
                    align_items="flex-start",
                    gap="16px",
                ),
                position="absolute",
                bottom="55px",
                left="28px",
                z_index="2",
            ),
            position="relative",
            width="100%",
            height="480px",
            overflow="hidden",
            background="#0d0d0d",
        ),
        # Lista de episodios
        rx.vstack(
            rx.text("Episodios", color="white", font_size="20px", font_weight="700"),
            *[
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.image(
                                src="/banner.jpg",
                                width="100%",
                                height="100%",
                                object_fit="cover",
                                border_radius="8px",
                            ),
                            rx.box(
                                rx.text(f"EP {i}", color="white", font_size="11px", font_weight="700"),
                                position="absolute",
                                bottom="6px",
                                left="8px",
                                background="rgba(0,0,0,0.65)",
                                border_radius="4px",
                                padding_x="6px",
                                padding_y="2px",
                                z_index="1",
                            ),
                            position="relative",
                            width="105px",
                            height="66px",
                            border_radius="8px",
                            overflow="hidden",
                            flex_shrink="0",
                        ),
                        rx.vstack(
                            rx.text(
                                [
                                    "La promesa del héroe",
                                    "El largo viaje comienza",
                                    "Recuerdos del pasado",
                                    "Nuevos compañeros",
                                    "El camino al norte",
                                    "La magia de los elfos",
                                ][i - 1],
                                color="white",
                                font_size="14px",
                                font_weight="600",
                            ),
                            rx.text("24 min  •  Sub español", color="#777777", font_size="12px"),
                            align_items="flex-start",
                            gap="4px",
                        ),
                        align="center",
                        gap="16px",
                        width="100%",
                    ),
                    background="#1a1a1a",
                    border_radius="10px",
                    padding="14px",
                    width="100%",
                    cursor="pointer",
                )
                for i in range(1, 7)
            ],
            align_items="flex-start",
            width="100%",
            gap="12px",
            padding_x="28px",
            padding_top="28px",
            padding_bottom="50px",
        ),
        background=BG,
        min_height="100vh",
    )


app = rx.App(
    style={
        "font_family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
        "background_color": BG,
        "color": "white",
        "box_sizing": "border-box",
        "margin": "0",
        "padding": "0",
    }
)

app.add_page(index, route="/")
app.add_page(frieren_detail, route="/frieren")