import reflex as rx

config = rx.Config(
    app_name="anime_streaming",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)