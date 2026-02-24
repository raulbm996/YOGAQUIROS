import os
import re

files = [
    'clases.html',
    'contacto.html',
    'horarios-tarifas.html',
    'reservas.html',
    'sobre-nosotros.html'
]

new_header = """    <!-- ===== TOP BAR ===== -->
    <div class="top-bar">
        <div class="container">
            <a href="#" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
        </div>
    </div>

    <!-- ===== HEADER ===== -->
    <header>
        <nav class="nav-container">
            <a href="index.html" class="logo">
                <img src="assets/images/logo.png" alt="Yoga Quirós" class="logo-img" style="height: 55px; mix-blend-mode: multiply;">
            </a>
            <div class="nav-menu" id="navMenu">
                <a href="index.html">Inicio</a>
                <a href="sobre-nosotros.html" class="{sobre_active}">Sobre nosotros</a>
                <a href="clases.html" class="{clases_active}">Qué ofrecemos</a>
                <a href="horarios-tarifas.html" class="{horarios_active}">Horarios y Tarifas</a>
                <a href="reservas.html" class="{reservas_active}">Reservas</a>
                <a href="contacto.html" class="{contacto_active}">Contacto</a>
            </div>
            <div class="hamburger" id="hamburger" onclick="toggleMenu()">
                <span></span><span></span><span></span>
            </div>
        </nav>
    </header>"""

new_footer = """    <!-- ===== FOOTER ===== -->
    <footer>
        <div class="footer-main">
            <div class="container">
                <div class="footer-grid">
                    <div class="footer-col">
                        <img src="assets/images/logo.png" alt="Yoga Quirós" class="footer-logo-img">
                        <h3>Sobre Nosotros</h3>
                        <p>Centro dedicado a llevar los beneficios del Yoga y la relajación profunda a tu vida de manera profesional y personal.</p>
                        <p style="margin-top: 10px; font-weight: 500;">Encuéntranos en:</p>
                        <div class="footer-social">
                            <a href="#" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                            <a href="#" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        </div>
                    </div>
                    <div class="footer-col">
                        <h3>Donde Estamos</h3>
                        <div class="footer-contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <a href="#" target="_blank" rel="noopener">Centro Histórico<br>41001 Sevilla</a>
                        </div>
                        <div class="footer-contact-item">
                            <i class="fas fa-phone-alt"></i>
                            <div><a href="tel:+34">Telf. aquí</a></div>
                        </div>
                        <div class="footer-contact-item">
                            <i class="fas fa-envelope"></i>
                            <a href="mailto:info@yogaquiros.com">info@yogaquiros.com</a>
                        </div>
                    </div>
                    <div class="footer-col">
                        <h3>Contacto</h3>
                        <form class="footer-form">
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                                <input type="text" name="nombre" placeholder="Nombre *" required>
                                <input type="email" name="email" placeholder="Email *" required>
                            </div>
                            <input type="tel" name="telefono" placeholder="Teléfono">
                            <textarea name="mensaje" placeholder="Mensaje *" required></textarea>
                            <button type="submit" class="btn-send">Enviar Mensaje</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                <p>Copyright &copy; 2026 - YOGA QUIRÓS | Todos los derechos reservados</p>
            </div>
        </div>
    </footer>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Format active classes
    header_to_insert = new_header.format(
        sobre_active='active' if f == 'sobre-nosotros.html' else '',
        clases_active='active' if f == 'clases.html' else '',
        horarios_active='active' if f == 'horarios-tarifas.html' else '',
        reservas_active='active' if f == 'reservas.html' else '',
        contacto_active='active' if f == 'contacto.html' else ''
    )

    # Remove old header
    content = re.sub(r'<!-- Header Navigation -->\s*<header>.*?</header>',
                     header_to_insert, content, flags=re.DOTALL)
    # Fallback if no comment
    content = re.sub(r'<header>.*?</header>',
                     header_to_insert, content, flags=re.DOTALL)

    # Remove old footer
    content = re.sub(r'<!-- Footer -->\s*<footer>.*?</footer>',
                     new_footer, content, flags=re.DOTALL)
    content = re.sub(r'<footer>.*?</footer>', new_footer,
                     content, flags=re.DOTALL)

    # Fix links for font-awesome if missing
    if 'font-awesome' not in content:
        content = content.replace(
            '</head>', '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n</head>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Updated {f}")
