import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --- Configuración general de la página ---
st.set_page_config(
    page_title="🎨 ArtBoard - Crea tu propio dibujo",
    page_icon="🖌️",
    layout="centered"
)

# --- Encabezado tipo página web ---
st.markdown("""
<h1 style='text-align: center; color: #FFB703;'>
🎨 ArtBoard - Crea tu propio dibujo
</h1>
<p style='text-align: center; color: #555; font-size: 18px;'>
Da rienda suelta a tu creatividad. Usa las herramientas del panel lateral para personalizar el tablero y dibujar libremente.
</p>
<hr style='border: 1px solid #ccc;'>
""", unsafe_allow_html=True)

# --- Barra lateral ---
with st.sidebar:
    st.header("⚙️ Propiedades del Tablero")
    st.markdown("Ajusta los parámetros de tu lienzo antes de comenzar a dibujar:")

    # Dimensiones del tablero
    st.subheader("🖼️ Dimensiones")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Herramienta de dibujo
    st.subheader("🖊️ Herramienta")
    drawing_mode = st.selectbox(
        "Selecciona una herramienta:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        help="Cambia el modo de dibujo para crear diferentes figuras."
    )

    # Propiedades del trazo
    st.subheader("🎨 Estilo del trazo")
    stroke_width = st.slider("Grosor de línea", 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")

    # Fondo del lienzo
    st.subheader("🌈 Fondo")
    bg_color = st.color_picker("Color de fondo", "#000000")

# --- Área principal del lienzo ---
st.markdown("""
<h3 style='color:#FFB703;'>🖌️ Tu espacio creativo</h3>
<p style='color:#777;'>Dibuja directamente sobre el lienzo. Puedes ajustar las herramientas en cualquier momento desde el panel lateral.</p>
""", unsafe_allow_html=True)

# --- Creación del canvas interactivo ---
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno semitransparente
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}"  # Clave dinámica según tamaño
)

# --- Pie de página ---
st.markdown("""
<hr style='border: 1px solid #ccc;'>
<p style='text-align: center; color: #999; font-size: 14px;'>
Desarrollado con ❤️ en Streamlit — Explora, dibuja y crea.
</p>
""", unsafe_allow_html=True)
