# anime_streaming/components.py

import reflex as rx
from anime_streaming.data import GENRES

CARD_W = "158px"
CARD_H = "218px"


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/logo.png",
                width="32px",
                height="32px",
                border_radius="50%",
                object_fit="cover",
            ),
            rx.hstack(
                rx.text("Home", color="white", font_weight="700", font_size="14px", cursor="pointer"),
                rx.text("My List", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("Movie", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("New Season", color="#888888", font_size="14px", cursor="pointer"),
                rx.text("Language", color="#888888", font_size="14px", cursor="pointer"),
                gap="24px",
                align="center",
            ),
            rx.spacer(),
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
            rx.hstack(
                rx.text("🔔", color="#777777", font_size="19px", cursor="pointer"),
                rx.image(
                    src="/avatar.jpg",
                    width="34px",
                    height="34px",
                    border_radius="50%",
                    object_fit="cover",
                    border="2px solid #444444",
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
    return rx.box(
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
            position="absolute",
            top="0", left="0", bottom="0",
            width="65%",
            background="linear-gradient(to right, #0d0d0d 42%, transparent 100%)",
            z_index="1",
        ),
        rx.box(
            position="absolute",
            left="0", right="0", bottom="0",
            height="55%",
            background="linear-gradient(to top, #0d0d0d 0%, transparent 100%)",
            z_index="1",
        ),
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
                    rx.box(
                        rx.text("More Info", color="white", font_weight="500", font_size="15px"),
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
        overflow="hidden",
        background="#0d0d0d",
    )


def anime_card(title: str, image: str, badge: str = "") -> rx.Component:
    badge_element = (
        rx.box(
            rx.text(badge, color="white", font_size="10px", font_weight="600"),
            background="rgba(70,175,200,0.28)",
            border_bottom="2px solid #46AFC8",
            padding_x="8px",
            padding_y="4px",
            position="absolute",
            top="0", left="0", right="0",
            text_align="center",
            z_index="1",
        )
        if badge
        else rx.box()
    )

    return rx.box(
        rx.box(
            rx.image(
                src=image,
                width="100%",
                height="100%",
                object_fit="cover",
                border_radius="10px",
            ),
            badge_element,
            width=CARD_W,
            height=CARD_H,
            border_radius="10px",
            position="relative",
            overflow="hidden",
            flex_shrink="0",
        ),
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
    cards = [
        anime_card(
            title=item["title"],
            image=item["image"],
            badge=item.get("badge", ""),
        )
        for item in data
    ]
    return rx.box(
        rx.hstack(*cards, gap="16px", padding_bottom="8px"),
        overflow_x="auto",
        width="100%",
        style={"scrollbar_width": "none", "-ms-overflow-style": "none"},
    )


def genre_pills() -> rx.Component:
    pills = []
    for i, genre in enumerate(GENRES):
        if i == 0:
            pill = rx.box(
                rx.text(genre, color="#111111", font_size="13px", font_weight="600", white_space="nowrap"),
                background="white",
                border_radius="20px",
                padding_x="16px",
                padding_y="7px",
                flex_shrink="0",
                cursor="pointer",
            )
        else:
            pill = rx.box(
                rx.text(genre, color="#cccccc", font_size="13px", white_space="nowrap"),
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
        style={"scrollbar_width": "none", "-ms-overflow-style": "none"},
    )


def content_section(title: str, data: list) -> rx.Component:
    return rx.vstack(
        rx.text(title, color="white", font_size="18px", font_weight="700"),
        anime_row(data),
        align_items="flex-start",
        width="100%",
        gap="14px",
    )